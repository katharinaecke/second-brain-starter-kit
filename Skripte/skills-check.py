#!/usr/bin/env python3
# Skills-Check: haelt die drei Stellen zusammen, an denen ein Skill sich beschreibt.
#
# Ein Skill steht immer an drei Orten, und die laufen erfahrungsgemaess auseinander:
#   1. .agents/skills/<slug>/SKILL.md  -- die eigentliche Anleitung (SSOT), mit einer
#      "**Ausloeser:**"-Kopfzeile im Body und `description:` im Frontmatter
#   2. .claude/skills/<slug>/SKILL.md  -- der duenne Zeiger, dessen `description:` Claude
#      Code vorab laedt, um zu entscheiden, wann der Skill dran ist
#   3. AGENTS.md                       -- die Ausloese-Tabelle fuer Tools OHNE eigene
#      Skill-Mechanik; fuer die ist sie die einzige Quelle
#
# Dieses Skript ERZEUGT nichts - es meldet nur Abweichungen. Bewusst so: die Zeiger und die
# AGENTS-Tabelle enthalten handgeschriebene Formulierungen, die ein Generator platt machen
# wuerde. Bei sehr vielen Skills lohnt ein echter Generator; bis dahin reicht ein Waechter.
#
# Aufruf:
#   python Skripte/skills-check.py            Bericht
#   python Skripte/skills-check.py --check    Exit 1 bei Drift (fuer CI/Gate)
#
# brain-check.py importiert drift_report() und zeigt die Befunde im taeglichen Report mit.
# Quellcode bewusst ASCII, Inhalte mit UTF-8 gelesen.

import os
import re
import sys

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SSOT_DIR = os.path.join(VAULT, '.agents', 'skills')
PARENT = os.path.dirname(VAULT)

# Zeiger und Kontextdatei koennen an ZWEI Orten liegen, und beide sind richtig:
#   - Eigenes Vault-Repo (Normalfall): direkt im Vault.
#   - Vault als Unterordner in einem Anwendungs-Repo: im Repo-Root eine Ebene hoeher, weil
#     Claude Code Skills und Settings nur von dort laedt (siehe
#     README.md#wenn-das-wissen-ins-repo-der-anwendung-soll).
# Deshalb beide Orte pruefen statt einen zu konfigurieren. Eine Konstante, die im zweiten
# Fall von Hand umgestellt werden muesste, bliebe garantiert stehen - und dann meldet dieser
# Waechter bei JEDEM Lauf jeden Skill als "kein Zeiger vorhanden". Der Fehlalarm zaehlt ueber
# skill_drift als harter Punkt und wuerde den taeglichen Hook dauerhaft ausloesen, also genau
# das, was ihn wertlos macht.
POINTER_DIRS = (os.path.join(VAULT, '.claude', 'skills'),
                os.path.join(PARENT, '.claude', 'skills'))
AGENTS_FILES = (os.path.join(VAULT, 'AGENTS.md'),
                os.path.join(PARENT, 'AGENTS.md'))


def pointer_path(slug):
    """Pfad des Zeigers fuer <slug>, egal an welchem der beiden Orte er liegt.

    Gibt den ersten existierenden zurueck, sonst None.
    """
    for d in POINTER_DIRS:
        p = os.path.join(d, slug, 'SKILL.md')
        if os.path.exists(p):
            return p
    return None

# Bootstrap-Skills sind Sonderfaelle: ihre Quelle liegt NICHT in .agents/skills/, sondern als
# Datei im Repo-Root, und sie sollen nach ihrem einen Lauf verschwinden. Sie duerfen also
# weder als "verwaister Zeiger" gelten, noch nach getanem Werk liegenbleiben.
# Aufbau: <slug> -> (Datei solange ungenutzt, Datei nach dem Lauf)
BOOTSTRAP = {'brain-setup': ('SETUP-PROMPT.md', 'SETUP-PROMPT-erledigt.md')}

# "**Ausloeser:**" bzw. "**Auslöser:**" am Zeilenanfang eines Blockquotes, bis zur Leerzeile.
TRIGGER_RE = re.compile(r'\*\*Ausl(?:ö|oe)ser:\*\*(.*?)(?=\n>\s*\n|\n\n)', re.S)
# Phrasen in typografischen oder geraden Anfuehrungszeichen.
PHRASE_RE = re.compile(r'[„“"]([^“”"\n]+)[“”"]')


def read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def frontmatter(text):
    if not text.startswith('---\n'):
        return {}
    end = text.find('\n---', 4)
    if end < 0:
        return {}
    meta = {}
    for line in text[4:end].split('\n'):
        m = re.match(r'^([A-Za-z0-9_-]+):\s*(.*)$', line)
        if m:
            v = m.group(2).strip()
            if len(v) >= 2 and v[0] == v[-1] == '"':
                v = v[1:-1]
            meta[m.group(1)] = v
    return meta


def phrases(text):
    """Ausloese-Phrasen aus einem Text, entdoppelt.

    Zuerst Zeilenumbrueche und Blockquote-Praefixe glaetten: Kopfzeilen sind oft umbrochen,
    und eine ueber zwei Zeilen laufende Phrase wuerde den Anfuehrungszeichen-Paarlauf sonst
    verschieben (der naechste Match startet dann am SCHLIESSENDEN Zeichen und liefert Muell).
    """
    text = re.sub(r'\s*\n\s*>?\s*', ' ', text or '')
    out = []
    for p in PHRASE_RE.findall(text):
        p = p.strip().rstrip('.').strip()
        # Platzhalter-Endungen wie "formulier mir ..." auf den Kern kuerzen
        p = p.replace('…', '').strip()
        if p and p.lower() not in [x.lower() for x in out]:
            out.append(p)
    return out


def slugs():
    if not os.path.isdir(SSOT_DIR):
        return []
    return sorted(n for n in os.listdir(SSOT_DIR)
                  if os.path.isfile(os.path.join(SSOT_DIR, n, 'SKILL.md')))


def drift_report():
    """Liste lesbarer Drift-Befunde. Leer = sauber. Schreibt nichts."""
    out = []
    if not os.path.isdir(SSOT_DIR):
        return out

    # Beide moeglichen Kontextdateien zusammen betrachten: Im Repo-Fall steht die
    # Ausloeser-Tabelle in der AGENTS.md des Repo-Roots, die Vault-AGENTS.md traegt die
    # Navigation. Eine Phrase gilt als vorhanden, wenn sie in einer der beiden steht.
    agents_text = '\n'.join(read(f) for f in AGENTS_FILES if os.path.exists(f))
    agents_lower = agents_text.lower()
    found = set()

    for slug in slugs():
        ssot_path = os.path.join(SSOT_DIR, slug, 'SKILL.md')
        ssot = read(ssot_path)
        meta = frontmatter(ssot)
        found.add(slug)

        if not meta.get('description'):
            out.append('{0}: SSOT hat kein description-Feld im Frontmatter'.format(slug))

        # Ausloeser aus der Kopfzeile der SSOT
        m = TRIGGER_RE.search(ssot)
        trigger_phrases = phrases(m.group(1)) if m else []
        if not trigger_phrases:
            out.append('{0}: keine Ausloeser-Phrasen in der "**Ausloeser:**"-Kopfzeile '
                       'gefunden'.format(slug))

        # 2. Zeiger vorhanden und beschreibt er dieselben Ausloeser?
        ptr_path = pointer_path(slug)
        if ptr_path is None:
            out.append('{0}: kein Zeiger unter .claude/skills/ (Skill ist in Claude Code '
                       'nicht als /{0} verfuegbar)'.format(slug))
        else:
            ptr_meta = frontmatter(read(ptr_path))
            if ptr_meta.get('name') and ptr_meta['name'] != slug:
                out.append('{0}: Zeiger hat name "{1}" statt "{0}"'.format(
                    slug, ptr_meta['name']))
            ptr_desc = (ptr_meta.get('description') or '').lower()
            if not ptr_desc:
                out.append('{0}: Zeiger hat keine description (Claude Code kann den Skill '
                           'dann nicht von selbst waehlen)'.format(slug))
            else:
                fehlt = [p for p in trigger_phrases if p.lower() not in ptr_desc]
                if fehlt:
                    out.append('{0}: Zeiger-description kennt diese Ausloeser nicht: {1}'.format(
                        slug, ', '.join('"{0}"'.format(x) for x in fehlt)))

        # 3. AGENTS.md - fuer Tools ohne Skill-Mechanik die einzige Quelle
        if agents_text:
            if slug not in agents_lower:
                out.append('{0}: kommt in AGENTS.md nicht vor (fuer Codex/Cursor damit gar '
                           'nicht ausloesbar)'.format(slug))
            else:
                fehlt = [p for p in trigger_phrases if p.lower() not in agents_lower]
                if fehlt:
                    out.append('{0}: AGENTS.md kennt diese Ausloeser nicht: {1}'.format(
                        slug, ', '.join('"{0}"'.format(x) for x in fehlt)))

    # Verwaiste Zeiger ohne SSOT, ueber beide moeglichen Zeiger-Orte.
    # Wichtig im Repo-Fall: Im .claude/skills/ eines Anwendungs-Repos liegen oft auch
    # projekteigene Skills (deploy, test, ...), die mit dem Vault nichts zu tun haben. Die
    # duerfen hier nicht als "verwaist" gelten. Erkennungsmerkmal eines Vault-Zeigers ist,
    # dass er auf .agents/skills/ verweist - genau das macht ihn zum Zeiger.
    gesehen = set()
    for pdir in POINTER_DIRS:
        if not os.path.isdir(pdir):
            continue
        for name in sorted(os.listdir(pdir)):
            if not os.path.isdir(os.path.join(pdir, name)) or name in found or name in gesehen:
                continue
            skill_md = os.path.join(pdir, name, 'SKILL.md')
            if name not in BOOTSTRAP:
                if not os.path.exists(skill_md):
                    continue
                if '.agents/skills/' not in read(skill_md):
                    continue  # fremder Skill des Projekts, nicht unsere Baustelle
            gesehen.add(name)
            if name in BOOTSTRAP:
                quelle, danach = BOOTSTRAP[name]
                if os.path.exists(os.path.join(VAULT, quelle)):
                    continue  # Setup steht noch aus - Zeiger gehoert hierher
                if os.path.exists(os.path.join(VAULT, danach)):
                    out.append('{0}: Setup ist gelaufen ({1} existiert), aber der '
                               'Bootstrap-Skill liegt noch unter .claude/skills/ - er sollte '
                               'sich danach selbst entfernen'.format(name, danach))
                else:
                    out.append('{0}: Zeiger da, aber weder {1} noch {2} gefunden - der Skill '
                               'zeigt ins Leere'.format(name, quelle, danach))
                continue
            out.append('{0}: Zeiger ohne zugehoerige SSOT unter .agents/skills/'.format(name))

    # AGENTS.md bewirbt Skills, die es nicht (mehr) gibt. Das ist der Normalfall NACH einem
    # Setup - dort werden nicht gebrauchte Skills geloescht, und die Tabelle bleibt gern
    # stehen. Von den vorhandenen Skills aus ist dieser Fall unsichtbar, deshalb hier
    # umgekehrt: was verweist AGENTS.md auf .agents/skills/, das gar nicht existiert?
    for m in re.finditer(r'\.agents/skills/([A-Za-z0-9_-]+)/SKILL\.md', agents_text):
        slug = m.group(1)
        if slug not in found:
            out.append('AGENTS.md verweist auf "{0}", aber .agents/skills/{0}/ existiert '
                       'nicht (geloeschter Skill in der Tabelle stehengeblieben?)'.format(slug))

    return out


def main():
    findings = drift_report()
    print('SSOT   : {0}'.format(SSOT_DIR))
    print('Zeiger : {0}'.format(' | '.join(
        d for d in POINTER_DIRS if os.path.isdir(d)) or '(keiner gefunden)'))
    print('Skills : {0}'.format(len(slugs())))
    print('')
    if not findings:
        print('Kein Drift.')
        return
    print('DRIFT ({0}):'.format(len(findings)))
    for f in findings:
        print('  - {0}'.format(f))
    if '--check' in sys.argv:
        sys.exit(1)


if __name__ == '__main__':
    main()
