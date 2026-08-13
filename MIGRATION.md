# Ein bestehendes Brain auf eine neue Kit-Version nachziehen

Dein Brain ist beim Setup aus diesem Kit entstanden und hat sich seitdem von ihm entfernt:
eigene Ordnernamen, gelöschte Skills, angepasste Konstanten, vielleicht eine andere
Bezeichnung als "Brain". Das ist so gewollt. Es heißt aber auch, dass ein `git pull` hier
nichts für dich tut, und ein Migrationsskript könnte gar nicht wissen, wie dein Vault
aussieht.

Deshalb ist die Migration wie das Setup ein **Prompt**: Die AI liest, was sich geändert hat,
sieht sich dein tatsächliches Brain an und schlägt nur das vor, was dort zutrifft. Du
entscheidest bei jedem Punkt.

**Nichts davon ist Pflicht.** Ein Brain, das seinen Zweck erfüllt, muss keiner neuen
Kit-Version folgen. Sinnvoll ist eine Migration vor allem bei Einträgen, die im
[CHANGELOG](./CHANGELOG.md) unter "Behoben" stehen: Dort liegt in deinem Vault eine Kopie
eines Skripts, das denselben Fehler noch hat.

## So gehst du vor

1. Sieh nach, von welcher Version dein Brain stammt. Das Setup schreibt sie in die
   `AGENTS.md` deines Vaults, ganz unten, als Zeile `Kit-Version: x.y.z`. Fehlt sie, stammt
   das Brain aus der Zeit vor 1.0.0; dann gilt der ganze Changelog als noch nicht angewandt.
2. Hol dir den aktuellen Stand dieses Kits (`git pull`, oder ZIP neu herunterladen).
3. Öffne eine Session, in der **beide** Ordner sichtbar sind, dein Brain und dieses Kit.
4. Schick den Block unten als Nachricht.

---

```
Ich habe ein Second Brain, das aus dem second-brain-starter-kit entstanden ist, und will es
auf den aktuellen Stand des Kits nachziehen. Beide Ordner sind in dieser Session sichtbar.

Wichtig vorweg, das ist der Kern der Aufgabe: Mein Brain ist beim Setup bewusst auf mich
zugeschnitten worden. Es hat eigene Ordnernamen, ich habe Skills gelöscht, Konstanten
angepasst und vielleicht eine andere Bezeichnung als "Brain" gewählt. Nichts davon ist ein
Fehler, der zu beheben wäre. Du gleichst NICHT mein Brain an das Kit an. Du prüfst nur, ob es
im Kit Verbesserungen gibt, die für mein Brain in seiner eigenen Form etwas bringen.

## Schritt 1: Herausfinden, wo ich stehe

Lies in der AGENTS.md meines Brains die Zeile `Kit-Version:`. Steht dort keine, stammt mein
Brain aus der Zeit vor 1.0.0, dann gilt der komplette Changelog als offen. Nenn mir die
gefundene Version und die aktuelle Version des Kits (steht oben in CHANGELOG.md), bevor du
weitermachst.

## Schritt 2: Changelog lesen und filtern

Lies CHANGELOG.md im Kit, aber nur die Einträge NEUER als meine Version. Jeder Eintrag ist
markiert:
- **[Brain]**: kann mich betreffen, weiter prüfen.
- **[Neu]**: betrifft nur Neuaufsetzer, für mich irrelevant. Überspringen, nicht erwähnen.
- **[Kit]**: betrifft nur das Repo selbst. Überspringen.

## Schritt 3: Jeden [Brain]-Eintrag gegen mein echtes Brain halten

Das ist der eigentliche Schritt, und er braucht Urteilsvermögen statt Textvergleich. Prüf für
jeden Eintrag konkret in meinen Dateien nach:

- **Trifft das bei mir überhaupt zu?** Ein Fix an einem Skill, den ich gar nicht habe, ist
  gegenstandslos. Eine Team-Regel in einem Solo-Vault ebenso.
- **Habe ich die Stelle selbst geändert?** Dann NICHT einfach überschreiben. Zeig mir beide
  Fassungen und frag, was gelten soll. Meine Anpassungen haben Vorrang, sie waren Absicht.
- **Bei Skripten: nicht die Kit-Datei drüberkopieren.** In meiner Fassung stehen meine
  Ordnernamen in den Konstanten oben (TICKET_FOLDER, WISSEN_FOLDER, SICHTBARKEIT_SCOPE,
  CONTEXT_FILES) und möglicherweise entfernte Kategorie-Checks. Übernimm nur die inhaltliche
  Änderung, meine Konfiguration bleibt stehen. Ein blindes Kopieren würde meinen Vault-Check
  auf fremde Ordnernamen umstellen, und der meldet danach entweder nichts mehr oder alles.
- **Bei umbenannten Auslöser-Phrasen aufpassen.** Habe ich die Bezeichnung geändert (etwa
  "Projektwissen" statt "Brain"), heißen meine Phrasen anders als im Kit. Übernimm die
  Sache, nicht den Wortlaut, und halte die drei Stellen zusammen: die `**Auslöser:**`-Zeile
  in `.agents/skills/<slug>/SKILL.md`, die `description:` im Zeiger unter `.claude/skills/`
  und die Tabelle in `AGENTS.md`.

## Schritt 4: Vorlegen, bevor du etwas anfasst

Zeig mir eine Liste: pro Eintrag, was er in MEINEM Brain konkret ändern würde, in welcher
Datei, und was ich davon habe. Sortiert nach Nutzen, die Fehlerkorrekturen zuerst, denn dort
liegt in meinem Vault eine Kopie mit demselben Fehler.

Sag ausdrücklich dazu, was du übersprungen hast und warum. Ein Migrationsbericht, der nur
zeigt, was gemacht werden soll, verschweigt die interessantere Hälfte.

Dann warte auf mein OK. Ich entscheide bei jedem Punkt einzeln, "alles" ist eine gültige
Antwort, "nichts" auch.

## Schritt 5: Umsetzen und gegenprüfen

Erst nach meiner Freigabe ändern. Danach in meinem Brain `Skripte/brain-check.py` und
`Skripte/skills-check.py` laufen lassen und aufräumen, was sie melden. Was dort auftaucht,
hat diese Migration gerade selbst verursacht.

Zum Schluss die Zeile `Kit-Version:` in meiner AGENTS.md auf die neue Version setzen, aber
NUR wenn ich alle vorgeschlagenen [Brain]-Punkte übernommen habe. Habe ich etwas bewusst
ausgelassen, schreib die alte Version stehen lassen und stattdessen dazu, welche Punkte offen
sind, sonst gilt beim nächsten Mal als erledigt, was nie passiert ist.

Fang nicht an zu ändern, bevor ich die Liste aus Schritt 4 gesehen und freigegeben habe.
```

---

## Wenn etwas schiefgeht

Die Migration fasst Dateien in deinem Vault an. Falls du ihn versionierst, mach sie in einem
eigenen Branch oder committe vorher, dann ist ein Rückweg einen Befehl entfernt. Falls nicht,
ist jetzt der Moment für die Sicherungskopie, siehe
[README.md](./README.md#sicherung-und-zweites-gerät).
