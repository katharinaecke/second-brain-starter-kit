# Team-Vault *(optional, nur falls beim Setup "Team" gewählt wurde, sonst diese Datei löschen)*

> Teil der Vault-Schreibkonventionen (`.agents/rules/`, Übersicht in `AGENTS.md`). Nur laden, wenn Vault-Inhalte **angelegt oder editiert** werden.

Sobald mehrere Menschen mitschreiben, gilt `grundhaltung.md` ("die AI ist die einzige
schreibende Instanz") nicht mehr wörtlich. Das Modell dahinter steht in
[ARCHITECTURE.md](../../ARCHITECTURE.md#10-team-variante-wenn-abschnitt-1-nicht-mehr-wörtlich-gilt),
hier stehen die Schreibregeln.

## Herkunft und Vertrauen im Frontmatter

Feldnamen nach dem Open Knowledge Format, damit der Vault an einen Standard anschließt statt
an eine Hauserfindung. Alle Felder sind optional, aber `generated` gehört in jede neue Notiz.

| Feld | Form | Wofür |
|---|---|---|
| `generated` | `{ by: <actor>, at: YYYY-MM-DD }` | Wer hat den Inhalt erzeugt und wann zuletzt inhaltlich geändert |
| `verified` | Liste von `{ by: <actor>, at: YYYY-MM-DD }` | Jede unabhängige Bestätigung ein Eintrag, nicht überschreiben |
| `sources` | Liste von `{ resource: <URL/Pfad>, author: <actor>, last_modified: YYYY-MM-DD }` | Woraus abgeleitet: Handbuch-Kapitel, Code-Datei, Gespräch |
| `stale_after` | `YYYY-MM-DD` | Ab wann gilt der Inhalt als nachprüfbedürftig |

**Actor-Schreibweise:** `human:<kürzel>` für Personen, `<tool>/<version>` für Agenten (z.B.
`claude/opus-5`), `process:<name>` für automatisierte Läufe. Das `human:`-Präfix ist das
eigentliche Signal: Daraus liest sich ab, ob eine Aussage nur maschinell entstanden oder von
einem Menschen abgenommen ist.

Daraus ergeben sich drei Vertrauensstufen, ohne dass jemand sie pflegen muss: kein
`verified` heißt unbestätigt, `verified` nur von Nicht-`human:`-Akteuren heißt maschinell
bestätigt, ein `human:`-Eintrag heißt von einer Person abgenommen. **Nur die letzte Stufe
ist vor automatischer Bereinigung sicher.**

## Wer schreibt was

- **Der Normalfall bleibt: schreiben über die AI.** Sie hält die Konventionen ein, ein Mensch
  im Direktzugriff tut das erfahrungsgemäß nicht durchgehend.
- **Wer doch direkt tippt, hält vier Dinge ein:** Frontmatter vollständig, `generated.by` auf
  den eigenen `human:`-Namen, Links mit Kontext-Halbsatz, keine Statusinformationen im
  Wissen. Alles Weitere darf die AI im nächsten Durchlauf glattziehen.
- **Aktualisieren statt duplizieren.** Vor jeder neuen Notiz prüfen, ob das Thema schon eine
  hat. Zwei Notizen zum selben Gegenstand sind im Team der häufigste Verfall, weil beide
  Autoren jeweils ihre pflegen.
- **Widersprüche ansprechen, nicht überschreiben.** Steht in einer Notiz etwas anderes als
  gerade berichtet wird, ist das eine Rückfrage wert, bevor der alte Stand verschwindet. Er
  kann richtig sein und die neue Aussage die Ausnahme. Bei bestätigtem Widerspruch die alte
  Aussage ersetzen und `verified` zurücksetzen, nicht beide Fassungen nebeneinander stehen
  lassen.
- **Quelle nennen, wenn Wissen aus einem Gespräch stammt:** ein Halbsatz im Text ("laut
  <Person>, <Datum>") zusätzlich zum `sources`-Eintrag. Im Team ist die Frage "wer sagt das"
  Teil der Aussage.

## Was NICHT hineingehört

- **Kein Push-Wissen.** Generelle Arbeitsanweisungen gehören in die Kontextdatei, nicht in
  den Vault, siehe [ARCHITECTURE.md](../../ARCHITECTURE.md#12-pull-wissen-ja-push-wissen-nein).
- **Keine personenbezogenen Daten.** In einem geteilten Vault gilt das strenger als solo:
  keine Einschätzungen über Kollegen, keine Kundendaten, keine privaten Details. Fachliche
  Zuständigkeiten ("<Person> kennt das Abrechnungsmodul") sind in Ordnung, Bewertungen nicht.
- **Keine Links in ein privates Vault und zurück.** Ein Team-Vault und ein persönliches
  Brain gehören verschiedenen Leuten und werden getrennt gepflegt. Querlinks brechen still,
  sobald einer der beiden umzieht, und niemand sieht es. Doppelt gebrauchtes Wissen wird an
  beiden Orten geschrieben, das ist billiger als eine Verbindung, die niemand prüfen kann.

## Wenn der Vault zu groß für eine flache Ablage wird

Der Wissens-Ordner startet flach, und das trägt erstaunlich lange: Glob und Grep interessiert
keine Ordnertiefe, und jede Struktur ist eine Entscheidung, die später jemand pflegen muss.
Irgendwann kippt es trotzdem, meist wenn sich klar getrennte Fachbereiche gebildet haben, die
kaum aufeinander verweisen.

Dann gilt:

- **Unterordner nach Fachbereich, nicht nach Notiztyp.** `Wissen/Abrechnung/` ist nützlich,
  `Wissen/Konzepte/` nicht, dafür gibt es `type`.
- **Alles bleibt trotzdem im Index und in einer MOC.** Der Ordner ist Ablage, die Landkarte
  bleibt die Navigation. Eine Notiz, die nur noch über ihren Pfad zu finden ist, ist aus der
  Navigation gefallen, und `brain-check.py` meldet das auch so.
- **Die Links ziehen mit.** Sie sind bundle-relativ ab Vault-Root, ein Verschieben bricht
  also jeden Verweis darauf. Beim Umsortieren einmal per Grep über den alten Pfad gehen und
  alle Fundstellen umbiegen, danach `brain-check.py` laufen lassen.
- **`WISSEN_FOLDER` in `brain-check.py` bleibt der Wurzelordner**, die Prüfungen greifen dann
  weiter über alle Unterordner.

## Glossar

Ein Team-Vault braucht eine Begriffsliste, ein Solo-Vault meistens nicht: Was einem allein
selbstverständlich ist, ist für neue Leute (und für die AI) genau die Hürde. `Glossar.md`
im Wissens-Ordner, eine Zeile pro Begriff, aus `Vorlagen/Glossar.md`. Ein Begriff kommt
hinein, sobald er in einer Notiz auftaucht, ohne dass er dort erklärt wird. Wird ein Eintrag
so lang, dass er die Zeile sprengt, wird er eine eigene Notiz, auf die das Glossar zeigt.
