#!/usr/bin/env python3
# Testlauf fuer die beiden Vault-Skripte. Reines Python 3 ohne Fremdpakete, wie sie selbst.
#
#   python tests/run-tests.py
#
# WOFUER: Beim Setup wird `Skripte/brain-check.py` aktiv umgebaut (Ordnernamen,
# TICKET_FOLDER, SICHTBARKEIT_SCOPE). Genau dabei geht leicht etwas kaputt, ohne dass es
# auffaellt: Ein Check, dessen Bedingung nicht mehr greift, meldet einfach dauerhaft
# "(keine)" und sieht damit aus wie ein sauberer Vault. Dieser Lauf baut deshalb einen
# Wegwerf-Vault, in dem JEDER Check genau einmal ausgeloest wird, und prueft, ob auch jeder
# anschlaegt.
#
# Die Tests fassen weder dein Vault noch dieses Repo an. Alle Fixtures entstehen in einem
# temporaeren Ordner und werden danach geloescht.
#
# Dieser Ordner gehoert NICHT in ein fertiges Brain. Er wird beim Setup nicht mitkopiert,
# siehe die Liste in SETUP-PROMPT.md.
#
# Quellcode bewusst ASCII, Vault-Inhalt mit UTF-8 geschrieben.

import io
import os
import re
import shutil
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable

# Die geprueften Skripte geben Dateinamen aus, und die enthalten im Test bewusst Umlaute.
# Ohne diese Vorgabe schreibt der Kindprozess unter Windows in der Konsolen-Kodierung
# (cp1252), waehrend hier UTF-8 gelesen wird - der Test wuerde an seinem eigenen Aufbau
# scheitern statt am Pruefling.
UMGEBUNG = dict(os.environ, PYTHONIOENCODING='utf-8')


def starte(vault, skript, *args):
    return subprocess.run([PY, os.path.join(vault, 'Skripte', skript)] + list(args),
                          capture_output=True, text=True, encoding='utf-8',
                          errors='replace', cwd=vault, env=UMGEBUNG)

fehler = []
gelaufen = []


def sagt(bedingung, text):
    gelaufen.append(text)
    if not bedingung:
        fehler.append(text)
    print('  {0}  {1}'.format('ok  ' if bedingung else 'FEHL', text))


def w(vault, rel, text):
    p = os.path.join(vault, rel.replace('/', os.sep))
    d = os.path.dirname(p)
    if d:
        os.makedirs(d, exist_ok=True)
    io.open(p, 'w', encoding='utf-8', newline='').write(text)


def kit_kopieren(vault, mit_setup_prompt=False, mit_bootstrap=True):
    """Legt einen Vault an, wie ihn das Setup erzeugt."""
    for d in ('.agents', 'Vorlagen', 'Skripte'):
        shutil.copytree(os.path.join(REPO, d), os.path.join(vault, d),
                        ignore=shutil.ignore_patterns('__pycache__'))
    ignore = None if mit_bootstrap else shutil.ignore_patterns('brain-setup')
    shutil.copytree(os.path.join(REPO, '.claude', 'skills'),
                    os.path.join(vault, '.claude', 'skills'), ignore=ignore)
    for f in ('AGENTS.md', 'CLAUDE.md', 'ARCHITECTURE.md'):
        shutil.copy(os.path.join(REPO, f), vault)
    if mit_setup_prompt:
        shutil.copy(os.path.join(REPO, 'SETUP-PROMPT.md'), vault)


def lauf(vault, *args):
    return starte(vault, 'brain-check.py', *args)


def skills_lauf(vault):
    return starte(vault, 'skills-check.py')


def treffer(report, titelteil):
    """Anzahl aus der Ueberschrift '## ... (N)' zur genannten Kategorie."""
    m = re.search(r'(?m)^## .*' + re.escape(titelteil) + r'.*\((\d+)\)\s*$', report)
    return int(m.group(1)) if m else -1


FM = "---\ntags: [t]\nthemengebiet: test\ntype: Konzept\ndescription: x\n---\n\n"


def test_alle_kategorien(tmp):
    """Jeden Check genau einmal ausloesen und pruefen, dass er anschlaegt."""
    print('\n[1] Schlaegt jede Kategorie an?')
    v = os.path.join(tmp, 'kategorien')
    os.makedirs(v)
    kit_kopieren(v, mit_bootstrap=False)

    w(v, 'Wissen/Kaputt.md', FM + "# Kaputt\n\n## Verwandt\n"
      "- [Weg](</Wissen/Gibts-Nicht.md>): toter Link\n- [Gut](</Wissen/Gut.md>): ok\n")
    w(v, 'Wissen/Gut.md', FM + "# Gut\n\n## Verwandt\n"
      "- [Kaputt](</wissen/Kaputt.md>): falsche Gross-/Kleinschreibung\n"
      "- [Backtick](</Wissen/Backtick.md>): zweiter\n")
    w(v, 'Wissen/Backtick.md', FM + "# Backtick\n\nSiehe `[Gut](</Wissen/Gut.md>)` im Code-Span.\n\n"
      "## Verwandt\n- [Gut](</Wissen/Gut.md>): a\n- [Kaputt](</Wissen/Kaputt.md>): b\n")
    w(v, 'Wissen/Einsam.md', FM + "# Einsam\n\n## Verwandt\n- niemand\n")
    w(v, 'Wissen/OhneFM.md', "---\ntags: [t]\nthemengebiet:\ntype: Konzept\n---\n\n"
      "# OhneFM\n\n## Verwandt\n- x\n")
    w(v, 'Wissen/OhneVerwandt.md', FM + "# OhneVerwandt\n\nText.\n")
    w(v, 'MOCs/Test.md', "---\ntype: MOC\ntags: [moc]\nthemengebiet: test\ndescription: x\n---\n\n"
      "# Test\n\n- [Gut](</Wissen/Gut.md>): drin\n")
    w(v, 'Wissen/Vorne.md', FM + "# Vorne\n\n## Verwandt\n"
      "- [Hinten](</Wissen/Hinten.md>): einseitig\n- [Gut](</Wissen/Gut.md>): zweiter\n")
    w(v, 'Wissen/Hinten.md', FM + "# Hinten\n\n## Verwandt\n"
      "- [Gut](</Wissen/Gut.md>): kein Ruecklink auf Vorne\n"
      "- [Backtick](</Wissen/Backtick.md>): zweiter\n")
    w(v, 'Wissen/Riesig.md', FM + "# Riesig\n\n" + ("Fuelltext. " * 1200) +
      "\n\n## Verwandt\n- [Gut](</Wissen/Gut.md>): a\n- [Kaputt](</Wissen/Kaputt.md>): b\n")
    w(v, 'Tickets/Ohne-Praefix.md', "---\ntype: Vorgang\ndescription: x\ntags: [v]\n---\n\n# Ohne\n\n"
      "## Verwandt\n- [Gut](</Wissen/Gut.md>): a\n- [Kaputt](</Wissen/Kaputt.md>): b\n")
    w(v, 'Wissen/Umlaut-ä.md', FM + "# Umlaut\n\n## Verwandt\n"
      "- [Gut](</Wissen/Gut.md>): a\n- [Kaputt](</Wissen/Kaputt.md>): b\n")
    w(v, 'Projekte/Log.md', "---\ntype: Projekt\ndescription: x\ntags: [p]\n---\n\n# Log\n\n"
      "- **2026-08-14** " + ("sehr langer Eintrag " * 40) + "\n\n## Verwandt\n"
      "- [Gut](</Wissen/Gut.md>): a\n- [Kaputt](</Wissen/Kaputt.md>): b\n")
    w(v, 'Wissen/Abgelaufen.md', "---\ntags: [t]\nthemengebiet: test\ntype: Referenz\n"
      "description: x\nstale_after: 2020-01-01\n---\n\n# Abgelaufen\n\n## Verwandt\n"
      "- [Gut](</Wissen/Gut.md>): a\n- [Kaputt](</Wissen/Kaputt.md>): b\n")
    w(v, 'Projekte/Klassifiziert.md', "---\ntype: Projekt\ndescription: x\ntags: [p]\n"
      "sichtbarkeit: intern\n---\n\n# K\n\n## Verwandt\n- [Gut](</Wissen/Gut.md>): a\n"
      "- [Kaputt](</Wissen/Kaputt.md>): b\n")
    # kaputte Kodierung: bewusst kein UTF-8
    open(os.path.join(v, 'Wissen', 'Latin1.md'), 'wb').write(
        b'---\ntags: [x]\nthemengebiet: test\n---\n\n# Caf\xe9 Cr\xe8me\n')
    # Kontextbudget sprengen. Die Groesse aus der Konstante des Prueflings ableiten statt
    # eine Zahl zu raten: Wird das Budget spaeter geaendert, faellt der Test sonst still
    # durch, weil die Fuellung nicht mehr reicht.
    budget = 30720
    m = re.search(r'(?m)^CONTEXT_BUDGET\s*=\s*(\d+)',
                  io.open(os.path.join(v, 'Skripte', 'brain-check.py'), encoding='utf-8').read())
    if m:
        budget = int(m.group(1))
    p = os.path.join(v, 'AGENTS.md')
    s = io.open(p, encoding='utf-8').read()
    zeile = '<!-- Fuelltext -->\n'
    noetig = (budget - len(s.encode('utf-8'))) // len(zeile) + 50
    io.open(p, 'w', encoding='utf-8', newline='').write(s + '\n' + zeile * max(noetig, 1))
    # Skill-Drift: Zeiger ohne SSOT
    w(v, '.claude/skills/geisterskill/SKILL.md',
      "---\nname: geisterskill\ndescription: zeigt auf .agents/skills/geisterskill/SKILL.md\n---\n\nx\n")

    r = lauf(v)
    sagt(r.returncode == 0, 'Report laeuft fehlerfrei durch')
    rep = r.stdout
    for titel, name in [
            ('kaputter Kodierung', 'kaputte Kodierung'),
            ('Kaputte / verdaechtige', 'kaputte Links'),
            ('falscher Gross-', 'Case-Fehler in Links'),
            ('Backtick-Links', 'Backtick-Links'),
            ('Isolierte Notizen', 'isolierte Notizen'),
            ('ohne vollstaendiges Frontmatter', 'fehlendes Frontmatter'),
            ('ohne ## Verwandt', 'fehlendes ## Verwandt'),
            ('in keiner MOC', 'nicht in MOC'),
            ('Fehlende Ruecklinks', 'fehlende Ruecklinks'),
            ('Grosse Notizen', 'grosse Notizen'),
            ('ohne ID-Praefix', 'Ticket-Naming'),
            ('Nicht-ASCII', 'Nicht-ASCII-Dateinamen'),
            ('Zu lange Log-Zeilen', 'lange Log-Zeilen'),
            ('Abgelaufen laut stale_after', 'stale_after'),
            ('Skill-Drift', 'Skill-Drift'),
            ('Kontextdateien ueber Budget', 'Kontextbudget'),
            ('Ohne sichtbarkeit', 'fehlende sichtbarkeit')]:
        sagt(treffer(rep, titel) > 0, 'Kategorie schlaegt an: ' + name)
    sagt('intern: 1' in rep, 'sichtbarkeit-Verteilung wird gezaehlt')
    sagt('Wissen/Kaputt.md  ->  Wissen/Gibts-Nicht.md' in rep,
         'toter Link nennt die richtige Datei')
    sagt('heisst wirklich: Wissen/Kaputt.md' in rep,
         'Case-Fehler nennt die echte Schreibweise')

    r = lauf(v, '--summary')
    sagt(r.returncode == 0, 'Summary laeuft fehlerfrei durch')
    r = lauf(v, '--hook')
    sagt(r.returncode == 0, 'Hook laeuft fehlerfrei durch')
    sagt('hookSpecificOutput' in r.stdout, 'Hook meldet, wenn es harte Punkte gibt')


def test_robust(tmp):
    """Kaputte Dateien duerfen den Lauf nie abbrechen, vor allem nicht im Hook."""
    print('\n[2] Robustheit gegen kaputte Dateien')
    v = os.path.join(tmp, 'robust')
    os.makedirs(v)
    kit_kopieren(v, mit_bootstrap=False)
    w(v, 'Wissen/Leer.md', '')
    w(v, 'Wissen/NurStrich.md', '---\n')
    w(v, 'Wissen/Kaputtes-YAML.md', '---\ntags: [unclosed\nthemengebiet\n---\n# x\n')
    open(os.path.join(v, 'Wissen', 'Latin1.md'), 'wb').write(b'---\ntags: [x]\n---\n\n# Caf\xe9\n')
    open(os.path.join(v, 'Wissen', 'bild.png'), 'wb').write(b'\x89PNG\r\n\x1a\n')

    r = lauf(v)
    sagt(r.returncode == 0, 'Report ueberlebt Nicht-UTF-8, leere und kaputte Dateien')
    sagt(treffer(r.stdout, 'kaputter Kodierung') == 1, 'die eine Nicht-UTF-8-Datei wird gemeldet')
    r = lauf(v, '--hook')
    sagt(r.returncode == 0, 'Hook ueberlebt dieselben Dateien (sonst crasht jeder Sessionstart)')


def test_konsolen_kodierung(tmp):
    """Dateinamen mit Zeichen, die die Konsole nicht darstellen kann.

    Unter Windows laeuft die Konsole oft in cp1252. Ein Emoji oder kyrillischer Dateiname
    liess die Ausgabe frueher mit UnicodeEncodeError abbrechen, ausgerechnet in der
    Kategorie, die genau solche Namen melden soll.
    """
    print('\n[3] Dateinamen, die die Konsole nicht darstellen kann')
    v = os.path.join(tmp, 'konsole')
    os.makedirs(v)
    kit_kopieren(v, mit_bootstrap=False)
    w(v, 'Wissen/Emoji-\U0001F680.md', FM + "# E\n\n## Verwandt\n- x\n")
    w(v, 'Wissen/Кириллица.md', FM + "# K\n\n## Verwandt\n- x\n")
    eng = dict(os.environ, PYTHONIOENCODING='cp1252')
    for args, name in ((['--summary'], 'Summary'), ([], 'Report'), (['--hook'], 'Hook')):
        r = subprocess.run([PY, os.path.join(v, 'Skripte', 'brain-check.py')] + args,
                           capture_output=True, text=True, encoding='cp1252',
                           errors='replace', cwd=v, env=eng)
        sagt(r.returncode == 0, '{0} ueberlebt cp1252-Konsole'.format(name))


def test_ohne_tickets(tmp):
    """TICKET_FOLDER = None ist der Normalfall fuer Vaults ohne Arbeitseinheiten."""
    print('\n[4] TICKET_FOLDER = None')
    v = os.path.join(tmp, 'ohnetickets')
    os.makedirs(v)
    kit_kopieren(v, mit_bootstrap=False)
    p = os.path.join(v, 'Skripte', 'brain-check.py')
    s = io.open(p, encoding='utf-8').read().replace("TICKET_FOLDER = 'Tickets/'",
                                                    "TICKET_FOLDER = None")
    io.open(p, 'w', encoding='utf-8', newline='').write(s)
    r = lauf(v)
    sagt(r.returncode == 0, 'Report laeuft ohne Arbeitseinheiten-Ordner')
    sagt('ID-Praefix' not in r.stdout, 'Ticket-Kategorie verschwindet aus dem Report')
    r = lauf(v, '--summary')
    sagt('ID-Praefix' not in r.stdout, 'Ticket-Kategorie verschwindet aus der Summary')


def test_bootstrap(tmp):
    """Die vier Zustaende des brain-setup-Zeigers (Kit-Umbau-Pfad)."""
    print('\n[5] Bootstrap-Zustaende von skills-check')

    def brain_setup_meldungen(v):
        return [l for l in skills_lauf(v).stdout.splitlines() if 'brain-setup' in l]

    v = os.path.join(tmp, 'bs_a')
    os.makedirs(v)
    kit_kopieren(v, mit_setup_prompt=True)
    sagt(not brain_setup_meldungen(v), 'Setup steht aus: Zeiger gilt als richtig, keine Meldung')

    v = os.path.join(tmp, 'bs_b')
    os.makedirs(v)
    kit_kopieren(v)
    shutil.copy(os.path.join(REPO, 'SETUP-PROMPT.md'), os.path.join(v, 'SETUP-PROMPT-erledigt.md'))
    sagt(any('selbst entfernen' in m for m in brain_setup_meldungen(v)),
         'Setup gelaufen, Zeiger vergessen: wird gemeldet')

    v = os.path.join(tmp, 'bs_c')
    os.makedirs(v)
    kit_kopieren(v)
    sagt(any('ins Leere' in m for m in brain_setup_meldungen(v)),
         'Zeiger ohne Quelle: wird gemeldet')

    v = os.path.join(tmp, 'bs_d')
    os.makedirs(v)
    kit_kopieren(v, mit_bootstrap=False)
    shutil.copy(os.path.join(REPO, 'SETUP-PROMPT.md'), os.path.join(v, 'SETUP-PROMPT-erledigt.md'))
    sagt(not brain_setup_meldungen(v), 'sauber aufgeraeumt: keine Meldung')


def test_repo_fall(tmp):
    """Vault als Unterordner eines Anwendungs-Repos: Zeiger und AGENTS.md liegen oben."""
    print('\n[6] Vault im Anwendungs-Repo (Zeiger im Repo-Root)')
    repo = os.path.join(tmp, 'anwendung')
    v = os.path.join(repo, 'projektwissen')
    os.makedirs(v)
    kit_kopieren(v, mit_bootstrap=False)
    # Zeiger und Kontextdatei eine Ebene hoeher schieben, wie im README beschrieben
    shutil.move(os.path.join(v, '.claude', 'skills'), os.path.join(repo, '.claude_tmp'))
    os.makedirs(os.path.join(repo, '.claude'), exist_ok=True)
    shutil.move(os.path.join(repo, '.claude_tmp'), os.path.join(repo, '.claude', 'skills'))
    shutil.copy(os.path.join(v, 'AGENTS.md'), os.path.join(repo, 'AGENTS.md'))
    # ein projekteigener Skill, der nichts mit dem Vault zu tun hat
    w(repo, '.claude/skills/deploy/SKILL.md',
      "---\nname: deploy\ndescription: rollt die Anwendung aus\n---\n\nEigener Skill des Projekts.\n")

    r = skills_lauf(v)
    sagt(r.returncode == 0, 'skills-check laeuft im Repo-Fall')
    sagt('kein Zeiger' not in r.stdout,
         'findet die Zeiger im Repo-Root (sonst Dauer-Fehlalarm im Hook)')
    sagt('deploy' not in r.stdout,
         'meldet den projekteigenen Skill nicht als verwaisten Zeiger')
    sagt('Kein Drift' in r.stdout, 'kein Drift im Repo-Fall')


def test_kit_selbst():
    """Das Kit im Auslieferungszustand muss sauber sein."""
    print('\n[7] Kit im Auslieferungszustand')
    r = starte(REPO, 'brain-check.py', '--summary')
    sagt(r.returncode == 0, 'brain-check laeuft')
    zahlen = re.findall(r':\s+(\d+)\s*$', r.stdout, re.M)
    sagt(bool(zahlen) and all(z == '0' for z in zahlen),
         'alle Kategorien im Kit sind auf null')
    r = starte(REPO, 'skills-check.py')
    sagt('Kein Drift' in r.stdout, 'kein Skill-Drift im Kit')


def main():
    tmp = tempfile.mkdtemp(prefix='brain-kit-tests-')
    print('Testlauf, Fixtures unter: {0}'.format(tmp))
    try:
        test_alle_kategorien(tmp)
        test_robust(tmp)
        test_konsolen_kodierung(tmp)
        test_ohne_tickets(tmp)
        test_bootstrap(tmp)
        test_repo_fall(tmp)
        test_kit_selbst()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print('\n' + '=' * 60)
    if fehler:
        print('{0} von {1} Pruefungen FEHLGESCHLAGEN:'.format(len(fehler), len(gelaufen)))
        for f in fehler:
            print('  - {0}'.format(f))
        sys.exit(1)
    print('Alle {0} Pruefungen bestanden.'.format(len(gelaufen)))


if __name__ == '__main__':
    main()
