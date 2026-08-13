# Agent-Einstiegspunkt für [DEIN NAME]s Second Brain

> **TEMPLATE, wird beim Setup ausgefüllt.** Diese Datei ist der erste Kontakt für jede
> AI/jedes Tool, das den Vault öffnet. Nach dem Setup-Interview (`SETUP-PROMPT.md`) ersetzt
> die AI die Platzhalter unten durch dein echtes Setup und löscht diesen Hinweis-Block.

> Diese Datei ist für dich als Agent (egal welche AI/welches Tool) gedacht. Token-schlanke
> Navigation, damit nicht bei jeder Session der ganze Vault gelesen werden muss.

## Hard-Facts (Cheat-Sheet)

> Häufig gebrauchte, stabile Fakten (keine Versionsnummern, die ändern sich zu oft), damit
> sie nicht bei jeder Session neu zusammengesucht werden müssen. Füllt sich mit der Zeit,
> am Anfang leer, das ist normal.

- [Platzhalter, z.B. Tool-/Repo-Übersicht, feste Abkürzungen, wiederkehrende Referenzwerte]

## So findest du, was du brauchst

**Lies NICHT zuerst `index.md`**, falls hier Obsidian-Dataview-Queries drinstehen. Die
füllen sich nur im Obsidian-Rendering, für dich als Agent steht da nur Query-Code statt
Daten. Nutze stattdessen direkt deine Such-Werkzeuge:

1. **Glob** auf den passenden Ordner mit Stichwort (z.B. `Wissen/*Stichwort*.md`).
2. **Grep** nach Inhalt, wenn das Stichwort nicht im Dateinamen steht.
3. **Frontmatter-Tags** greppen (`tags: [...]`, `themengebiet:`), wenn thematisch gesucht wird.

Erst danach gezielt mit Read in die gefundene Notiz rein. Ein paar hundert Tokens für
Glob/Grep plus die eine Notiz, statt tausende für einen Volltext-Sweep.

## Wo liegt was

> **Trennung Evergreen-Wissen vs. laufender Stand, die wichtigste Regel, siehe
> [ARCHITECTURE.md](./ARCHITECTURE.md#2-evergreen-wissen-vs-laufender-stand-die-wichtigste-trennung).**
> Wiederverwendbares Wissen gehört NICHT in eine Status-Notiz vergraben, sondern in einen
> eigenen Wissens-Ordner. Aktueller Stand und offene Punkte gehören in eine lebende
> Projekt-/Bereichs-Notiz, nicht ins Wissen.

> **Zweite Frage vor jedem Schreiben: schlägt die AI das später nach, oder muss es immer
> gelten?** Nur Nachschlagbares gehört in den Vault. Regeln, die in jeder Session gelten
> (Coding-Standards, Sprachvorgaben), gehören hierher in `AGENTS.md`, sonst werden sie
> übersehen. Siehe
> [ARCHITECTURE.md](./ARCHITECTURE.md#12-pull-wissen-ja-push-wissen-nein).

- **`[ORDNERNAME z.B. Wissen]/`**: atomare Konzept-/Referenz-Notizen, flach. Frontmatter mit
  `tags`, `themengebiet` und **`type`** (Konzept | Referenz | Vorgehen, siehe
  [ARCHITECTURE.md](./ARCHITECTURE.md#3-das-type-feld-lernstoff-vs-nachschlagewissen-vs-ablauf)).
- **`[ORDNERNAME z.B. Tickets/Vorgaenge]/`** *(optional, falls im Setup gewählt)*: pro
  abgeschlossener Arbeitseinheit eine Notiz mit Problem, Lösung und Lessons Learned. Filename
  sprechend genug für Glob.
- **`MOCs/`**: eine kuratierte Landkarte pro Themengebiet, gruppiert die Wissens-Notizen.
  Bester Einstieg in ein Themengebiet, weil lesbar, anders als automatisch generierte
  Listen. Frontmatter `tags: [moc]`.
- **`Personen/`** *(optional)*: eine Notiz pro Person, mit der regelmäßig zusammengearbeitet
  wird. Datenschutz beachten (siehe `.agents/rules/frontmatter.md`).
- **`Projekte/`** *(optional)*: laufender Stand größerer, andauernder Zusammenhänge.
- **`Meetings/`** *(optional)*: nur wenn der Gesprächsverlauf selbst dauerhaft
  nachvollziehbar bleiben muss; sonst wird die dauerhafte Erkenntnis direkt in die passende
  Themen-Notiz destilliert (kein Pflicht-Log pro Termin).
- **`Vorlagen/`**: Templates für neue Notizen.
- **`Lernen/`** *(optional)*: Spaced-Repetition-Lernstand, falls aktiv gelernt wird.
- **`.agents/skills/<slug>/SKILL.md`**: ein Ordner pro Skill/Routine, toolübergreifend
  lesbar (nicht nur für Claude Code).
- **`.agents/knowledge/`**: persistenter Referenz-Kontext ohne Ablauf-Charakter (z.B. ein
  Schreibstil-Profil).
- **`.agents/rules/`**: die Schreibkonventionen, pro Bereich eine Datei (Übersicht im
  Abschnitt "Konventionen beim Schreiben" unten).
- **`Skripte/`**: Sammel-Routinen, v.a. `brain-check.py` (Vault-Gesundheitscheck).
- **`Ressourcen/`** *(optional)*: Materialien, die keinem anderen Ordner zugehören.

## Wann welche Datei, Auslöse-Phrasen

> Sagt die Person eine dieser Phrasen, ist das das Signal, die genannte Datei zu lesen und
> ihr Schema zu befolgen, ohne Rückfrage. Diese Tabelle wird beim Setup mit den tatsächlich
> gewählten Skills gefüllt; unten stehen nur die Kern-Skills, die praktisch immer dabei sind.

> **Vollständig halten, nicht kürzen.** Tools mit eigener Skill-Mechanik (Claude Code) lesen
> die Auslöser aus dem Skill-Frontmatter; für alle anderen ist diese Tabelle die **einzige**
> Quelle. Fehlt hier eine Phrase, ist der Skill für sie schlicht nicht auslösbar. Die Liste
> muss deshalb mit den `**Auslöser:**`-Kopfzeilen in `.agents/skills/*/SKILL.md`
> übereinstimmen. Bei jeder Änderung beide Seiten anfassen.

| Aufgabe | Reflex |
|---------|--------|
| Chat abschließen, Inhalt sichern: **"brain input" / "ab ins brain" / "ins brain" / "alles ins brain" / "Chat abschließen"** | `.agents/skills/brain-input/SKILL.md` lesen und Schema befolgen |
| Etwas gezielt merken: **"merk dir das" / "merk dir" / "notier dir das" / "das solltest du dir merken" / "festhalten"** | `.agents/skills/merk-dir-das/SKILL.md` lesen und Schema befolgen |
| Tägliche/periodische Bereinigung: **"Brain bereinigen" / "tägliche Bereinigung" / "Brain-Note prüfen"** | `.agents/skills/brain-bereinigen/SKILL.md` lesen und Schema befolgen |
| Vault-Gesundheitscheck: **"Brain optimieren" / "Vault-Check" / "Brain aufräumen" / "großer Brain-Review" / "ist mein Brain noch effektiv"** | `.agents/skills/brain-optimieren/SKILL.md` lesen und Schema befolgen |
| *(optional)* Lernen/Karteikarten: **"Lernen" / "Karteikarten" / "frag mich ab" / "Quiz" / "Lernrunde"** | `.agents/skills/lernen/SKILL.md` lesen und Schema befolgen |
| *(optional)* Text in eigenem Stil: **"formulier mir ..." / "schreib mir eine Mail/Nachricht an ..." / "wie sag ich das ..." / "bring das in meinen Stil" / "klingt das zu nach AI" / "Schreibstil kalibrieren"** | `.agents/skills/formulieren/SKILL.md` lesen und Schema befolgen |
| *[weitere eigene Skills hier eintragen, sobald angelegt]* | |

## Konventionen beim Schreiben

Nur beim Anlegen oder Editieren von Notizen laden, nicht bei jedem Session-Start nötig. Die
Regeln liegen pro Bereich aufgeteilt unter `.agents/rules/`, damit nur der gerade relevante
Teil gelesen wird statt der ganzen Sammlung:

| Datei | Deckt ab |
|---|---|
| `.agents/rules/grundhaltung.md` | Wer schreibt, Umgang mit Abweichungen, Context-Engineering-Maßstab |
| `.agents/rules/frontmatter.md` | Pflichtfelder je Notiz, `sichtbarkeit`-Klassifizierung *(optional)* |
| `.agents/rules/links.md` | Markdown-Links, Kontext-Halbsatz, `## Verwandt`-Dichte |
| `.agents/rules/ablage.md` | Wo Todos/Status hingehören, MOC-vs-Notiz-Duplikate |
| `.agents/rules/karteikarten.md` | Aufnahmekriterium und Form für `Lernen/Karten.md` *(optional, nur falls Lernen aktiv)* |
| `.agents/rules/sprache-und-dateinamen.md` | Sprache im Body, ASCII-Filenames, Tastatur-Typografie |
| `.agents/rules/team.md` | Herkunfts-/Vertrauens-Felder, Multi-Writer-Regeln, Glossar *(optional, nur im Team-Vault)* |
| `.agents/rules/arbeitsweise.md` | Skript statt Rohdaten-Durchlesen bei Sammelaufgaben |
| `.agents/rules/checkliste.md` | Schritt-für-Schritt beim Anlegen einer neuen Notiz |

**Bei Konflikt gilt diese Datei (AGENTS.md).** Steht eine Regel hier und in einer
`.agents/rules/`-Datei unterschiedlich, ist das ein Drift-Bug: die Regel gehört an EINEN Ort
(harte Schreib-Regeln nach `.agents/rules/`, Navigation/Ablage hierher), die Dopplung wird
aufgelöst statt beide Fassungen zu pflegen.

## Themen-Tags & `themengebiet`

> Liste der bislang vergebenen `themengebiet`-Werte und Tags, wächst mit dem Vault. Bei
> Unsicherheit: `Grep: pattern="^themengebiet:" path="Wissen/"` zeigt alle bisher genutzten
> Werte.

- [Platzhalter, z.B. `technik`, `prozess`, `org`, `privat` ... je nach Themenfeldern der Person]

---

Kit-Version: [wird beim Setup eingetragen, siehe CHANGELOG.md im Kit]
