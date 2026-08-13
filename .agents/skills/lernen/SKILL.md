---
tags: [lernen, spaced-repetition]
themengebiet: prozess
type: Vorgehen
description: Schema der Spaced-Repetition-Runde (Leitner-Boxen), rund 10 fällige Karten nacheinander abfragen und den Lernstand fortschreiben. Optionales Modul.
---

# Lernkarten-Vorgehen (Spaced Repetition)

> **Auslöser:** "Lernen", "Karteikarten", "frag mich ab", "Quiz", "Lernrunde" o.ä., dieses
> Schema befolgen, ohne Rückfrage. In Claude Code zusätzlich als `/lernen`-Skill.
>
> **Optionales Modul**, nur relevant, wenn beim Setup aktives Lernen gewünscht wurde.
> Sonst diesen Skill-Ordner löschen (samt `.claude/skills/lernen/` und `Vorlagen/Karten.md`).

## Was ist das?
Eine regelmäßige **Spaced-Repetition-Runde** (Karteikarten): Die AI fragt rund 10 Fragen ab,
**eine nach der anderen**, und merkt sich pro Frage, wie gut sie saß. Schwieriges kommt oft
wieder, Gesessenes seltener.

## Warum brauche ich das?
Der Vault sammelt Wissen, aber Sammeln ist nicht Können. Spaced Repetition (Leitner-Boxen)
sorgt dafür, dass jede Frage genau dann wiederkommt, wenn sie zu verblassen droht.

## Aufnahmekriterium: was überhaupt eine Karte wird
Die wichtigste Regel: **nur was aus dem Kopf gekonnt werden muss** (Daily, Review,
Gespräch) wird eine Karte. Was **nachgeschlagen** werden kann, bleibt reines Vault-Wissen
ohne Karte. Das meiste Wissen ist Nachschlage-Wissen. Karten entstehen **bewusst** an zwei
Stellen, nie automatisch:
- **Brain-Input**, beim Sichern von Neuem: "muss ich das im Kopf haben?" Ja → 1-2 Karten.
- **Brain-Bereinigen**, beim Durchgehen einer Notiz: fehlt eine Karte für Kern-Können? Ist
  eine vorhandene schlecht? → vorschlagen / nachschärfen / streichen.

## Grundprinzip: Leitner-Boxen
Jede Karte hat eine **Box (1 bis 6)**, die bestimmt, wann sie wieder fällig wird:

| Box | nächste Wiederholung |
|-----|----------------------|
| 1   | +1 Tag |
| 2   | +2 Tage |
| 3   | +4 Tage |
| 4   | +7 Tage |
| 5   | +15 Tage |
| 6   | +30 Tage (gemeistert) |

- **Richtig** → Karte steigt eine Box hoch (max 6), nächste Fälligkeit nach dem neuen Intervall.
- **Falsch oder nur teilweise** → zurück auf **Box 1**, kommt morgen wieder.
- **Neue Karte** → startet in Box 1.

## Wo liegt was
- **Karten und Lernstand:** `Lernen/Karten.md` im Vault (entsteht beim Setup aus
  `Vorlagen/Karten.md`; der Ordnername kann abweichen), **eine** Datei, eine
  Tabellenzeile pro Karte: `ID | Frage | Antwort | Box | Fällig | Historie | Quelle`. Frage,
  Antwort und Lernstand stehen zusammen, damit eine Lernrunde mit **einem** Read auskommt.
  `Quelle` verlinkt die Herkunfts-Notiz für Vertiefung.
- **Keine Quiz-Blöcke in den Wissens-Notizen**, Karten leben ausschließlich zentral in
  `Karten.md`. Wer eine Karte anlegt, schreibt sie dorthin (mit Link zur Notiz), nicht in
  die Notiz.

## Wie funktioniert's? (die Runde)

1. **Heutiges Datum bestimmen.**
2. **Fällige Karten holen:** `Lernen/Karten.md` lesen (ein Read
   genügt). Fällig = alle Karten mit `Fällig ≤ heute`, sortiert nach niedrigster Box zuerst.
3. **Auf rund 10 Karten auffüllen** (Zielanzahl anpassbar). Sind 10 oder mehr fällig: die 10
   dringendsten, Rest bleibt für morgen. Weniger als 10 fällig: mit neuen Karten auffüllen
   (max rund 6 neue pro Tag). Ist der Stapel fast leer, bei einem frischen Vault der
   Normalzustand, keine Fragen erfinden: kurz erwähnen, dass neue Karten über
   Brain-Input/Bereinigen entstehen, und die vorhandenen abfragen.
4. **Abfragen, eine Karte nach der anderen:**
   1. Nur die Frage stellen (Antwort NICHT zeigen).
   2. Auf Antwort warten.
   3. **Wohlwollend bewerten** gegen die Musterantwort: Kernaussage getroffen = richtig,
      wichtiges Detail fehlt = teilweise, daneben = falsch.
   4. Kurzes Feedback plus Musterantwort zeigen.
   5. Box aktualisieren.
5. **Karten nachschärfen:** sitzt eine Karte zweimal in Folge nicht (`✗✗` bzw. `✗~`/`~✗` am
   Ende der Historie), ist sie ein Kandidat für ein Formulierungsproblem, nicht nur
   fehlendes Wissen. Dann Frage und Antwort überarbeiten statt sie nur wieder vorzulegen.
6. **Karten.md fortschreiben.**
7. **Abschluss:** kurze Bilanz, wie viele richtig, was morgen wiederkommt.

## Stolpersteine
- **Nicht die Antwort mitliefern.** Erst fragen, tippen lassen, DANN auflösen.
- **Wohlwollend, nicht pingelig.** Es geht ums Verstehen, nicht um Wortgleichheit.
- **Zeitdeckel respektieren.** Lieber 10 Karten sauber als 30 gehetzt.
- **Neue Karten nur nach Kriterium** (im Kopf können, nicht nachschlagen) und begrenzt pro Tag.
- **Stale Karten reparieren:** zeigt die `Quelle` einer Karte auf eine gelöschte oder
  umbenannte Notiz → Link korrigieren oder Karte entfernen.
- **`|` in Frage/Antwort escapen** (`\|`), sonst bricht die Tabelle.

## Verwandt
- [Karten-Vorlage](</Vorlagen/Karten.md>): der Stapel selbst (Frage/Antwort/Lernstand), aus
  dem hier abgefragt wird; liegt im fertigen Vault als `Lernen/Karten.md`
- [Brain-Input-Vorgehen](</.agents/skills/brain-input/SKILL.md>): legt neue Karten an (das
  Tor beim Reinkommen)
- [Brain-Bereinigen-Vorgehen](</.agents/skills/brain-bereinigen/SKILL.md>): Qualitätswächter,
  findet fehlende, schärft und streicht schlechte Karten
