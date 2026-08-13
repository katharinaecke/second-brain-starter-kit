#!/usr/bin/env python3
# Brain-Check: stumpfer Vault-Sweep fuer die Brain-Pflege (Routine "Brain optimieren").
# Findet mechanisch, was sich automatisch finden laesst; das URTEIL (fixen, loeschen,
# umbenennen) macht die AI anhand des Reports - siehe .agents/skills/brain-optimieren/SKILL.md.
#
# Portabel: reines Python 3 ohne Fremdpakete, laeuft ueberall (Windows/macOS/Linux, auch
# in Sandbox-Umgebungen ohne PowerShell). Vault-Pfad wird aus dem Skript-Ort abgeleitet,
# nicht hartkodiert.
#
# Modi:
#   (ohne)      vollstaendiger Report (Kategorien + Trefferlisten) - fuer den Skill
#   --summary   nur Zaehlungen pro Kategorie
#   --hook      SessionStart-Hook: Wochenende raus, max 1x/Tag, nudge nur bei harten Punkten
#
# Quellcode bewusst ASCII, Vault-Inhalt mit UTF-8 gelesen.
#
# Link-Konvention: Standard-Markdown-Links `[Text](</Ordner/Datei.md>)` statt
# Obsidian-Wikilinks (siehe .agents/rules/links.md). Pfade sind bundle-relativ (fuehrender "/"),
# meist in spitze Klammern gewrappt (Leerzeichen in Dateinamen moeglich).
#
# ANPASSEN: die Ordnernamen unten sind Vorgaben aus dem Starter-Kit, KEINE existierenden
# Ordner - das Kit liefert bewusst keine Vault-Ordner mit, die entstehen erst im Setup
# (siehe SETUP-PROMPT.md). Vor dem ersten echten Lauf also auf die tatsaechlich gewaehlten
# Namen setzen. Der Ticket-Naming-Check geht zusaetzlich von einer ID-Praefix-Konvention
# aus (z.B. "AB-42_Titel.md"); ohne solche Arbeitseinheiten TICKET_FOLDER = None setzen.

import os
import re
import sys
import json
import importlib.util
from datetime import date, datetime

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def skill_drift():
    """Skill-Drift (SSOT vs. Zeiger vs. AGENTS.md) aus skills-check.py.

    Bewusst hier eingehaengt, damit der Waechter im taeglichen Lauf mitkommt, statt als
    Skript zu existieren, das nie jemand aufruft. Der Dateiname traegt einen Bindestrich und
    ist damit nicht direkt importierbar - daher ueber importlib. Fehlt die Datei (Setup ganz
    ohne Skills), laeuft der Rest unveraendert weiter.
    """
    path = os.path.join(VAULT, 'Skripte', 'skills-check.py')
    if not os.path.exists(path):
        return []
    try:
        spec = importlib.util.spec_from_file_location('skills_check', path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.drift_report()
    except Exception as e:
        return ['skills-check.py laeuft nicht: {0}'.format(e)]

# ANPASSEN je nach gewaehlter Ordnerstruktur (siehe SETUP-PROMPT.md):
TICKET_FOLDER = 'Tickets/'          # Ordner fuer abgeschlossene Arbeitseinheiten, oder None
TICKET_NAME_RE = re.compile(r'^[A-Z][A-Z0-9]*-\d+_')
WISSEN_FOLDER = 'Wissen/'
SICHTBARKEIT_SCOPE = ('Wissen/', 'Tickets/', 'Personen/', 'Projekte/', 'Meetings/', 'Ressourcen/')


def read_files():
    """Alle .md einlesen. Nicht-UTF-8-Dateien brechen den Lauf NICHT ab.

    Eine einzige falsch kodierte Datei (z.B. aus einem alten Windows-Editor in CP1252)
    wuerde sonst hier abstuerzen, bevor auch nur ein Check laeuft - und mit ihr der
    SessionStart-Hook, bei jedem Start. Deshalb wird ersatzweise gelesen und die Datei
    stattdessen als eigener Befund gemeldet: Sie ist ein echtes Problem (Obsidian und Git
    zeigen sie fehlerhaft an), aber eins, das man sehen und beheben koennen muss, statt
    dass es das ganze Werkzeug lahmlegt.
    """
    files = []
    attachments = []
    for root, dirs, fs in os.walk(VAULT):
        dirs[:] = [d for d in dirs if d != '.obsidian' and d != '.git']
        for f in fs:
            if f.endswith('.md'):
                files.append(os.path.join(root, f))
            elif not f.startswith('.'):
                attachments.append(os.path.join(root, f))
    content = {}
    kaputt = []  # Liste von (pfad, grund)
    for f in files:
        try:
            with open(f, encoding='utf-8') as fh:
                content[f] = fh.read()
        except UnicodeDecodeError:
            with open(f, encoding='utf-8', errors='replace') as fh:
                content[f] = fh.read()
            kaputt.append((f, 'kein gueltiges UTF-8, ersatzweise gelesen'))
        except OSError as e:
            content[f] = ''
            kaputt.append((f, 'nicht lesbar: {0}'.format(e)))
    return files, content, attachments, kaputt


def rel(full):
    return full[len(VAULT):].lstrip(os.sep).replace(os.sep, '/')


def frontmatter_wert(text, feld):
    """Wert eines Frontmatter-Feldes, oder None wenn das Feld fehlt oder leer ist.

    Bewusst nicht `^feld:\\s*(\\S+)`: `\\s*` laeuft ueber den Zeilenumbruch und liest bei
    einem LEEREN Feld den ersten Token der naechsten Zeile als Wert ("---", "tags:"). Und
    ein YAML-Kommentar dahinter - genau so stehen die Felder in Vorlagen/, z.B.
    `sichtbarkeit:   # optional, siehe ...` - wuerde als Wert "#" durchgehen. Beides macht
    aus einer UNklassifizierten Notiz eine klassifizierte und dreht damit das
    Fail-closed-Prinzip (ARCHITECTURE.md#8) genau um.
    """
    m = re.search(r'(?m)^' + re.escape(feld) + r':[ \t]*(.*)$', text)
    if not m:
        return None
    return m.group(1).split('#')[0].strip() or None


# Standard-Markdown-Link mit bundle-relativem Pfad, in spitzen Klammern:
# [Text](</Ordner/Datei.md>). Group 1 = sichtbarer Text, Group 2 = Pfad ohne fuehrenden "/".
LINK_RE = re.compile(r'\[([^\]]*)\]\(<\/([^>]+)>\)')
LOGLINE_RE = re.compile(r'(?m)^- \*\*\d{4}-\d{2}-\d{2}.*$')
VERWANDT_RE = re.compile(r'(?s)##\s+Verwandt\b.*?(?=\n##\s|\Z)')
# Meta-Dokumente: schreiben UEBER die Konventionen und enthalten daher legitim backtickte
# Platzhalter-Beispiele (kein echter Graph-Link gemeint). Sie sind zusaetzlich von der
# Groessen-Pruefung ausgenommen - ein Nachschlagewerk darf lang sein.
# SETUP-PROMPT-erledigt.md gehoert mit dazu: Wer das Kit im eigenen Ordner umbaut, behaelt
# den Fragebogen unter diesem Namen. Ohne den Eintrag meldet der Check ihn ab dann bei jedem
# Lauf als "grosse Notiz" - ein Dauer-Treffer an einer Datei, die niemand kuerzen wird.
META_DOCS = ('AGENTS.md', 'index.md', 'ARCHITECTURE.md', 'README.md', 'SETUP-PROMPT.md',
             'SETUP-PROMPT-erledigt.md', 'CHANGELOG.md', 'MIGRATION.md',
             '.agents/rules/links.md', '.agents/skills/brain-optimieren/SKILL.md')
# Dauer-Treffer, die den taeglichen Hook nicht mehr nudgen sollen (im vollen Report aber
# weiter sichtbar bleiben). Leer im Starter-Kit - trag hier Pfade ein, sobald du bewusst
# einen Backtick-Platzhalter dauerhaft stehen lassen willst.
HOOK_IGNORE_BACKTICK = ()

# Wie oft der SessionStart-Hook sich melden darf.
#   'taeglich'  (Default) hoechstens ein Nudge pro Werktag, Wochenende bleibt still
#   'werktags'  jede Session an Werktagen, Wochenende bleibt still
#   'immer'     jede Session, auch am Wochenende
# Der Default ist bewusst gedaempft: Der Check meldet dieselben Punkte, bis sie behoben sind.
# Ein Hinweis, den man dreimal taeglich wegklickt, wird ab Woche zwei nicht mehr gelesen -
# und dann faellt auch der eine auf, der wirklich wichtig war. Wer den Vault stark bearbeitet
# und sofortiges Feedback will, stellt hier um.
HOOK_FREQUENZ = 'taeglich'

# Dateien, die per Bauart nicht im Wissens-Graph haengen: Templates, Konventionsdateien und
# Skill-Anleitungen. Ohne diese Ausnahme meldet der allererste Lauf in einem frischen Vault
# ein Dutzend "isolierte Notizen", die keine sind - und ein Report, dessen erste Haelfte
# Fehlalarm ist, wird ab dem zweiten Mal nicht mehr gelesen.
# Der Kartenstapel gehoert mit dazu: Er verlinkt zwar Herkunfts-Notizen, ist aber bei einem
# frischen Vault leer und damit dauerhaft "isoliert" - ein Treffer, den niemand beheben kann,
# solange noch keine Karten existieren.
ORPHAN_EXEMPT_PREFIXES = ('Vorlagen/', '.agents/', '.claude/', 'Lernen/')

# Kontextgroessen-Gate. Codex CLI kappt die Summe aller geladenen Kontextdateien bei 32 KiB
# (PROJECT_DOC_MAX_BYTES) - OHNE Warnung, ohne Log. Abgeschnitten wird das ENDE, also genau
# die Regeln, die unten in der Datei stehen. Deshalb ein Budget mit Sicherheitsabstand, das
# meldet, BEVOR still gekuerzt wird. Das Budget wird nicht angehoben, um Wachstum zu
# verstecken - stattdessen Inhalt in eine eigene Notiz auslagern und von hier aus verlinken.
CONTEXT_FILES = ('AGENTS.md', 'CLAUDE.md')
CONTEXT_HARD_LIMIT = 32768
CONTEXT_BUDGET = 30720  # 30 KiB, laesst ~2 KiB Puffer bis zur stillen Truncation


def analyze(files, content, attachments=(), encoding_kaputt=()):
    by_path = {}
    by_path_exact = set()
    for f in list(files) + list(attachments):
        by_path[rel(f).lower()] = f
        by_path_exact.add(rel(f))

    def resolve(path_part):
        target = path_part.split('#')[0].strip()
        if target == '':
            return None
        return by_path.get(target.lower())

    r = {
        'broken': [], 'backtick': [], 'orphans': [], 'no_frontmatter': [],
        'no_verwandt': [], 'not_in_moc': [], 'missing_backlinks': [],
        'big': [], 'ticket_naming': [], 'non_ascii': [], 'long_log': [],
        'no_sichtbarkeit': [], 'sichtbarkeit_counts': {}, 'case_mismatch': [],
        'skill_drift': skill_drift(), 'context_size': [], 'context_total': 0,
        'stale': [],
        'encoding': ['{0}  ({1})'.format(rel(f), grund) for f, grund in encoding_kaputt],
    }

    total = 0
    for name in CONTEXT_FILES:
        p = os.path.join(VAULT, name)
        if os.path.exists(p):
            total += os.path.getsize(p)
    r['context_total'] = total
    if total > CONTEXT_BUDGET:
        r['context_size'].append(
            "{0} zusammen: {1} B ({2:.1f} KiB) - ueber Budget {3} B. Ab {4} B kappt Codex CLI "
            "still das Ende. Inhalt auslagern, Budget NICHT anheben.".format(
                '+'.join(CONTEXT_FILES), total, total / 1024.0,
                CONTEXT_BUDGET, CONTEXT_HARD_LIMIT))

    out_deg = {f: set() for f in files}
    in_deg = {f: set() for f in files}

    for f in files:
        text = content[f]
        rl = rel(f)

        has_backtick_link = False
        for m in LINK_RE.finditer(text):
            start, end = m.span()
            if (start > 0 and text[start - 1] == '`') or (end < len(text) and text[end] == '`'):
                has_backtick_link = True
                break
        if has_backtick_link and rl not in META_DOCS:
            r['backtick'].append(rl)

        link_text = re.sub(r'```.*?```', '', text, flags=re.S)
        link_text = re.sub(r'`[^`]*`', '', link_text)
        for m in LINK_RE.finditer(link_text):
            tgt = m.group(2).split('#')[0].strip()
            if tgt == '':
                continue
            res = resolve(tgt)
            if res is None:
                if not rl.startswith('Vorlagen/'):
                    r['broken'].append("{0}  ->  {1}".format(rl, tgt))
            else:
                # Auf Windows/macOS loest ein falsch geschriebener Pfad auf, auf Linux nicht.
                # Ohne diesen Check meldet der Sweep so einen Link als in Ordnung - und er
                # bricht erst, wenn der Vault auf einem case-sensitiven System landet.
                if tgt not in by_path_exact and not rl.startswith('Vorlagen/'):
                    r['case_mismatch'].append("{0}  ->  {1}  (heisst wirklich: {2})".format(
                        rl, tgt, rel(res)))
            if res is not None and res in in_deg:  # nur .md zaehlt im Graph, Attachments nicht
                out_deg[f].add(res)
                in_deg[res].add(f)

    for f in files:
        rl = rel(f)
        text = content[f]
        name = os.path.basename(f)
        size = os.path.getsize(f)

        if re.search(r'[^\x00-\x7F]', name):
            r['non_ascii'].append(rl)

        if (not re.match(r'^(index|CLAUDE|AGENTS|ARCHITECTURE|README|TODO'
                         r'|SETUP-PROMPT|SETUP-PROMPT-erledigt|CHANGELOG|MIGRATION)\.md$', rl)
                and not any(rl.startswith(p) for p in ORPHAN_EXEMPT_PREFIXES)):
            deg = len(out_deg[f]) + len(in_deg[f])
            if deg < 2:
                r['orphans'].append("{0}  ({1} Verknuepfungen)".format(rl, deg))

        # Meta-Dokumente sind absichtlich lang (Nachschlagewerk, nicht Notiz) und werden nie
        # gesplittet - sie hier zu melden erzeugt einen Dauer-Treffer, den niemand abarbeitet.
        if size > 9000 and rl not in META_DOCS:
            r['big'].append("{0}  ({1} KB)".format(rl, round(size / 1024, 1)))

        # Archiv-Sammeldateien (<Thema>-Archiv.md, siehe .agents/rules/ablage.md) duerfen
        # lange Eintraege haben - das ist dort der Zweck, kein Fehler.
        if not rl.endswith('-Archiv.md'):
            for m in LOGLINE_RE.finditer(text):
                if len(m.group(0)) > 600:
                    r['long_log'].append("{0}  ({1} Zeichen: {2}...)".format(rl, len(m.group(0)), m.group(0)[:60]))

        if TICKET_FOLDER and rl.startswith(TICKET_FOLDER) and not TICKET_NAME_RE.match(name):
            r['ticket_naming'].append(rl)

        # stale_after (Feldname aus dem Open Knowledge Format): ein bewusst gesetztes
        # Ablaufdatum. Anders als ein kaputter Link ist das nie Absicht, sondern ein
        # Versprechen an die eigene Zukunft - deshalb zaehlt es im Hook als harter Punkt.
        # Vorlagen bleiben aussen vor, dort steht der Platzhalter YYYY-MM-DD.
        if not rl.startswith('Vorlagen/'):
            sa = frontmatter_wert(text, 'stale_after')
            if sa:
                try:
                    if date.fromisoformat(sa) <= date.today():
                        r['stale'].append("{0}  (stale_after: {1})".format(rl, sa))
                except ValueError:
                    r['stale'].append("{0}  (stale_after unlesbar: '{1}', erwartet "
                                      "YYYY-MM-DD)".format(rl, sa))

        if any(rl.startswith(p) for p in SICHTBARKEIT_SCOPE):
            val = frontmatter_wert(text, 'sichtbarkeit')
            if val:
                r['sichtbarkeit_counts'][val] = r['sichtbarkeit_counts'].get(val, 0) + 1
            else:
                r['no_sichtbarkeit'].append(rl)

        if rl.startswith(WISSEN_FOLDER):
            # Auf den WERT pruefen, nicht auf die blosse Zeile: eine frisch aus der Vorlage
            # kopierte Notiz hat `themengebiet:` leer stehen, und genau die soll der Check
            # melden.
            if not frontmatter_wert(text, 'themengebiet') or not frontmatter_wert(text, 'tags'):
                r['no_frontmatter'].append(rl)
            if not re.search(r'(?m)^##\s+Verwandt', text):
                r['no_verwandt'].append(rl)

    # MOC-Abdeckung: Wissen-Notizen, die in keiner MOC und nicht im Index vorkommen
    moc_text = ''
    for f in files:
        rl = rel(f)
        if rl.startswith('MOCs/') or rl == 'index.md':
            moc_text += '\n' + content[f]
    moc_targets = set()
    for m in LINK_RE.finditer(moc_text):
        tgt = m.group(2).split('#')[0].strip()
        base = os.path.splitext(tgt.split('/')[-1])[0]
        moc_targets.add(base.lower())
    for f in files:
        if rel(f).startswith(WISSEN_FOLDER):
            if os.path.splitext(os.path.basename(f))[0].lower() not in moc_targets:
                r['not_in_moc'].append(rel(f))

    # Fehlende Ruecklinks (Wissen A -> B in ## Verwandt, B hat keinen Link zu A)
    for f in files:
        rl = rel(f)
        if not rl.startswith(WISSEN_FOLDER):
            continue
        vm = VERWANDT_RE.search(content[f])
        if not vm:
            continue
        for m in LINK_RE.finditer(vm.group(0)):
            tgt = m.group(2).split('#')[0].strip()
            res = resolve(tgt)
            if res is None or not rel(res).startswith(WISSEN_FOLDER):
                continue
            if res not in in_deg[f]:
                r['missing_backlinks'].append("{0}  ->  {1}  (kein Ruecklink in Ziel)".format(rl, tgt))

    return r


def section(title, items, out):
    out.append("## {0} ({1})".format(title, len(items)))
    if not items:
        out.append("  (keine)")
    else:
        for i in items:
            out.append("  - {0}".format(i))
    out.append("")


def full_report(files, r):
    out = []
    out.append("# Brain-Check {0}".format(datetime.now().strftime('%Y-%m-%d %H:%M')))
    out.append("Vault: {0}   |   Notizen: {1}".format(VAULT, len(files)))
    out.append("")
    section("Dateien mit kaputter Kodierung (nicht UTF-8 - Umlaute stehen falsch im Text)", r['encoding'], out)
    section("Kaputte / verdaechtige Links (Tippfehler fixen, bewusste Zukunfts-Notizen lassen)", r['broken'], out)
    section("Links mit falscher Gross-/Kleinschreibung (brechen auf Linux, nicht auf Windows/macOS)", r['case_mismatch'], out)
    section("Backtick-Links (entwerten den Graph-Link - Backticks entfernen)", r['backtick'], out)
    section("Isolierte Notizen (<2 Verknuepfungen - Querlinks ergaenzen)", r['orphans'], out)
    section("Wissen-Notizen ohne vollstaendiges Frontmatter (tags + themengebiet)", r['no_frontmatter'], out)
    section("Wissen-Notizen ohne ## Verwandt", r['no_verwandt'], out)
    section("Wissen-Notizen in keiner MOC und nicht im Index (aus Navigation gefallen)", r['not_in_moc'], out)
    section("Fehlende Ruecklinks (A -> B in Verwandt, B hat keinen Link zu A - bidirektional ergaenzen)", r['missing_backlinks'], out)
    section("Grosse Notizen (>9 KB - splitten/kuerzen pruefen)", r['big'], out)
    if TICKET_FOLDER:
        section("Arbeitseinheiten ohne ID-Praefix im Dateinamen", r['ticket_naming'], out)
    section("Dateinamen mit Nicht-ASCII-Zeichen (falls ASCII-Filenamen-Konvention gilt)", r['non_ascii'], out)
    section("Zu lange Log-Zeilen (>600 Zeichen - gehoert in eine Wissen-Notiz statt ins Log)", r['long_log'], out)
    section("Abgelaufen laut stale_after (Inhalt nachpruefen, Datum neu setzen oder Notiz loeschen)", r['stale'], out)
    section("Skill-Drift (Skripte/skills-check.py zeigt Details)", r['skill_drift'], out)
    section("Kontextdateien ueber Budget (werden von manchen Tools still gekuerzt)", r['context_size'], out)
    out.append("  Kontextdateien: {0} B von {1} B Budget ({2:.0f}%)".format(
        r['context_total'], CONTEXT_BUDGET, 100.0 * r['context_total'] / CONTEXT_BUDGET))
    out.append("")
    section("Ohne sichtbarkeit: klassifiziert (falls Datenschutz-Klassifizierung genutzt wird)", r['no_sichtbarkeit'], out)
    out.append("## sichtbarkeit-Verteilung (klassifizierte Dateien)")
    if not r['sichtbarkeit_counts']:
        out.append("  (noch keine klassifiziert / Feature nicht genutzt)")
    else:
        for k in sorted(r['sichtbarkeit_counts']):
            out.append("  - {0}: {1}".format(k, r['sichtbarkeit_counts'][k]))
    out.append("")
    return "\n".join(out)


def summary(files, r):
    out = []
    out.append("Kaputte Kodierung (kein UTF-8): {0}".format(len(r['encoding'])))
    out.append("Kaputte/verdaechtige Links:    {0}".format(len(r['broken'])))
    out.append("Links mit Case-Fehler:         {0}".format(len(r['case_mismatch'])))
    out.append("Backtick-Links:                {0}".format(len(r['backtick'])))
    out.append("Isolierte Notizen (<2 Links):  {0}".format(len(r['orphans'])))
    out.append("Wissen ohne Frontmatter:       {0}".format(len(r['no_frontmatter'])))
    out.append("Wissen ohne ## Verwandt:       {0}".format(len(r['no_verwandt'])))
    out.append("Wissen in keiner MOC/Index:    {0}".format(len(r['not_in_moc'])))
    out.append("Fehlende Ruecklinks (Verwandt): {0}".format(len(r['missing_backlinks'])))
    out.append("Grosse Notizen (>9 KB):        {0}".format(len(r['big'])))
    if TICKET_FOLDER:
        out.append("Arbeitseinheiten ohne ID-Praefix: {0}".format(len(r['ticket_naming'])))
    out.append("Nicht-ASCII Dateinamen:        {0}".format(len(r['non_ascii'])))
    out.append("Zu lange Log-Zeilen (>600 Z.): {0}".format(len(r['long_log'])))
    out.append("Abgelaufen (stale_after):      {0}".format(len(r['stale'])))
    out.append("Skill-Drift:                   {0}".format(len(r['skill_drift'])))
    out.append("Kontextdateien:                {0} B von {1} B Budget ({2:.0f}%)".format(
        r['context_total'], CONTEXT_BUDGET, 100.0 * r['context_total'] / CONTEXT_BUDGET))
    out.append("Ohne sichtbarkeit: klassifiziert: {0}".format(len(r['no_sichtbarkeit'])))
    for k in sorted(r['sichtbarkeit_counts']):
        out.append("  - {0}: {1}".format(k, r['sichtbarkeit_counts'][k]))
    return "\n".join(out)


def hook(files, r):
    # Wie oft gemeldet werden darf, steuert HOOK_FREQUENZ oben im Skript.
    if HOOK_FREQUENZ != 'immer' and datetime.today().weekday() >= 5:  # 5=Sa, 6=So
        return
    today = date.today().isoformat()
    state = os.path.join(VAULT, '.brain-check-letzte-erinnerung')
    if HOOK_FREQUENZ == 'taeglich' and os.path.exists(state):
        try:
            with open(state, encoding='ascii') as fh:
                if fh.read().strip() == today:
                    return
        except Exception:
            pass
    # Kaputte Links bewusst NICHT im Hard-Count: oft bewusste Zukunfts-Notizen.
    backtick_hard = [x for x in r['backtick'] if x not in HOOK_IGNORE_BACKTICK]
    # Case-Fehler zaehlen mit: anders als ein kaputter Link ist eine falsche
    # Gross-/Kleinschreibung nie Absicht.
    # Kontextdateien ueber Budget zaehlen mit: die Kuerzung passiert still, also merkt es
    # sonst niemand - und sie trifft die Regeln am Dateiende.
    # Kaputte Kodierung zaehlt mit: nie Absicht, und sie macht die Datei in Obsidian und im
    # Diff unbrauchbar, ohne dass es beim Schreiben auffaellt.
    hard = (len(backtick_hard) + len(r['no_frontmatter']) + len(r['not_in_moc'])
            + len(r['case_mismatch']) + len(r['skill_drift']) + len(r['context_size'])
            + len(r['stale']) + len(r['encoding']))
    if hard < 1:
        return
    # Erst hier stempeln, nicht schon oben beim Tagesabgleich: Sonst verbraucht der erste
    # Sessionstart eines ruhigen Morgens die eine Erinnerung des Tages, und was danach
    # entsteht, meldet sich erst morgen. Gestempelt wird, was tatsaechlich genudged hat.
    with open(state, 'w', encoding='ascii') as fh:
        fh.write(today)
    msg = ("Brain-Pflege (Vault-Hook): Der Vault-Check hat {0} Punkt(e) gefunden "
           "(kaputte Kodierung, Backtick-Links, Case-Fehler in Links, fehlendes Frontmatter, Notizen "
           "ausserhalb der MOCs, laut stale_after abgelaufene Inhalte oder zu grosse "
           "Kontextdateien). "
           "Weise kurz und freundlich darauf hin, dass sich mit 'Brain optimieren' ein "
           "Aufraeum-Durchlauf starten laesst. Dezenter Einzeiler, kein Drangsalieren.").format(hard)
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": msg}}))


def main():
    # Der Report gibt Dateinamen aus, und es gibt sogar eine eigene Kategorie fuer solche
    # mit Nicht-ASCII-Zeichen. Auf einer Windows-Konsole in cp1252 wuerde ein Name mit
    # Emoji oder kyrillischen Zeichen die Ausgabe mit einem UnicodeEncodeError abbrechen -
    # ausgerechnet dann, wenn der Check die Datei melden will. Undarstellbare Zeichen
    # werden deshalb ersetzt, statt den ganzen Lauf zu verlieren. Die Konsolen-Kodierung
    # selbst bleibt unangetastet.
    try:
        sys.stdout.reconfigure(errors='replace')
    except Exception:
        pass

    mode = None
    if '--summary' in sys.argv:
        mode = 'summary'
    elif '--hook' in sys.argv:
        mode = 'hook'
    files, content, attachments, encoding_kaputt = read_files()
    r = analyze(files, content, attachments, encoding_kaputt)
    if mode == 'hook':
        hook(files, r)
    elif mode == 'summary':
        print(summary(files, r))
    else:
        print(full_report(files, r))


if __name__ == '__main__':
    main()
