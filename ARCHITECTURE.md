# Architektur: Wie und warum dieses Brain so aufgebaut ist

Dieses Dokument erklärt das Grundmodell hinter dem Starter-Kit, losgelöst von einer
konkreten Ordnerstruktur. Die Ordner ändern sich je nach Person (siehe `SETUP-PROMPT.md`),
diese Prinzipien nicht.

## 1. Eine schreibende Instanz

Der Vault hat genau eine Instanz, die hineinschreibt: die AI. Der Mensch liest und korrigiert
im Gespräch, tippt aber selbst keine Notizen. Das klingt nach einer Kleinigkeit, ist aber
die Voraussetzung für alles Weitere: Konventionen (Frontmatter,
Linkformat, Notizaufbau) lassen sich nur konsequent durchhalten, wenn eine einzige Instanz
sie durchsetzt. Bei zwei Schreibern (Mensch und AI) driftet der Stil garantiert auseinander.

Konsequenz für Konventionen: sie sind **Pflicht der AI**, nie eine Bitte an den Menschen.
"Du solltest die Notiz so formatieren" ist im Modell sinnlos, die AI formatiert selbst
korrekt.

## 2. Evergreen-Wissen vs. laufender Stand, die wichtigste Trennung

Der häufigste Fehler in gewachsenen Notiz-Systemen: Wissen und Status vermischen sich im
selben Dokument, bis man nicht mehr weiß, was davon noch stimmt.

Drei Kategorien, klar getrennt:

- **Evergreen-Wissen:** Konzepte, Patterns, Fakten, die in einem halben Jahr noch wahr
  sind. Gehört in einen reinen Wissens-Ordner, nie in eine Status-Notiz vergraben.
- **Laufender Stand:** aktuelle Version, offene Punkte, "warten auf X", Entscheidungen zu
  einer noch laufenden Sache. Ändert sich ständig, gehört in eine lebende Projekt- oder
  Bereichs-Notiz, die überschrieben statt fortgeschrieben wird.
- **Abgeschlossene Arbeitseinheiten:** die konkrete Historie einer einzelnen erledigten
  Aufgabe (Ticket, Auftrag, Fall, Session). Wird nicht mehr geändert, ist aber durchsuchbar.

Faustregel beim Schreiben einer neuen Notiz: *"In 6 Monaten gefragt, noch wahr?"* → Wissen.
*"Aktueller Stand, ändert sich bald wieder?"* → laufende Projekt-Notiz. *"Arbeit an genau
dieser einen Sache?"* → abgeschlossene Arbeitseinheit.

## 3. Das `type`-Feld: Lernstoff vs. Nachschlagewissen vs. Ablauf

Nicht jede Wissens-Notiz will abgefragt werden. Drei Rollen, ein Frontmatter-Feld:

- **Konzept** (Default): Lernstoff-*Kandidat* und AI-Referenz zugleich.
- **Referenz:** reines Nachschlagewissen (Cheatsheets, Fakten, Konfigurationsdetails). Die
  AI liest es, es wird **nie** abgefragt, sonst verstopft Nachschlagewissen die Lernrunde.
- **Vorgehen:** eine Routine oder ein Skill-Dokument. Auch kein Lernstoff.

Der Grund, das explizit zu trennen statt alles als "Wissen" zu behandeln: eine Lernrunde,
die auch Konfigurationsdetails und Skill-Anleitungen abfragt, wird schnell sinnlos und dann
ignoriert. Die Trennung hält den Lernstoff-Ballast aus dem Rest raus.

Wichtig: `type: Konzept` allein macht noch **keine** Karte. Ob eine Notiz tatsächlich
abgefragt wird, entscheidet ein zweites, härteres Kriterium: *muss dieses Wissen aus dem
Kopf gekonnt werden (Daily, Review, Gespräch), oder reicht Nachschlagen?* Nur im ersten Fall
entsteht **bewusst** eine atomare Karte. Sie entsteht später über die Brain-Pflege-Routinen
(Punkt 6), nie automatisch beim Anlegen der Notiz. Die Karten selbst leben zentral in einer
eigenen Lern-Datei, Frage, Antwort und Lernstand in einer Zeile. In der Wissens-Notiz steht
dazu kein Quiz-Block. Sonst hat jede Karte zwei Pflegestellen (Notiz-Inhalt und Lernstand),
die bei Umformulierungen auseinanderlaufen.

## 4. MOCs, kuratierte Landkarten statt automatisch generierter Listen

Ein automatisch generierter Index (Datenbank-Abfrage über alle Notizen) zeigt *dass* etwas
existiert, nicht *wie es zusammenhängt*. Eine MOC (Map of Content) pro Themengebiet ist eine
handkuratierte Übersichtsnotiz, die die Einzelnotizen gruppiert und in Beziehung setzt. Sie
ist der beste Einstiegspunkt für eine AI in ein Themengebiet, weil sie sofort die
Cluster-Struktur zeigt statt einer flachen alphabetischen Liste.

Wichtig: MOCs pflegen sich **nicht** automatisch (anders als ein generierter Index). Jede
neue Wissensnotiz muss aktiv eingehängt werden, sonst veraltet die Landkarte.

## 5. Mindmap-Verlinkung statt Sternstruktur

Querverbindungen entstehen direkt zwischen Notizen, nicht ausschließlich über einen
zentralen Hub oder Index. Ziel ist ein organisches Netz, kein Stern mit dem Index in der
Mitte. Jeder Link bekommt einen Halbsatz Kontext ("warum ist das relevant"), nicht nur den
Titel. Eine kontextlose Linkliste zwingt beim Lesen zu genau der Einordnung, die man beim
Schreiben hätte treffen sollen. Und: Verlinkung geht in **beide Richtungen**, verweist A auf
B, bekommt B auch einen Link zurück zu A.

## 6. Die Brain-Pflege pflegt sich selbst

Ein Vault, der nur wächst, wird nach einem Jahr unbrauchbar: veraltete Fakten, tote Links,
Notizen, die niemand mehr braucht. Vier Routinen halten das im Griff, jede mit einer klaren
Frequenz und einem klaren Zweck:

| Routine | Frequenz | Zweck |
|---|---|---|
| **Brain-Input** | Am Ende jeder relevanten Session | Was aus diesem Gespräch gehört dauerhaft ins Brain? Vorschau vor dem Schreiben, dann erst schreiben. |
| **Merk-dir-das** | Mitten im Gespräch, auf Zuruf | Eine einzelne Info sofort festhalten, mit Rückfrage, wohin, nicht automatisch. |
| **Brain-bereinigen** | Regelmäßig (z.B. täglich), eine Datei pro Durchlauf | Systematisch jede Notiz irgendwann auf Aktualität, Relevanz und Kürzung prüfen. |
| **Brain-optimieren** | Auf Zuruf oder periodisch | Mechanischer Gesundheitscheck (Skript) übers ganze Vault plus gelegentlicher Tiefen-Check (wird es noch benutzt, ist die Struktur noch passend). |

Das Zusammenspiel ist bewusst so gebaut. Brain-Input fängt den Moment ab, in dem am
billigsten korrigiert werden kann (beim Schreiben). Brain-Bereinigen holt nach, was beim
Schreiben durchgerutscht ist. Brain-Optimieren findet die mechanischen Symptome, die kein
einzelner Schreibmoment sieht (kaputte Links durch spätere Umbenennungen, fehlende
Rücklinks). Ohne diese Routinen sammelt sich zwangsläufig Unrat an, kein Vault bleibt von
allein sauber.

## 7. Vorschau vor dem Schreiben

Bei sammelnden Routinen (v.a. Brain-Input) gilt: **nie direkt schreiben.** Erst den
kompletten geplanten Inhalt jeder Notiz im Gespräch zeigen, auf Bestätigung warten, dann
erst in den Vault schreiben. Der Schreibmoment ist der günstigste Zeitpunkt, um eine
Fehlinterpretation abzufangen, danach wird es nur noch Aufräumarbeit.

## 8. Fail closed bei Sensiblem

Wer Kunden-, Patienten- oder sonstige Personendaten im Vault führt, klassifiziert jede
Notiz explizit (öffentlich zeigbar / intern / vertraulich, oder ein eigenes Schema). Fehlt
die Klassifizierung, gilt eine Notiz automatisch als **vertraulich**, nie umgekehrt. Das
macht spätere Nutzung (z.B. Demo-Ausschnitte fürs eigene Portfolio) mechanisch statt
manuell-riskant.

## 9. Struktur folgt der Person, nicht umgekehrt

Nichts oben zwingt zu bestimmten Ordnernamen. Wer keine abgeschlossenen Arbeitseinheiten
im Ticket-Sinn hat, braucht keinen entsprechenden Ordner. Wer nicht aktiv lernen will,
braucht weder Kartenstapel noch Lernrunde. Was bleibt, ist das Modell aus 1 bis 8. Die
Entscheidung, *welche* Ordner und Module daraus für eine konkrete Person sinnvoll sind,
trifft das Interview in `SETUP-PROMPT.md`.

## 10. Team-Variante: wenn Abschnitt 1 nicht mehr wörtlich gilt

Alles oben geht von **einer** schreibenden Instanz aus (Abschnitt 1). Sobald mehrere
Menschen aktiv mitschreiben, mit oder ohne AI dazwischen, kippt diese Voraussetzung. Dann
müssen zwei Dinge dazukommen, die im Solo-Fall bewusst fehlen:

- **Herkunfts- und Vertrauens-Kennzeichnung pro Aussage.** Bei einer schreibenden Instanz ist
  jede Notiz gleich vertrauenswürdig, es gibt nur die eine Quelle. Bei mehreren Schreibern
  gilt das nicht mehr: eine Aussage kann von einer Person aktiv bestätigt sein oder von der
  AI aus einem Gespräch abgeleitet, kann frisch sein oder seit Monaten unangefasst. Diese
  Unterscheidung braucht eigene Frontmatter-Felder, nicht nur `type`. Die konkreten Felder
  stehen in `.agents/rules/team.md`; sie folgen dem Open Knowledge Format (siehe unten),
  statt eigene zu erfinden.
- **Multi-Writer-Konvention statt "Konventionen sind Pflicht der AI".** Abschnitt 1 sagt,
  Konventionen durchzusetzen sei allein Sache der AI, weil nur sie schreibt. Schreiben
  mehrere Menschen direkt mit, gilt das nicht mehr. Dann braucht es eine für Menschen
  lesbare, kurze Schreib-Konvention zusätzlich zur AI-Durchsetzung, sonst driften die
  Stile der Mitschreiber auseinander, ohne dass die AI das je korrigieren könnte (sie sieht
  die Abweichung erst, nachdem sie längst geschrieben ist).

**Automatisierte, geplante Bereinigung ist die eine Sache, die im Solo-Fall bewusst fehlt
und im Team-Fall Sinn ergeben kann, aber nur unter dieser Bedingung:** Ohne
Herkunfts- und Vertrauens-Kennzeichnung ist ein automatisierter Lauf blind. Er kann nicht
unterscheiden, ob eine unauffällige, alte Notiz absichtlich stabil ist oder schlicht
niemand mehr hinschaut. Erst mit den Feldern oben hat ein Skript ein Signal, auf das es sich
verlassen kann (z.B. "von einer Person bestätigt, nie automatisch anfassen" gegen "von der
AI abgeleitet, seit Monaten unbestätigt, Kandidat fürs Archiv"). Ohne diese Felder bleibt
Bereinigung getriggert (siehe Abschnitt 6). Automatisiert ohne Vertrauens-Signal wird sie
zum Risiko.

Diese Erweiterung hängt bewusst an der Team-Weiche in `SETUP-PROMPT.md` (Frage 0) statt im
Standard-Interview zu stehen: Ein Solo-Vault mit nur einer schreibenden Instanz braucht
diese Felder nicht, sie wären dort reiner Mehraufwand ohne Gegenwert.

### Warum die Felder aus dem Open Knowledge Format kommen

Für genau dieses Problem gibt es seit Juni 2026 einen offenen Standard: das **Open Knowledge
Format (OKF)** von Google Cloud, inzwischen in Version 0.2. Es beschreibt Wissen als
Verzeichnis von Markdown-Dateien mit YAML-Frontmatter, ein Konzept pro Datei, per
Markdown-Links zu einem Graphen verbunden. Also dasselbe Modell wie hier, unabhängig
entstanden.

Interessant macht es aber etwas anderes als die Struktur. In v0.2 bekommen Herkunft,
Vertrauen und Alterung eigene Felder: `generated` (wer hat den Inhalt erzeugt, wann),
`verified` (eine Liste unabhängiger Bestätigungen), `sources` (woraus abgeleitet, mit Autor
und Datum je Quelle) und `stale_after` (ab wann gilt das als überholt). Wer im Team-Fall
eigene Felder erfindet, baut dasselbe noch einmal, nur schlechter: ein einzelnes
`herkunft`-Feld vermischt Erzeuger und Bestätiger und kennt immer nur einen davon.

Deshalb nutzt die Team-Variante diese Namen. **Übernommen wird nur, was trägt**, denn OKF
verlangt selbst nur ein einziges Pflichtfeld (`type`), alles andere ist optional, und
Consumer müssen unbekannte Zusatzfelder tolerieren. `themengebiet`, `sichtbarkeit` und
`letzte-bereinigung` bleiben also unangetastet. Zwei Punkte, an denen dieses Kit bewusst
abweicht: `index.md` ist bei OKF ein reservierter Name mit fester Listing-Struktur (hier
steht Fließtext drin), und `status` heißt im Standard `draft|stable|deprecated`, während es in
`Vorlagen/Vorgang.md` den Bearbeitungsstand einer Arbeitseinheit meint. Das Vault ist damit
**OKF-nah, aber kein konformes Bundle**, und das ist in Ordnung, solange man es nicht anders
behauptet.

Auch im Solo-Fall lohnt ein Feld daraus: `stale_after: YYYY-MM-DD` an Quellen-Notizen macht
aus der Faustregel "älter als drei Monate ist nachprüfbedürftig" ein Datum, das
`brain-check.py` tatsächlich prüfen kann. `generated` und `verified` bleiben dagegen dem
Team-Fall vorbehalten; bei einer einzigen schreibenden Instanz wären sie ein Ritual ohne
Aussage.

## 11. Klartext-Dateien: die Stärke, die eine Bedingung hat

Der Vault ist ein Ordner mit Markdown-Dateien. Kein Datenbankformat, kein Anbieter-Konto,
keine API. Das ist eine bewusste Architekturentscheidung und der Grund, warum dieses Modell
ein Werkzeug überleben kann: Was heute Claude liest, liest morgen ein anderer Agent, und
notfalls ein Mensch mit einem Texteditor. Wissen, das in einem geschlossenen Notiz-Dienst
liegt, ist an dessen Geschäftsmodell gebunden; Wissen in Markdown nicht.

Der Preis steht auf der Rückseite derselben Medaille: **Es gibt keinen Anbieter, der für dich
sichert.** Kein automatisches Cloud-Backup, keine Versionshistorie, keine Wiederherstellung
nach einem Fehlgriff, außer der, die du selbst einrichtest. Ein Vault, in den jemand ein
Jahr lang Wissen schreibt und der dann mit einem Laufwerk verschwindet, ist schlimmer als gar
keiner: Man hat sich in der Zwischenzeit darauf verlassen und anderswo nichts aufgehoben.

Deshalb gehört die Frage "wie wird das gesichert, und wie kommt es auf mein zweites Gerät"
zum Aufsetzen dazu, nicht in ein späteres Kapitel. Die konkreten Wege (privates Git-Repo,
Cloud-Ordner, externe Platte, jeweils mit ihren Nachteilen und der Datenschutz-Abwägung bei
Personendaten) stehen in [README.md](./README.md#sicherung-und-zweites-gerät).

## 12. Pull-Wissen ja, Push-Wissen nein

Abschnitt 2 trennt danach, wie lange etwas gilt. Es fehlt eine zweite Frage, an der ein
Vault genauso zuverlässig kaputtgeht: *Wie kommt dieses Wissen zum Einsatz?*

- **Pull-Wissen** schlägt die AI bei passender Gelegenheit selbst nach. "Wie funktioniert
  der Import in diesem System", "was bedeutet dieser Fachbegriff", "warum wurde das damals
  so entschieden". Es liegt herum, bis jemand danach sucht, und genau dafür ist der Vault da.
- **Push-Wissen** muss immer gelten, ohne dass jemand danach fragt. Coding-Standards,
  "antworte immer auf Deutsch", "vor jedem Commit die Tests laufen lassen". Das gehört in
  die Kontextdatei, die bei jeder Session ohnehin geladen wird (`AGENTS.md`/`CLAUDE.md`),
  oder in einen Hook.

Der Fehler ist, Push-Wissen in den Vault zu schreiben. Es sieht dort ordentlich aus und ist
trotzdem wirkungslos: Eine Regel, die nur wirkt, wenn die AI zufällig die richtige Notiz
liest, wird über kurz oder lang übersehen. Schlimmer, sie erzeugt falsche Sicherheit, weil
sie ja "dokumentiert" ist. Umgekehrt bläht Pull-Wissen in der Kontextdatei jede einzelne
Session auf, auch die neunundneunzig, in denen es niemand braucht.

**Der Aufnahmefilter für Pull-Wissen** hat zwei Bedingungen, und beide müssen erfüllt sein:
*Müsste ich das im Bedarfsfall teuer neu herleiten (Code lesen, jemanden fragen, erneut
recherchieren)?* Und: *bleibt es über die Zeit stabil?* Die Schwelle ist der Vergleich, nicht
das Gefühl: Ist Neu-Herausfinden teurer als die Zeile, die es hier kostet? Wenn nicht,
schreib es nicht auf. Ein Vault, in dem alles steht, ist so unbrauchbar wie einer, in dem
nichts steht, nur teurer in der Pflege.
