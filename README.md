# Second Brain Starter Kit

Ein Grundgerüst für ein **AI-gepflegtes persönliches Wissens-Vault**: ein Markdown-Ordner
(Obsidian-kompatibel, aber kein Obsidian nötig), den eine AI über Monate hinweg für dich
führt. Sie liest, schreibt, räumt auf und fragt dich daraus ab. Als Tool geht Claude Code,
Claude Desktop oder jeder andere Agent mit Dateizugriff.

Das ist kein fertiges Brain zum Kopieren. Jedes echte Brain ist auf die Person zugeschnitten,
die es benutzt: Ordnernamen, was reinkommt, wie viel Struktur nötig ist. Dieses Kit liefert
das **Betriebssystem darunter**, also die paar Prinzipien und Selbstpflege-Routinen, die
unabhängig vom Beruf funktionieren, plus einen Interview-Prompt, der daraus dein
individuelles Setup ableitet.

## Schnellstart

1. **Klonen oder als ZIP herunterladen.**
2. Mit deinem Agenten-Tool öffnen (Claude Code, o.ä.).
3. **`/brain-setup`** eingeben, das startet das Interview.
   *Kein Claude Code?* Dann **[SETUP-PROMPT.md](./SETUP-PROMPT.md)** öffnen und den
   Prompt-Block von Hand kopieren; inhaltlich ist es derselbe Weg.
4. Fragen beantworten, Ergebnis prüfen, loslegen.

**Dein Brain entsteht in einem eigenen Ordner, nicht hier drin.** Die erste Frage ist, wo es
liegen und wie es heißen soll; das Setup kopiert nur das Gebrauchte dorthin. Dieses Kit bleibt
unverändert, als Vorlage für ein zweites Brain (oder ein Team-Brain) und als Quelle für
spätere Updates.

Das ist kein Ordnungsdetail. Ein Brain, das in diesem Ordner wächst, hängt am GitHub-Remote
dieses Repos. Ein `git pull` überschreibt dir dann deine eigenen Dateien, und wer sich das
Kit als eigenes Repo angelegt hat, hat dort auch Push-Rechte. Ein unbedachtes `git push`
stellt Personen- und Projektnotizen unter deinem Namen ins Netz. Willst du dein Brain
versionieren, dann in einem **eigenen, privaten** Repo.

Das ausführliche Interview stellt rund ein Dutzend Fragen und baut dafür ein Setup, das
wirklich zu dir passt. Wem das für den Anfang zu viel ist: in derselben Datei steht ein
**Kurz-Einstieg mit drei Fragen**, der ein Minimal-Vault anlegt. Der Rest wächst später nach.

Kein Setup-Zwang: wer lieber selbst baut, findet die Prinzipien in
**[ARCHITECTURE.md](./ARCHITECTURE.md)** und kann von dort direkt weiterbauen.

## Was du davon wissen musst

Vier Sätze. Das ist die komplette Bedienoberfläche:

| Du sagst ... | ... und die AI |
|---|---|
| **"ab ins brain"** | geht den Chat durch, zeigt dir, was sie dauerhaft festhalten will, und schreibt es nach deinem OK |
| **"merk dir das"** | hält eine einzelne Sache fest, fragt vorher, wohin |
| **"Brain bereinigen"** | nimmt sich eine Datei vor und prüft mit dir, ob sie noch stimmt, noch gebraucht wird, kürzer geht |
| **"Brain optimieren"** | lässt den mechanischen Check über alles laufen (tote Links, fehlendes Frontmatter, vergessene Notizen) |

Alles Weitere unten ist Maschinenraum. Die Regeln, Vorlagen und Konventionen sind für die
AI geschrieben, nicht für dich. **Du musst sie nicht lesen, um das Brain zu benutzen.**
Genau das ist der Punkt. Systeme dieser Art scheitern fast nie am Sammeln. Sie scheitern an
der Wartung, die irgendwann an einem hängen bleibt. Hier hängt sie nicht an dir.

## Was ist drin

| Datei/Ordner | Zweck |
|---|---|
| `SETUP-PROMPT.md` | Der Interview-Prompt, der aus deinen Antworten dein persönliches Setup baut |
| `ARCHITECTURE.md` | Das Grundmodell dahinter, also warum so und nicht anders, zum Nachlesen und Anpassen |
| `AGENTS.md` | Generischer Agent-Einstiegspunkt (Template, wird beim Setup auf dich zugeschnitten) |
| `CLAUDE.md` | Einzeiler, der `AGENTS.md` importiert. Sieht überflüssig aus, ist der Einstieg für Claude Code und Cowork |
| `.agents/rules/` | Schreib-Konventionen fürs Vault, pro Bereich eine Datei (Templates) |
| `.agents/skills/` | Die Kern-Skills der Brain-Pflege selbst (brain-input, brain-bereinigen, brain-optimieren, merk-dir-das) plus optionale Module (lernen, formulieren) |
| `.claude/skills/` | Dünne Shortcuts auf `.agents/skills/`, damit Claude Code sie als `/skill` anbietet. Dazu `/brain-setup`, der das Setup startet und sich danach selbst entfernt |
| `.claude/settings.json` | Verdrahtet den Vault-Check als SessionStart-Hook (siehe unten) |
| `Vorlagen/` | Note-Templates (Wissensnotiz, Vorgang/Ticket, Quelle, Person, MOC, Kartenstapel, Glossar) |
| `Skripte/brain-check.py` | Mechanischer Vault-Gesundheitscheck (kaputte Links, fehlendes Frontmatter, isolierte Notizen, falsche Kodierung, ...) |
| `Skripte/skills-check.py` | Wächter über die Skills: hält SSOT, Claude-Zeiger und `AGENTS.md` beisammen (läuft im Check mit) |
| `tests/run-tests.py` | Prüft die beiden Skripte oben. Bleibt im Kit, kommt nicht ins Brain mit |
| `CHANGELOG.md` | Was sich je Version geändert hat und warum, markiert danach, ob es bestehende Brains betrifft |
| `MIGRATION.md` | Prompt, um ein schon eingerichtetes Brain auf eine neue Kit-Version nachzuziehen |

**Was hier bewusst *nicht* liegt: die Vault-Ordner selbst.** Kein `Wissen/`, kein `Tickets/`,
kein `Personen/` auf Vorrat. Die legt das Setup an, und nur die, die sich aus deinen
Antworten begründen lassen. Ein Kit, das acht leere Ordner mitliefert, von denen du drei
brauchst, zwingt dich zum Aufräumen, bevor du die erste Notiz geschrieben hast.

## Warum das funktioniert

Den Kern machen drei Entwurfsentscheidungen aus, die sich in der Praxis über Monate und
hunderte Notizen als tragfähig erwiesen haben:

1. **Eine schreibende Instanz.** Den Vault pflegt die AI, nicht du. Sie tut es nach Regeln,
   die in `.agents/rules/` stehen, statt nach Bauchgefühl bei jedem Edit.
2. **Trennung von Wissen und Stand.** Was in 6 Monaten noch wahr ist, ist etwas anderes als
   der aktuelle Stand einer laufenden Sache. Beides im selben Ordner zu vermischen macht
   den Vault mit der Zeit unbrauchbar.
3. **Das Brain pflegt sich selbst.** Vier Skills (brain-input, brain-bereinigen,
   brain-optimieren, merk-dir-das) sind kein Kür-Feature. Sie sind der Grund, warum ein
   AI-Vault nach einem Jahr noch brauchbar ist statt eine Deponie halbwahrer Notizen.

Details, Beispiele und die Begründung dahinter: **[ARCHITECTURE.md](./ARCHITECTURE.md)**.

## Die tägliche Erinnerung

Ein Vault verfällt leise. Man fasst ihn ein paar Wochen nicht an, und danach stimmt die
Hälfte nicht mehr. Deshalb bringt das Kit einen **SessionStart-Hook** mit:
`Skripte/brain-check.py --hook` läuft beim Start einer Claude-Code-Session, prüft den Vault
mechanisch durch und meldet sich **nur dann**, wenn es harte Punkte gibt. Im Default an
Werktagen, höchstens einmal am Tag.

Verdrahtet ist das in [`.claude/settings.json`](./.claude/settings.json). Drei Dinge dazu:

- **Der Python-Befehl muss zu deinem System passen.** In der mitgelieferten Datei steht
  `python3`; unter Windows heißt es oft schlicht `python`. Das Setup-Interview prüft das und
  korrigiert es. Wer von Hand aufsetzt, ändert es selbst. Gebraucht wird **Python 3.7 oder
  neuer**, ohne Fremdpakete; die Skripte laufen unter Windows, macOS und Linux gleich.
- **Wer den Nudge nicht will, löscht die Datei.** Der Rest des Kits funktioniert ohne Hook
  genauso; die Routinen laufen dann rein auf Zuruf.
- **Wie oft er sich meldet, steht als `HOOK_FREQUENZ` oben in `brain-check.py`.** Default ist
  `taeglich` (höchstens einmal pro Werktag), möglich sind auch `werktags` und `immer` für
  eine Meldung in jeder Session. Der Default ist mit Absicht der leiseste: Der Check meldet
  dieselben Punkte, bis sie behoben sind, und ein Hinweis, den man dreimal am Tag wegklickt,
  wird ab Woche zwei nicht mehr gelesen.
- **Er feuert nur in Sessions, die im Brain-Ordner starten.** Wer sein Brain aus anderen
  Projekten heraus benutzt, verschiebt den Eintrag nach `~/.claude/settings.json`, siehe
  [Wo die Skills gelten](#wo-die-skills-gelten).

Der Hook ist das einzige Stück, das von selbst läuft. Ohne ihn funktioniert alles andere
unverändert, auch mit Cursor, Codex oder jedem anderen Agenten mit Dateizugriff. Dafür
liegen die Inhalte in `.agents/`. Du musst dann nur selbst daran denken, ab und zu "Brain
optimieren" zu sagen.

## Wo die Skills gelten

Ein Punkt, der leicht übersehen wird und im Alltag den Unterschied macht: Claude Code lädt
Skills aus `.claude/skills/` **nur für Sessions, die in diesem Ordner starten** (und in
Unterordnern davon). Dein Brain als zusätzlich verbundenes Verzeichnis zählt dafür nicht.

Der typische Moment für "ab ins brain" ist aber das Ende einer Arbeitssession, und die
läuft in deinem Projekt, nicht im Brain. Dort wäre keine der Routinen auslösbar. Zwei Wege:

| Weg | Wirkung |
|---|---|
| **Skills bleiben im Brain** (`.claude/skills/`) | Routinen greifen nur, wenn du Claude Code im Brain-Ordner startest. Reicht, wenn du dein Brain ohnehin in eigenen Sessions pflegst |
| **Zeiger zusätzlich nach `~/.claude/skills/`** | Routinen greifen in *allen* Projekten. Dafür muss im globalen Zeiger der **absolute** Vault-Pfad stehen; der relative zeigt von dort ins Leere |

Beim zweiten Weg gehören zwei Dinge mit nach `~/.claude/settings.json`. Erstens der
Brain-Ordner unter `permissions.additionalDirectories`, sonst darf die AI aus einem fremden
Projekt heraus gar nicht hineinschreiben (alternativ pro Session `/add-dir <pfad>`).
Zweitens der SessionStart-Hook, falls du ihn nutzt. Der läge sonst weiter im Brain und würde
nur dort feuern, also gerade nicht in den Sessions, um die es hier geht. In der globalen
Fassung tritt der **absolute Vault-Pfad** an die Stelle von `${CLAUDE_PROJECT_DIR}`: Die
Variable zeigt dort auf das gerade offene Projekt, der Hook würde im falschen Ordner nach dem
Skript suchen und stillschweigend nichts tun.

Das Setup-Interview fragt nach beidem und richtet es auf Wunsch ein. Von selbst wird
nichts an deiner globalen Konfiguration geändert.

## Mit anderen Tools als Claude Code

Der Inhalt liegt bewusst in `.agents/`, damit jedes Tool mit Dateizugriff ihn lesen kann.
Was sich unterscheidet, ist nur die Frage, wie eine Routine ausgelöst wird.

**Claude Cowork** (Desktop, Web, Mobil) arbeitet mit verbundenen Ordnern statt mit einem
Arbeitsverzeichnis. Verbinde deinen Brain-Ordner einmal, dann liest Cowork ihn in jeder
Session. Zwei Unterschiede zu Claude Code:

- **Skills kommen nicht aus `.claude/skills/` deines Vaults.** Cowork verwaltet seine
  Skills zentral unter *Customize → Skills*. Wer die Routinen dort als `/brain-input` und
  Co. haben will, lädt die Skill-Ordner einmal als ZIP hoch. Ohne das funktionieren die
  Auslöser-Phrasen trotzdem, und genau dafür ist die scheinbar überflüssige `CLAUDE.md` im
  Vault da: Cowork lädt sie beim Verbinden automatisch, sie importiert per `@AGENTS.md` den
  Einstiegspunkt, und dessen Auslöser-Tabelle sagt der AI, welche Datei sie bei welchem Satz
  lesen soll. Deshalb muss `CLAUDE.md` mit ins Brain, auch wenn sie nur eine Zeile hat.
- **Kein SessionStart-Hook.** Die Erinnerung entfällt, `.claude/settings.json` hat dort
  keine Wirkung. "Brain optimieren" musst du selbst sagen.

**Codex CLI, Cursor, Aider und andere** lesen `AGENTS.md` direkt, das ist inzwischen der
verbreitete Standard dafür. Für sie ist die Auslöser-Tabelle darin die **einzige** Quelle,
weil sie von `.agents/skills/` nichts wissen. Genau deshalb hält `Skripte/skills-check.py`
sie mit den Skill-Dateien synchron: Fehlt dort eine Phrase, ist die Routine für diese Tools
stumm, ohne Fehlermeldung.

Bei Codex CLI kommt eine Eigenheit dazu, auf die das Kit vorbereitet ist: Es kappt die Summe
aller geladenen Kontextdateien bei 32 KiB, ohne Warnung, und zwar am Ende. `brain-check.py`
meldet deshalb, sobald `AGENTS.md` plus `CLAUDE.md` zusammen über 30 KiB kommen.

## Sicherung und zweites Gerät

Hier liegt dein Wissen als **lokale Markdown-Dateien**. Das ist die Stärke (kein Anbieter
dazwischen, alles les- und greppbar in dreißig Jahren) und zugleich die Verantwortung: **für
Backup und Synchronisation sorgt niemand außer dir.** Ein Second Brain, das man ein Jahr lang
füllt und dann mit einer kaputten Festplatte verliert, ist schlimmer als keins. Man hat sich
darauf verlassen.

Drei Wege, die in der Praxis funktionieren; einer reicht:

| Weg | Taugt für | Preis |
|---|---|---|
| **Privates Git-Repo** (GitHub/GitLab, privat!) | Backup, Versionshistorie und mehrere Geräte | Du musst regelmäßig committen, oder es die AI am Ende jeder Session tun lassen |
| **Cloud-Ordner** (iCloud, Dropbox, OneDrive, Nextcloud) | Backup und Sync ohne Nachdenken | Keine Historie; ein versehentliches Löschen synchronisiert sich mit |
| **Externe Platte, feste Erinnerung** | Backup offline, unabhängig von Anbietern | Kein Sync; nur so gut wie die Disziplin dahinter |

**Wenn Personendaten im Vault stehen** (Kollegen, Kunden, Klienten), ist die Wahl keine reine
Komfortfrage mehr. Ein privates Repo bei einem US-Anbieter oder ein Cloud-Ordner ist etwas
anderes als eine verschlüsselte Platte im Schreibtisch. Die `sichtbarkeit:`-Klassifizierung
(siehe [ARCHITECTURE.md](./ARCHITECTURE.md#8-fail-closed-bei-sensiblem)) hilft dabei nur, wenn
man sie vor dieser Entscheidung gelesen hat, nicht danach.

## Wenn mehrere Leute mitschreiben

Das Interview fragt als Erstes, ob der Vault dir allein gehört oder einem Team. Bei "Team"
ändert sich das Modell an einer Stelle grundlegend: Die Annahme "es gibt genau eine
schreibende Instanz" trägt nicht mehr, und damit auch nicht die Selbstverständlichkeit, dass
jede Notiz gleich vertrauenswürdig ist. Eine Aussage kann von einer Person abgenommen oder
von der AI aus einem Gespräch abgeleitet sein, frisch oder ein Jahr alt.

Deshalb kommen im Team-Fall Felder dazu, die festhalten, wer etwas geschrieben hat, wer es
bestätigt hat und ab wann es nachprüfbedürftig wird. Die Namen dafür sind nicht erfunden,
sie stammen aus dem [Open Knowledge Format](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf),
einem offenen Standard von Google Cloud für genau diese Art von Markdown-Wissensbasis.
Übernommen wird nur, was trägt: OKF selbst verlangt ein einziges Pflichtfeld. Das Vault ist
damit OKF-nah, aber kein konformes Bundle, Details in
[ARCHITECTURE.md](./ARCHITECTURE.md#10-team-variante-wenn-abschnitt-1-nicht-mehr-wörtlich-gilt).

Dazu kommen ein Glossar (Hausbegriffe sind für neue Leute und für die AI die eigentliche
Hürde), Regeln fürs Mitschreiben in `.agents/rules/team.md` und die Frage, wo das Ganze
liegt. Ein Projekt-Vault gehört meist ins Repo des Projekts, das er beschreibt: Dann läuft
Wissen durch dieselben Merge Requests wie der Code und wird mitreviewt. Der Preis ist, dass
jeder mit Repo-Zugriff mitliest, personenbezogene Daten haben dort also nichts zu suchen.

Ein Detail, das im Alltag mehr wiegt, als es klingt: **"Brain" ist nicht überall ein
beliebter Name.** Der Begriff legt nahe, das Ding denke selbst, dabei ist es ein
Wissensspeicher. Das Setup fragt deshalb im Team-Fall nach der Bezeichnung und benutzt
danach durchgängig eure, zum Beispiel "Projektwissen".

Zwei Fragen, die ein Team früh klären sollte und die das Interview deshalb stellt: **Welche
vorhandene Doku steht dazu parallel?** Ein Wissensspeicher, der neben Handbuch, Wiki und
README herläuft, ohne dass jemand sagt, wer wofür zuständig ist, wird zur vierten Quelle,
die auch veraltet. Und: **Wo kommt das erste Wissen her?** Ein Handbuch einzulesen und gegen
den Code zu prüfen bringt in einem Durchgang mehr als Monate an Session-Ernte.

## Wenn das Wissen ins Repo der Anwendung soll

Ein Sonderfall des Team-Vaults, der in der Praxis oft der eigentliche Anlass ist: **das
fachliche Wissen über genau eine Anwendung, versioniert neben ihrem Code**. Also warum das
Abrechnungsmodul so rechnet, was der Hausbegriff im Ticket bedeutet, welche Entscheidung vor
zwei Jahren wie begründet war.
Der Gewinn ist echt: Wissen läuft durch dieselben Merge Requests wie der Code, wird
mitreviewt, und der Diff wird nebenbei zum fachlichen Changelog.

Technisch ist das aber **kein einfaches Hineinkopieren**. Drei Dinge brechen still, wenn man
den Vault als Unterordner (`projektwissen/`) ins Repo legt:

| Was | Warum es bricht | Lösung |
|---|---|---|
| `.claude/settings.json` | Claude Code liest Projekt-Settings nur aus dem **Repo-Root**, nicht aus Unterordnern. Der Hook feuert nie | Hook-Eintrag ins `.claude/settings.json` des Repos, mit dem Pfad `projektwissen/Skripte/brain-check.py` |
| `.claude/skills/` | Kommt ebenfalls nur aus dem Repo-Root. Alle Routinen wären stumm | Zeiger nach `<repo>/.claude/skills/` legen, im Zeiger auf `projektwissen/.agents/skills/<slug>/SKILL.md` verweisen |
| `AGENTS.md` | Das Repo hat meist schon eine, für Coding-Regeln. Zwei Dateien mit demselben Namen und verschiedenem Zweck | Die Wissens-Navigation **nicht** duplizieren: in der Repo-`AGENTS.md` ein Verweis darauf, dass fachliches Wissen unter `projektwissen/` liegt, samt Auslöser-Tabelle. Die zweite `AGENTS.md` im Unterordner bleibt der Vault-Einstieg |

`brain-check.py` selbst funktioniert unverändert, es leitet den Vault-Pfad aus seinem eigenen
Ort ab und sweept damit nur den Unterordner. Was du anpassen musst, ist `CONTEXT_FILES`: Die
Größenprüfung soll die `AGENTS.md` messen, die der Agent tatsächlich lädt, und das ist im
Repo-Fall die im Root.

Der Preis bleibt derselbe wie bei jedem Repo-Vault: **Jeder mit Repo-Zugriff liest mit.**
Personenbezogene Daten, Einschätzungen über Kollegen und Kundendaten haben dort nichts zu
suchen, auch nicht in einem privaten Repo. `.agents/rules/team.md` sagt das, und der
Brain-Input-Skill prüft es beim Schreiben mit.

## Nicht enthalten (bewusst)

Dieses Kit enthält keine Skills, die an ein bestimmtes Berufsfeld, Firmentools (Jira,
bestimmte Deploy-Pipelines) oder eine bestimmte Person gebunden sind. Die im Original
existierenden Beispiele dafür (Ticket-Tracker-Sync, Foto-Kuration, Präsentations-Faktencheck)
zeigen aber ein wiederkehrendes Muster: **eine fachliche Routine bekommt genau dann einen
eigenen Skill, wenn du sie öfter als ein-, zweimal im Monat brauchst.** Baue eigene Skills
nach demselben Muster wie die mitgelieferten: kurzer Shortcut in `.claude/skills/`, der
eigentliche Inhalt als Note in `.agents/skills/<name>/SKILL.md`, damit jedes Tool ihn lesen
kann und nicht nur Claude Code.

Sobald du das tust, beschreibt sich jeder Skill an **drei** Stellen: in seiner Anleitung, im
Claude-Zeiger und in der Auslöser-Tabelle in `AGENTS.md`. Die laufen zuverlässig auseinander,
und der Ausfall ist tückisch. Fehlt eine Phrase in `AGENTS.md`, ist der Skill für Tools ohne
Skill-Mechanik einfach nicht auslösbar, ohne Fehlermeldung. `Skripte/skills-check.py` hält die
drei zusammen und läuft bei jedem `brain-check.py` mit.

## Wenn du die Skripte anpasst

```bash
python tests/run-tests.py
```

Das Setup baut `brain-check.py` aktiv um: Ordnernamen, `TICKET_FOLDER`,
`SICHTBARKEIT_SCOPE`. Genau dabei geht leicht etwas kaputt, und der Ausfall ist wieder der
stille: Ein Check, dessen Bedingung nicht mehr greift, meldet dauerhaft "(keine)" und sieht
damit aus wie ein sauberer Vault.

Der Lauf baut deshalb einen Wegwerf-Vault, in dem **jede** Kategorie genau einmal ausgelöst
wird, und prüft, ob auch jede anschlägt. Dazu die Fälle, die im Alltag wehtun: Dateien, die
kein UTF-8 sind, Dateinamen mit Emoji auf einer Windows-Konsole, ein Vault ohne
Arbeitseinheiten-Ordner, ein Vault im Repo einer Anwendung. Alle Fixtures entstehen im
System-Temp, weder dein Vault noch dieses Repo werden angefasst.

Der Ordner bleibt hier und kommt beim Setup nicht ins Brain mit.

## Updates für ein schon eingerichtetes Brain

Dein Brain entfernt sich vom Kit, sobald es steht: eigene Ordnernamen, gelöschte Skills,
angepasste Konstanten. Ein `git pull` bringt dir hier deshalb nichts, und ein
Migrationsskript könnte gar nicht wissen, wie dein Vault aussieht.

Stattdessen führt [`CHANGELOG.md`](./CHANGELOG.md) pro Version auf, was sich geändert hat und
warum, und markiert jeden Eintrag danach, **ob er bestehende Brains überhaupt betrifft**. Das
meiste tut das nicht: Änderungen am Setup-Interview zum Beispiel sieht nur, wer neu aufsetzt.

Wenn doch, hilft [`MIGRATION.md`](./MIGRATION.md). Das ist wieder ein Prompt, kein Skript: Die
AI liest die Einträge ab deiner Version, sieht sich dein tatsächliches Brain an und schlägt
nur vor, was dort zutrifft, ohne deine Anpassungen zu überschreiben. Damit das funktioniert,
schreibt das Setup die Kit-Version als letzte Zeile in deine `AGENTS.md`.

Pflicht ist nichts davon. Relevant sind vor allem Einträge unter "Behoben", denn dort liegt in
deinem Vault eine Kopie eines Skripts, das denselben Fehler noch hat.

## Lizenz / Nutzung

[MIT](./LICENSE): forken, anpassen, weitergeben, auch kommerziell nutzen; einzige Bedingung
ist der Copyright-Hinweis. Es ist ein Startpunkt, keine fertige Lösung. Der Sinn des
Interviews in `SETUP-PROMPT.md` ist gerade, dass am Ende **dein** Brain dabei rauskommt und
keine Kopie von jemand anderem.

## Keine Gewähr

Dieses Kit kommt ohne jede Zusicherung, wie in der MIT-Lizenz festgehalten. Drei Punkte, die
zu leicht untergehen, weil hier eine AI mitschreibt:

- **Was in deinem Vault landet, verantwortest du.** Das Setup und die Routinen fragen an
  vielen Stellen nach, bevor sie schreiben, aber sie sind kein Datenschutz-Prüfsystem. Ob
  personenbezogene Daten, Kundeninhalte oder Betriebsgeheimnisse in einen Ordner gehören,
  der womöglich synchronisiert, gesichert oder geteilt wird, entscheidest allein du. Das
  gilt besonders im Team-Fall und im Repo-Fall, wo mitliest, wer Zugriff hat.
- **Für Backup und Wiederherstellung sorgt niemand außer dir.** Siehe
  [Sicherung und zweites Gerät](#sicherung-und-zweites-gerät).
- **Die Skills löschen und überschreiben Dateien.** Das Setup legt Ordner an und entfernt
  Ungebrauchtes, die Bereinigung schlägt Löschungen vor. Beides bestätigst du vorher, aber
  ein Fehlgriff ist ohne Versionskontrolle endgültig. Setz das Ganze auf einem Ordner auf,
  dessen Verlust du verkraften würdest, oder committe früh.

Kurz: Es ist ein Werkzeug zum Selberbauen und Anpassen. Wer es einsetzt, prüft selbst, ob es
zu seiner Situation, seinen Daten und seinen Vorgaben passt.
