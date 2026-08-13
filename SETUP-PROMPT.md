# Setup-Prompt: Second Brain einrichten

Diese Datei ist der eigentliche Startpunkt. Alles hier drunter (der Block im Codefeld) ist
**ein einziger Prompt**. Kopiere ihn komplett und schick ihn deiner AI (Claude Code, Claude
Desktop mit Dateizugriff, Cursor, egal), nachdem du dieses Repo geklont oder als ZIP
heruntergeladen und lokal geöffnet hast.

Der Prompt macht **kein** Copy-Paste einer fremden Struktur. Er lässt sich von dir interviewen
und baut die Ordner, Vorlagen und Skills erst danach, nur die, die zu deinem Alltag passen.
Eine Softwareentwicklerin mit Jira-Tickets braucht andere Ordner als ein Student, eine
Selbstständige oder ein Forschungsteam. Was **nicht** verhandelbar ist: das Grundprinzip
darunter (siehe [ARCHITECTURE.md](./ARCHITECTURE.md)). Ordnerstruktur ist nur die Oberfläche.

**Zu viel für den Anfang?** Ganz unten steht ein
[Kurz-Einstieg mit drei Fragen](#kurz-einstieg-drei-fragen), der legt ein Minimal-Vault an,
mit dem sich sofort arbeiten lässt. Das ausführliche Interview kannst du jederzeit später
nachholen; es ist derselbe Weg, nur gründlicher.

## So gehst du vor

1. Kit klonen oder als ZIP herunterladen.
2. Mit Claude Code (oder deinem Agenten-Tool der Wahl) in diesem Ordner öffnen.
3. **In Claude Code genügt `/brain-setup`.** Der Skill fragt, welcher Weg (ausführlich oder
   kurz), und arbeitet dann den passenden Block dieser Datei ab. Ohne Skill-Mechanik: den
   kompletten Block unten (zwischen den `---`-Linien) als Nachricht schicken.
4. **Erste Frage ist, wo dein Brain entstehen soll und wie es heißt.** Es entsteht in einem
   eigenen Ordner; dieses Kit bleibt Vorlage und wird nicht umgebaut.
5. Die weiteren Fragen beantworten, ehrlich und im eigenen Tempo, es ist kein Test.
6. Die AI kopiert das Gebrauchte in deinen neuen Ordner, schreibt dort dein persönliches
   `AGENTS.md` und `.agents/rules/`, legt nur die passenden Ordner an und behält nur die
   Skills, die du wirklich brauchst. Kein Museum ungenutzter Optionen.
7. Am Ende steht dein Brain im eigenen Ordner, das Kit unverändert daneben. Willst du dein
   Brain versionieren: eigenes, **privates** Repo, nie der Remote des Kits.

---

```
Ich richte gerade mein persönliches "Second Brain" ein, einen Wissens-Vault (Markdown/
Obsidian-kompatibel), den du als AI-Assistentin dauerhaft mitpflegst: du liest ihn zu
Beginn jeder Session, schreibst als einzige Instanz hinein, und hältst ihn nach festen
Konventionen sauber. Dieses Repo ist ein Starter-Kit dafür (second-brain-starter-kit).
Es enthält eine Rohstruktur, Vorlagen und ein paar Kern-Skills, aber noch NICHT auf mich
zugeschnitten.

**Frag mich als Allererstes, wo mein Brain entstehen soll und wie es heißen soll**, also Pfad
und Ordnername. Schlag etwas vor (z.B. einen Nachbarordner des Kits, `MeinBrain`), aber
entscheide nicht für mich. Das Kit selbst bleibt dabei unangetastet: Es ist die Vorlage,
nicht das Ergebnis. Gründe, warum das Brain NICHT im Kit-Ordner entsteht:
- Das Kit hängt am GitHub-Remote des Starter-Kits. Ein Brain, das darin wächst, erbt ihn:
  ein `git pull` überschreibt eigene Dateien, und wer Push-Rechte auf dieses Repo hat,
  veröffentlicht mit einem unbedachten `git push` private Notizen.
- Mein Brain soll heißen, wie ich will, nicht `second-brain-starter-kit`.
- Das Kit bleibt so wiederverwendbar (zweites Brain, Team-Brain) und aktualisierbar.

Nur wenn ich ausdrücklich sage, dass das Kit selbst umgebaut werden soll, ist der Kit-Ordner
das Ziel. Sind in dieser Session weitere Ordner sichtbar, womöglich ein schon eingerichteter
Vault: die sind nie gemeint und werden nicht angefasst. Nenn mir den gewählten Zielpfad
absolut und warte auf mein OK, bevor du etwas schreibst.

Deine Aufgabe jetzt: interview mich mit den Fragen unten, EINE nach der anderen (nicht
alle auf einmal abfragen), und leite aus meinen Antworten ab, welche Ordner, Vorlagen und
Skills aus diesem Kit ich wirklich brauche. Nimm nichts blind aus dem Kit an, jede
Struktur muss sich aus einer meiner Antworten begründen lassen. Wenn eine Frage für mich
offensichtlich nicht zutrifft, überspring sie kurz begründet statt stur durchzufragen.

Lies zuerst ARCHITECTURE.md in diesem Repo komplett. Das ist das Grundmodell (evergreen
vs. Stand-Wissen, das type-Feld, MOCs als Landkarten, die Brain-Pflege-Skills), das bleibt
über alle Antworten hinweg gleich. Nur die Ordnerauswahl, Terminologie und welche
optionalen Skills mitkommen, hängt von mir ab.

## Fragen (eine nach der anderen, kurz halten)

0. **Ist dieses Brain nur für dich allein, oder soll es auch von anderen aktiv
   mitgepflegt/gelesen werden** (Team-Brain)? Bei "nur ich" bleibt alles unten wie
   beschrieben. Bei "Team" kommt nach Frage 8 ein zusätzlicher Block dazu (Multi-Writer,
   Confidence-/Herkunfts-Kennzeichnung). Das Grundmodell in ARCHITECTURE.md#1 ("eine
   schreibende Instanz") gilt dann nicht mehr wörtlich, siehe ARCHITECTURE.md#10.

1. **Was machst du beruflich/hauptsächlich, und in welcher Einheit läuft deine Arbeit?**
   (z.B. Tickets/Issues in einem Tracker, Kundenprojekte, Studienfächer, freie Projekte,
   Forschung, gar keine klare Einheit). Das entscheidet, ob und wie ein Ordner für
   abgeschlossene Arbeitseinheiten aussieht (Name, Frontmatter, z.B. "Tickets" mit
   Jira-ID-Präfix, oder "Auftraege", "Faelle", "Sessions").

1b. **Und gibt es Dinge, die über Wochen oder Monate laufen und deren aktueller Stand sich
   ständig ändert** (ein Projekt, ein Kunde, ein Fach, eine Bewerbungsphase)? Frag das
   getrennt von 1, es ist eine andere Achse: 1 meint *abgeschlossene* Einheiten, die man
   nachschlägt, hier geht es um *laufenden* Stand, der überschrieben wird. Genau diese
   Trennung ist laut ARCHITECTURE.md#2 die wichtigste im ganzen Modell, und sie geht schief,
   wenn nur nach einer der beiden Seiten gefragt wird. Bei "ja" entsteht ein Ordner dafür
   (`Projekte/` oder passender benannt), bei "nein" nicht.

2. **Sammelst du wiederverwendbares Fachwissen, das in 6 Monaten noch stimmt** (Konzepte,
   Patterns, Fakten zu Tools/Domänen)? Falls ja: **willst du dabei aktiv lernen** (dich
   von der AI im Spaced-Repetition-Verfahren abfragen lassen), oder soll es reines
   Nachschlagewissen ohne Lernanspruch sein?

3. **Arbeitest du mit Menschen, über die es sich lohnt, eigene Notizen zu führen**
   (Kollegen, Kunden, Netzwerkkontakte mit Zuständigkeiten/Historie)? Falls ja: nur
   interne Leute oder auch externe Kontakte? Gibt es Datenschutz-Sensibilität
   (Kundendaten, Personendaten), die eine Vertraulichkeits-Klassifizierung pro Notiz
   braucht?

4. **Hast du schon ein Tool für Todos/Erinnerungen** (Trello, Todoist, Reminders, Jira
   selbst, Papier)? Sollen Todos dort bleiben (Vault verweist nur drauf), oder willst du
   Todos direkt im Vault führen? (Die *technische* Verbindung, z.B. ein MCP-Server für
   Trello/Jira, ist Sache deines Agenten-Tools, nicht dieses Vault-Repos. Hier geht es nur
   darum, ob und wie der Vault-Inhalt darauf Bezug nimmt.)

5. **Gibt es feste Termine/Meetings, deren Inhalt langfristig relevant ist** (Weeklys,
   Coachings, Kundengespräche), oder ist das für dich irrelevant/schon anderswo
   dokumentiert?

6. **Schreibst du oft Texte in einem bestimmten eigenen Ton** (Mails, Chat-Nachrichten,
   Tickets, Posts), bei denen dir wichtig ist, dass die AI in DEINER Stimme schreibt statt
   generisch? Falls ja: für wie viele unterschiedliche Kanäle/Empfänger (z.B. Kollege
   locker vs. Kunde förmlich)?

7. **Wie oft willst du mit der AI Bilanz ziehen**: laufend am Ende jeder Session ("was
   davon gehört ins Brain"), nur auf Zuruf, oder in festen Abständen (täglich/wöchentlich)
   für eine Aufräum-Routine?

8. **Welche Sprache soll der Vault-Inhalt haben**, und gibt es Namenskonventionen, die du
   ungern änderst (z.B. Dateinamen ASCII wegen Windows/Git)?

### Nur falls Frage 0 = Team-Brain

9. **Wer schreibt aktiv mit**, nur Menschen über die AI, oder tippen manche auch direkt in
   Dateien? Wie viele Personen etwa?

10. **Braucht ihr eine Kennzeichnung, woher eine Aussage stammt und wie sicher/aktuell sie
    ist** (z.B. "von einer Person bestätigt" gegen "von der AI abgeleitet", Datum der letzten
    Bestätigung)? Ohne das kann eine automatisierte Bereinigung nicht sicher entscheiden, was
    sie anfassen darf, mit dieser Kennzeichnung schon.

11. **Falls ja bei Frage 10: soll die Bereinigung automatisiert/geplant laufen** (nicht nur
    auf Zuruf), gestützt auf genau diese Felder? Das ist die einzige Situation, in der
    automatisierte Bereinigung im Sinne von ARCHITECTURE.md#10 vertretbar ist. Ohne
    Frage-10-Antwort "ja" bleibt Bereinigung getriggert wie im Solo-Fall.

12. **Welche Doku habt ihr schon** (Benutzerhandbuch, Wiki, Readmes, Architekturdoku), und
    was davon steht künftig parallel zu diesem Vault, was soll er irgendwann ersetzen? Das
    ist die Frage, an der geteilte Wissensspeicher am häufigsten scheitern: Ohne Antwort wird
    der Vault die nächste Quelle, die niemand pflegt, weil unklar bleibt, wo eine Aussage
    hingehört. Antwort festhalten, sie gehört später in die Team-`AGENTS.md`.

13. **Wo soll das Ganze liegen** (eigenes Repo oder im Repo der Anwendung, die es
    beschreibt)? Beim Repo der Anwendung greifen `.claude/settings.json` und
    `.claude/skills/` nur aus dem **Repo-Root**, nicht aus dem Vault-Unterordner, und die
    vorhandene `AGENTS.md` des Projekts muss auf den Vault zeigen. Details in
    `README.md#wenn-das-wissen-ins-repo-der-anwendung-soll`. Dazusagen: Jeder mit
    Repo-Zugriff liest mit.

## Danach: Aufbau

Basierend auf den Antworten:

- **Zuerst den Zielordner anlegen und das Gebrauchte hineinkopieren** (entfällt, wenn ich
  ausdrücklich den Umbau im Kit-Ordner gewählt habe). Mitkommen: `.agents/`,
  `.claude/skills/` (ohne `brain-setup`), `.claude/settings.json`, `Vorlagen/`, `Skripte/`,
  `AGENTS.md`, `CLAUDE.md`, `index.md`, `.gitignore`, `.gitattributes` und `ARCHITECTURE.md`.
  Letzteres als Nachschlagewerk, damit später nachvollziehbar bleibt, warum die Regeln so
  sind. Die drei unscheinbaren Dateien sind nicht optional: ohne `.claude/settings.json` gibt
  es im neuen Brain keinen Hook, den der Schritt weiter unten einrichten könnte, ohne
  `.gitignore` landen die tägliche Statusdatei und `__pycache__/` im ersten Commit, und ohne
  `.gitattributes` schreibt Git unter Windows CRLF, was bei einem Vault auf zwei Geräten
  Diffs über ganze Dateien erzeugt.
  **Nicht** mitkopieren: `README.md`, `SETUP-PROMPT.md`, `tests/`, `.git/` und der
  `brain-setup`-Skill. Das sind Kit-Dateien, kein Vault-Inhalt, und ein mitgeschlepptes
  `.git/` würde den Remote des Kits vererben. `tests/` prüft die mitgelieferten Skripte und
  hat in einem Vault nichts zu suchen; es würde dort nur als Fremdkörper mitgeschleppt. `LICENSE` bleibt ebenfalls hier; nur falls das Brain später selbst
  veröffentlicht werden soll (z.B. ein Team-Brain), gehört sie mit, weil die MIT-Lizenz den
  Copyright-Hinweis verlangt.
  Ab hier arbeitest du **ausschließlich im Zielordner**; das Kit wird nicht mehr verändert.
- Nur die wirklich gebrauchten Top-Level-Ordner anlegen (Auswahl aus: Wissen/Referenz-
  Ordner, Ordner für abgeschlossene Arbeitseinheiten, Personen/, Projekte/laufender-Stand,
  Meetings/, Lernen/, MOCs/, Ressourcen/), mit dem Namen, der zu Frage 1 passt, nicht
  stur "Tickets" wenn ich keine Tickets habe. Der Ordner für laufenden Stand hängt an
  Frage 1b, nicht an 1: ohne ein "ja" dort wird keiner angelegt. Im Kit liegt bewusst KEINER
  dieser Ordner schon vorab; sie entstehen erst hier, aus meinen Antworten.
- Aus `Vorlagen/` die passenden Templates in die neuen Ordner ausrollen, wo sie als
  Startdatei gebraucht werden: `Vorlagen/MOC.md` als erste Landkarte im MOCs-Ordner,
  `Vorlagen/Karten.md` als `Lernen/Karten.md` (nur falls Lernen aktiv),
  `Vorlagen/Glossar.md` in den Wissens-Ordner (nur bei Team-Brain). Die Vorlagen selbst
  bleiben als Templates liegen. **Beim Ausrollen die Platzhalter-Zeilen entfernen und die
  leeren Frontmatter-Felder füllen**: in der MOC-Vorlage die Beispiel-Links auf
  `Wissen/Konzeptname.md` und `MOCs/Anderes-Themengebiet.md`, im Glossar die Beispielzeile,
  in beiden `themengebiet:` und `description:`. In `Vorlagen/` sind das harmlose Muster, im
  echten Ordner werden daraus kaputte Links und Notizen, die der erste Gesundheitscheck als
  unvollständig meldet.
- `AGENTS.md` aus der Vorlage in diesem Kit ableiten: Hard-Facts-Sektion leer/als Platzhalter
  lassen (füllt sich mit der Zeit), Ordnerbeschreibung auf die gewählten Ordner
  zuschneiden, die Trigger-Tabelle nur mit den Skills, die ich tatsächlich mitnehme. **Jede
  Zeile prüfen, die auf etwas Gelöschtes zeigt**, auch außerhalb der Tabelle (z.B. der
  Verweis auf `.agents/knowledge/`, wenn das Schreibstil-Profil mit `formulieren` rausfliegt).
- `.agents/rules/` entsprechend zuschneiden: nicht zutreffende Dateien löschen (z.B.
  `frontmatter.md`s Sichtbarkeits-Abschnitt bzw. `karteikarten.md` ganz, wenn ich in Frage 2
  kein aktives Lernen will; `ablage.md`s Todo-Regel, wenn ich kein externes Tool nutze;
  `team.md` komplett, wenn Frage 0 "nur ich" war), die restlichen auf meine gewählten
  Ordnernamen/Begriffe anpassen.
- Aus `.agents/skills/` nur die Skills behalten, die zu meinen Antworten passen. Die
  vier Brain-Pflege-Skills (brain-input, brain-bereinigen, brain-optimieren,
  merk-dir-das) sind der Kern und bleiben so gut wie immer, alles andere (lernen,
  formulieren, ein Todo-Sync) ist optional und hängt an einer Antwort oben.
- Nicht gebrauchte Vorlagen/Skill-Ordner aus dem Kit **löschen**, nicht nur ignorieren.
  Ein Starter-Kit, das nach dem Setup noch halb aus totem Beispielmaterial besteht, ist
  kein aufgeräumtes Brain. **Nach jeder Löschung die Verweise darauf mitnehmen:** einmal per
  Grep nach dem Namen des Gelöschten über den ganzen Ordner suchen und die Fundstellen
  entfernen oder umbiegen. Löschen ohne Aufräumen hinterlässt tote Verweise in genau den
  Dateien, die neu am wichtigsten sind (`AGENTS.md`, die Regeln, die übrigen Skills).
- `Skripte/brain-check.py` anpassen: die Kategorie-Checks, die zu nicht angelegten Ordnern
  gehören (z.B. Ticket-Naming-Check ohne Tickets-Ordner), rausnehmen oder umbenennen. Die
  Ordner-Konstanten oben im Skript (`TICKET_FOLDER`, `WISSEN_FOLDER`, `SICHTBARKEIT_SCOPE`)
  auf die tatsächlich angelegten Ordnernamen setzen.
- **`index.md` auf die gewählten Ordnernamen ziehen.** Dort steht `FROM "Wissen"` in der
  Dataview-Abfrage; heißt der Wissens-Ordner anders, liefert sie dauerhaft eine leere
  Tabelle, ohne dass irgendwo ein Fehler auftaucht. Ebenso die Struktur- und
  MOC-Platzhalter durch die real angelegten Ordner ersetzen. Wird Obsidian gar nicht
  genutzt, den Dataview-Block ersatzlos streichen statt ihn tot stehen zu lassen.
- **Den SessionStart-Hook nach meiner Antwort auf Frage 7 behandeln.** Habe ich dort "nur auf
  Zuruf" gesagt, `.claude/settings.json` ersatzlos löschen und mir das in einem Satz sagen,
  nicht nochmal nachfragen, die Frage ist beantwortet. Sonst den Hook lauffähig machen: Dort
  steht `python3`; prüf, ob das auf meinem System funktioniert (`python3 --version` und
  `python --version` ausprobieren) und trag den Befehl ein, der wirklich läuft, unter Windows
  meist `python`. Danach einmal testweise ausführen (`<befehl> Skripte/brain-check.py --hook`)
  und mir zeigen, dass er fehlerfrei durchläuft. Ein Hook, der still scheitert, ist schlimmer
  als keiner: er suggeriert eine Kontrolle, die nicht stattfindet.
- **Die Bereinigungs-Frequenz aus Frage 7 auch im Vorgehen festhalten:** In
  `.agents/skills/brain-bereinigen/SKILL.md` den Auslöser-Kopf auf meinen Rhythmus anpassen
  (täglich / wöchentlich / nur auf Zuruf), statt die Kit-Vorgabe stehen zu lassen.
- **Die Skills dorthin bringen, wo sie gebraucht werden, sonst laufen sie ins Leere.**
  Zeiger unter `.claude/skills/` gelten nur für Sessions, die **im Brain-Ordner** starten;
  Claude Code lädt Projekt-Skills ausschließlich aus dem Arbeitsverzeichnis und darunter.
  Der typische Moment für "ab ins brain" ist aber das Ende einer Arbeitssession in einem
  ganz anderen Ordner, dort wäre keine der Routinen auslösbar. Frag mich deshalb, ob die
  Skills überall verfügbar sein sollen. Bei "ja":
  - Die Zeiger der behaltenen Skills zusätzlich nach `~/.claude/skills/<slug>/SKILL.md`
    kopieren, persönliche Skills gelten projektübergreifend.
  - **In der globalen Kopie den Pfad absolut schreiben.** Der relative Verweis
    `.agents/skills/<slug>/SKILL.md` zeigt von dort aus ins Leere. Stattdessen den vollen
    Vault-Pfad nennen, plus einen Satz für den Fall, dass er nicht mehr stimmt: im Vault
    nach der Datei mit passendem `name:` im Frontmatter suchen und mir melden, dass der
    Zeiger veraltet ist.
  - Den Brain-Ordner in `~/.claude/settings.json` unter
    `permissions.additionalDirectories` eintragen, damit die AI ihn aus fremden Ordnern
    heraus überhaupt lesen und beschreiben darf. Wer das nicht dauerhaft will, nutzt
    stattdessen `/add-dir <pfad>` je Session.
  - **Den Hook mitziehen, falls er eingerichtet wurde** (Frage 7). Er steht sonst in der
    `.claude/settings.json` des Brains und feuert nur dort, also gerade nicht in den
    Sessions, für die dieser ganze Schritt gemacht wird. Also den Hook-Eintrag stattdessen
    in `~/.claude/settings.json` anlegen und die lokale Datei entfernen. Dabei
    `${CLAUDE_PROJECT_DIR}` **durch den absoluten Vault-Pfad ersetzen**: global zeigt die
    Variable auf das jeweils offene Projekt, der Hook würde also im fremden Ordner nach dem
    Skript suchen und still scheitern.
  - Mir dazusagen, dass das alles **globale** Konfiguration ist (gilt für alle Projekte,
    liegt außerhalb meines Brains), und dass die Kopien und Pfade beim nächsten Umbenennen
    oder Verschieben des Vaults nachgezogen werden müssen.

  Sage ich "nein", bleibt alles im Brain-Ordner; dann in einem Satz erwähnen, dass die
  Routinen und die tägliche Erinnerung nur in Sessions greifen, die dort laufen.
- **Nur bei Team-Brain (Frage 0):**
  - `.agents/rules/team.md` behalten (im Solo-Fall wird sie gelöscht) und auf die Antworten
    aus Frage 9 bis 13 zuschneiden: Kürzel-Schema für `human:<kürzel>` festlegen, die
    Direktschreiber-Regel streichen, falls alle über die AI schreiben.
  - Die Frontmatter-Vorlagen um `generated`, `verified` und `sources` ergänzen (Form siehe
    `.agents/rules/team.md`), aber nur, wenn Frage 10 mit ja beantwortet wurde. Ohne dieses
    Ja bleiben die Felder weg, sie wären dann Pflichtübung ohne Abnehmer.
  - `Vorlagen/Glossar.md` in den Wissens-Ordner ausrollen. Im Team lohnt es fast immer, weil
    Hausbegriffe für neue Leute und für die AI die eigentliche Hürde sind.
  - Einen automatisierten/geplanten Bereinigungslauf nur dann einrichten, wenn Frage 11 das
    bestätigt hat, gestützt auf `verified` und `stale_after`.
  - **Nach der Bezeichnung fragen.** "Brain" ist nicht überall beliebt, der Begriff
    suggeriert, das Ding denke selbst, dabei ist es ein Wissensspeicher. In Teams sind
    Namen wie "Projektwissen" oder "Fachwissen" oft die bessere Wahl. Frag danach und
    benutze die gewählte Bezeichnung durchgängig in `AGENTS.md`, `index.md` und den
    Auslöser-Phrasen der Trigger-Tabelle. Die Skill-Ordnernamen (`brain-input` usw.) bleiben
    wie sie sind, sonst zeigen alle Zeiger ins Leere.
    **Eine umbenannte Auslöser-Phrase muss an allen drei Stellen ankommen**, sonst meldet
    `skills-check.py` sofort Drift und liegt damit richtig: die `**Auslöser:**`-Kopfzeile in
    `.agents/skills/<slug>/SKILL.md`, die `description:` im Zeiger unter `.claude/skills/`
    und die Tabelle in `AGENTS.md`. Wer nur die Tabelle anfasst, hat den Skill für Claude
    Code unter dem alten Namen und für alle anderen Tools unter dem neuen. Vorsicht bei
    `brain-optimieren`: Dort steht eine Phrase **zweimal** in der Kopfzeile, einmal in der
    Aufzählung und einmal im Satz darunter. Nach dem Umbenennen einmal per Grep über die alte
    Phrase gehen, statt sich auf das erste Vorkommen zu verlassen.
  - **Den Ablageort aus Frage 13 umsetzen.** Bei "eigenes Repo" ist nichts weiter zu tun.
    Bei "im Repo der Anwendung" reicht Hineinkopieren nicht, drei Dinge scheitern sonst
    still (Begründung in `README.md#wenn-das-wissen-ins-repo-der-anwendung-soll`):
    - Den Hook-Eintrag in die `.claude/settings.json` im **Repo-Root** schreiben, nicht in
      die des Vault-Unterordners. Letztere wird von Claude Code nie gelesen. Pfad im Befehl
      entsprechend auf `<vault-ordner>/Skripte/brain-check.py` setzen.
    - Die Skill-Zeiger nach `<repo-root>/.claude/skills/<slug>/SKILL.md` legen, ebenfalls
      aus dem Root. Im Zeiger den Pfad auf
      `<vault-ordner>/.agents/skills/<slug>/SKILL.md` schreiben.
    - Die **vorhandene** `AGENTS.md` des Projekts nicht überschreiben. Dort nur einen kurzen
      Abschnitt ergänzen: wo das fachliche Wissen liegt, plus die Auslöser-Tabelle. Die
      Vault-`AGENTS.md` bleibt im Unterordner der Navigations-Einstieg.
    - In `Skripte/brain-check.py` `CONTEXT_FILES` auf die Kontextdateien setzen, die der
      Agent tatsächlich lädt, im Repo-Fall also die im Root.
    Dazusagen: Jeder mit Repo-Zugriff liest mit, personenbezogene Daten gehören dort nicht
    hinein.
  - **Die Doku-Abgrenzung aus Frage 12 festhalten.** In die Team-`AGENTS.md` einen kurzen
    Abschnitt schreiben, der sagt, welche Quelle wofür zuständig bleibt und was der Vault
    übernimmt. Ohne diesen Satz landet dieselbe Aussage über kurz oder lang in Handbuch und
    Vault, und beide veralten getrennt voneinander.
  - **Erstbefüllung anbieten, statt bei null zu starten.** Bei einem laufenden Projekt gibt
    es meist schon Wissen in Handbüchern, Wikis oder Readmes. Anbieten, eine vorhandene
    Quelle einzulesen, die Aussagen gegen den Code zu prüfen und daraus die ersten Notizen
    zu bauen, jeweils mit `sources`-Eintrag und `generated.by` auf das eigene Tool-Kürzel.
    Das bringt in einem Durchgang mehr als Monate an Session-Ernte. Widersprüche zwischen
    Doku und Code dabei nicht auflösen, sondern sammeln und am Ende zeigen.
- **Die Kit-Version ins Brain schreiben.** Als letzte Zeile meiner neuen `AGENTS.md`:
  `Kit-Version: <x.y.z>`, mit der Versionsnummer aus dem obersten Abschnitt von
  `CHANGELOG.md` im Kit. Das ist keine Deko: Ohne diese Zeile kann eine spätere Migration
  (`MIGRATION.md`) nicht wissen, welche Änderungen mein Brain schon kennt, und müsste
  entweder alles oder nichts vorschlagen.
- **Die eigene Arbeit gegenprüfen, bevor du mir Vollzug meldest:** `Skripte/brain-check.py`
  und `Skripte/skills-check.py` laufen lassen. Alles, was sie melden, hat das Setup gerade
  selbst verursacht: tote Verweise auf Gelöschtes, Platzhalter aus ausgerollten Vorlagen,
  Skills in `AGENTS.md`, die es nicht mehr gibt. Aufräumen und erst dann weiter. Ein frisch
  aufgesetzter Vault, dessen erster Gesundheitscheck rot ist, verspielt genau das Vertrauen,
  das die Routinen später brauchen.
- Zum Schluss kurz zusammenfassen, was angelegt wurde und wie ich es ab jetzt benutze
  (welche Trigger-Phrasen starten was), plus einen Hinweis, `README.md` und
  `ARCHITECTURE.md` bei Bedarf später erneut zu lesen.
- **Nach der Sicherung fragen**, ein Satz: Wo soll dieser Ordner gesichert werden und soll er
  auf ein zweites Gerät (privates Git-Repo, Cloud-Ordner, externe Platte)? Es gibt keinen
  Anbieter, der das im Hintergrund erledigt, siehe `README.md#sicherung-und-zweites-gerät`
  und ARCHITECTURE.md#11. Bei Personendaten im Vault ist das keine reine Komfortfrage.
- **Nur falls ich den Umbau im Kit-Ordner gewählt habe:** dort `SETUP-PROMPT.md`
  **umbenennen, nicht leeren** → `SETUP-PROMPT-erledigt.md`, mit einer neuen ersten Zeile
  "Setup am <heutiges Datum> gelaufen, siehe `AGENTS.md`. Dieser Fragebogen ist
  aufgehoben, falls ich später neu aufsetzen oder nachschlagen will." Sonst liefe man Gefahr,
  ihn bei einem späteren `git pull` versehentlich ein zweites Mal loszuschicken und ein
  fertiges Brain zu überschreiben. Löschen wäre falsch: ohne Git (ZIP-Download) gäbe es
  keinen Weg zurück.
  **Liegt das Brain dagegen in einem eigenen Ordner, das Kit unverändert lassen**: Dort ist
  keine `SETUP-PROMPT.md`, und im Kit soll sie bleiben, damit es ein zweites Mal nutzbar ist
  (weiteres Brain, Team-Brain).
- **Wenn ich das Brain versionieren will**, im Zielordner `git init` anbieten, mit dem
  ausdrücklichen Hinweis, dass ein daraus entstehendes GitHub-Repo **privat** sein muss.
  Niemals den Remote des Kits übernehmen.

Fang nicht an zu schreiben, bevor du nicht alle relevanten Fragen gestellt und meine
Antworten hast. Bei Unsicherheit lieber kurz nachfragen als raten.
```

---

## Kurz-Einstieg: drei Fragen

Für alle, denen das Interview oben zu groß ist, oder die erst einmal sehen wollen, ob ihnen
die Idee überhaupt liegt, bevor sie eine Viertelstunde Fragen beantworten. Dieser Prompt legt
ein **Minimal-Vault** an: ein Wissens-Ordner, eine Landkarte, die vier Pflege-Skills. Mehr
nicht. Alles Weitere (Personen, Projekte, Arbeitseinheiten, Lernen) kann später dazukommen,
entweder von Hand oder indem du das lange Interview oben nachholst. Es bleibt dir erhalten:
das Setup benennt diese Datei am Ende nur um (`SETUP-PROMPT-erledigt.md`), statt sie zu
leeren, damit beide Prompts nachlesbar bleiben.

Der Unterschied ist nur die Gründlichkeit, nicht das Modell. Was hier entsteht, ist ein
kleiner, aber echter Vault nach denselben Prinzipien, kein Wegwerf-Prototyp.

---

```
Ich richte mein persönliches "Second Brain" ein, einen Wissens-Vault (Markdown/
Obsidian-kompatibel), den du als AI dauerhaft mitpflegst: du liest ihn zu Beginn jeder
Session, schreibst als einzige Instanz hinein, und hältst ihn nach festen Konventionen
sauber. Dieses Repo ist das Starter-Kit dafür.

**Frag mich zuerst, wo mein Brain entstehen soll und wie es heißen soll** (Pfad + Ordnername,
gern mit Vorschlag). Das Kit bleibt die Vorlage und wird nicht umgebaut, sonst erbt mein
Brain den GitHub-Remote des Kits, und ein unbedachter Push würde private Notizen öffentlich
machen. Andere in dieser Session sichtbare Ordner sind nie gemeint, auch kein bereits
eingerichteter Vault. Nenn mir den Zielpfad absolut und warte auf mein OK, bevor du schreibst.

Ich will den KURZEN Einstieg, nicht das große Interview. Stell mir genau die drei Fragen
unten, eine nach der anderen, und bau danach ein bewusst minimales Setup. Frag nicht nach
Dingen, die hier nicht stehen; für alles andere gilt: sinnvoller Standard jetzt, Ausbau
später.

Lies vorher ARCHITECTURE.md, Abschnitte 1 bis 6 (das ist das Modell, das auch im
Minimal-Setup gilt) plus Abschnitt 11 (warum die Sicherung meine Sache ist).

## Fragen

1. **Was machst du beruflich/hauptsächlich?** Ein, zwei Sätze reichen. Daraus leitest du
   die Themenfelder ab, mit denen der Vault startet.

2. **Willst du das gesammelte Wissen aktiv lernen** (dich von mir abfragen lassen), oder
   reicht dir Nachschlagen?

3. **In welcher Sprache soll der Vault-Inhalt sein**, und sollen Dateinamen reines ASCII
   sein (empfehlenswert unter Windows/Git)?

## Danach: Aufbau (klein halten)

- **Zielordner anlegen und das Gebrauchte hineinkopieren:** `.agents/`, `.claude/skills/`
  (ohne `brain-setup`), `.claude/settings.json`, `Vorlagen/`, `Skripte/`, `AGENTS.md`,
  `CLAUDE.md`, `index.md`, `.gitignore`, `.gitattributes`, `ARCHITECTURE.md`. Die
  `settings.json` wird weiter unten gebraucht (Hook), die `.gitignore` hält Statusdatei und
  `__pycache__/` aus einem späteren Repo, die `.gitattributes` hält die Zeilenenden auf LF.
  **Nicht** mit: `README.md`, `LICENSE`, `SETUP-PROMPT.md`, `tests/`, `.git/`.
  Danach nur noch im Zielordner arbeiten, das Kit bleibt unverändert.
- Zwei Ordner anlegen: einen Wissens-Ordner und `MOCs/`. Dazu `Lernen/` **nur**, wenn ich bei
  Frage 2 aktives Lernen wollte. Sonst keine weiteren, auch nicht "schon mal für später".
- `Vorlagen/MOC.md` als erste Landkarte in `MOCs/` ausrollen, passend zu Frage 1 benannt,
  dabei die Platzhalter-Beispiellinks entfernen, sonst stehen sie als kaputte Links im Vault.
- `AGENTS.md` aus der Vorlage ableiten, aber kurz: nur die tatsächlich angelegten Ordner, nur
  die vier Pflege-Skills in der Trigger-Tabelle (plus `lernen`, falls aktiv),
  Hard-Facts-Abschnitt als Platzhalter.
- Aus `.agents/skills/` nur die vier Kern-Skills behalten (brain-input, brain-bereinigen,
  brain-optimieren, merk-dir-das). `formulieren` und `lernen` LÖSCHEN, samt ihrer
  `.claude/skills/`-Zeiger, außer Frage 2 war "aktiv lernen", dann bleibt `lernen` drin
  und `Vorlagen/Karten.md` wird als `Lernen/Karten.md` ausgerollt.
- Aus `.agents/rules/` die Dateien behalten, die für zwei Ordner Sinn ergeben; nicht
  Zutreffendes (z.B. `karteikarten.md` ohne aktives Lernen, `team.md` im Solo-Fall) löschen.
  Ebenso `Vorlagen/Glossar.md`, das ist eine Team-Vorlage.
- Nicht gebrauchte Vorlagen löschen, nicht liegen lassen, und per Grep nach dem Namen jedes
  Gelöschten suchen, damit keine toten Verweise in `AGENTS.md` oder den Regeln zurückbleiben.
- `Skripte/brain-check.py` anpassen: `TICKET_FOLDER = None` setzen (es gibt keinen
  Arbeitseinheiten-Ordner), `WISSEN_FOLDER` und `SICHTBARKEIT_SCOPE` auf den tatsächlich
  gewählten Wissens-Ordner setzen.
- `index.md` mitziehen: In der Dataview-Abfrage steht `FROM "Wissen"`; heißt der
  Wissens-Ordner anders, bleibt die Tabelle stumm leer. Ohne Obsidian den Block streichen.
- **Die Kit-Version ins Brain schreiben**, als letzte Zeile der neuen `AGENTS.md`:
  `Kit-Version: <x.y.z>` aus dem obersten Abschnitt von `CHANGELOG.md`. Eine spätere
  Migration (`MIGRATION.md`) braucht sie, um zu wissen, was mein Brain schon kennt.
- **Erst jetzt `Skripte/brain-check.py` und `Skripte/skills-check.py` laufen lassen** und
  aufräumen, was sie melden. Was dort auftaucht, hat dieses Setup gerade selbst verursacht.
  Die Reihenfolge ist wichtig: vor der Anpassung oben prüft das Skript noch gegen die
  Kit-Ordnernamen und meldet dann nichtssagend "alles grün".
- In `.claude/settings.json` den Python-Befehl des SessionStart-Hooks prüfen (dort steht
  `python3`, unter Windows meist `python`), einmal testweise laufen lassen, und mich fragen,
  ob ich die tägliche Erinnerung will, sonst die Datei löschen.
- **Fragen, ob die vier Pflege-Skills überall verfügbar sein sollen** oder nur in Sessions,
  die im Brain-Ordner starten. Zeiger unter `.claude/skills/` gelten nämlich nur für dieses
  eine Verzeichnis, "ab ins brain" am Ende einer Arbeitssession woanders liefe ins Leere.
  Bei "ja": die Zeiger zusätzlich nach `~/.claude/skills/<slug>/SKILL.md` kopieren, dort den
  **absoluten** Vault-Pfad hineinschreiben (der relative zeigt von dort ins Leere), und den
  Brain-Ordner in `~/.claude/settings.json` unter `permissions.additionalDirectories`
  eintragen. Einen eingerichteten Hook dann ebenfalls dorthin verschieben, mit absolutem
  Pfad statt `${CLAUDE_PROJECT_DIR}`, global zeigt die Variable sonst auf das gerade offene
  fremde Projekt. Dazusagen, dass das globale Konfiguration außerhalb meines Brains ist.
- Zum Schluss in drei, vier Sätzen erklären, wie es ab jetzt läuft: welche Phrase startet
  was, und dass der Vault mit der Zeit wächst statt vorab fertig zu sein.
- **Nach der Sicherung fragen**, ein Satz, keine Belehrung: Wo soll dieser Ordner gesichert
  werden (privates Git-Repo, Cloud-Ordner, externe Platte)? Wer hier klein anfängt, hat in
  drei Monaten Wissen drin, das er nicht verlieren will. Die drei Wege stehen in
  `README.md#sicherung-und-zweites-gerät`.
- **Nur falls ich ausnahmsweise den Umbau im Kit-Ordner gewählt habe:** dort diese Datei
  **umbenennen, nicht leeren** → `SETUP-PROMPT-erledigt.md`, erste Zeile "Kurz-Einstieg am
  <heutiges Datum> gelaufen, siehe `AGENTS.md`. Das ausführliche Interview steht weiter unten
  in dieser Datei." Nicht löschen: ohne Git gäbe es keinen Weg zurück. Liegt mein Brain
  dagegen in einem eigenen Ordner, bleibt das Kit komplett unverändert.
- **Wenn ich versionieren will:** `git init` im Zielordner anbieten, und dazusagen, dass ein
  GitHub-Repo daraus **privat** sein muss. Nie den Remote des Kits übernehmen.

Fang nicht an zu schreiben, bevor ich alle drei Fragen beantwortet habe.
```
