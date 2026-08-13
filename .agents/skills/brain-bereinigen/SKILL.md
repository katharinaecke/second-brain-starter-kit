---
tags: [pkm, second-brain, vault-pflege]
themengebiet: prozess
type: Vorgehen
description: Schema für die rotierende Tiefenprüfung, eine Datei pro Durchlauf auf Aktualität, Relevanz, Kürzbarkeit und Frontmatter abklopfen.
letzte-bereinigung:
---

# Brain täglich bereinigen: Vorgehen

> **Auslöser:** "Brain bereinigen", "tägliche Bereinigung", "Brain-Note prüfen" o.ä. →
> dieses Schema befolgen. In Claude Code zusätzlich als `/brain-bereinigen`-Skill.

## Wozu

Alle Notizen im Vault, die Skill-Dateien und ggf. Memory-Dateien können veralten. Eine
Datei pro Durchlauf prüfen hält die Sammlung scharf: überholte Inhalte raus, ungenaue
korrigieren, kürzen wo möglich, Frontmatter vervollständigen.

**Skills gehören dazu, weil sie hartcodierte Pfade auf Vault-Notizen halten.** Bei einer
Vault-Reorganisation ziehen die nicht automatisch mit.

**Bei einem frischen Vault** findet die Routine meist nichts. "Keine Datei fällig, alles
aktuell" ist ein normales Ergebnis, kein Zeichen, dass sie überflüssig ist. Ihr Wert zeigt
sich über Monate: sie fängt Drift (veraltete Fakten, verwaiste Pfade, Rollenwechsel), sobald
er entsteht, statt erst dann, wenn ein Review-Zyklus schon untragbar geworden ist.

## Tracking

Jede bereinigte Datei bekommt ein Frontmatter-Feld `letzte-bereinigung: YYYY-MM-DD`. Keine
separate Queue-Datei nötig, die nächste Datei wird per Glob und Grep ermittelt.

## Scope

- **Vault:** alle Content-Ordner (Wissen, abgeschlossene Arbeitseinheiten, Personen,
  Projekte, MOCs, Meetings, Ressourcen, je nachdem, welche existieren) plus
  `.agents/skills/`, `.agents/knowledge/`, `.agents/rules/` und `AGENTS.md`. Die letzten
  beiden driften zuerst, wenn eine Konvention sich ändert. Sie tragen kein Frontmatter,
  können also kein `letzte-bereinigung` bekommen: sie kommen dran, wenn gerade eine Regel
  geändert wurde oder der Durchlauf einmal herum ist.
- **Skill-Dateien im Agenten-Tool** (z.B. `~/.claude/skills/*/SKILL.md`), falls es
  Shortcuts auf Vault-Pfade gibt. Schwerpunkt: existieren die referenzierten Pfade noch?
- **Ausgenommen:** `Vorlagen/` (Templates, kein Inhalt), `Skripte/` und `Lernen/` (haben
  jeweils eine eigene Routine)

## Ablauf

### Schritt 0: Tagespensum

**1 Datei pro Durchlauf.** Jede Datei durchläuft alle Schritte unten einzeln, keine
Sammel-Abarbeitung ohne Rückfrage.

### Schritt 1: Nächste Datei ermitteln

1. Glob alle `.md` über alle Scope-Ordner
2. Grep nach `^letzte-bereinigung:` → liefert alle schon geprüften Dateien mit Datum
3. Dateien **ohne** `letzte-bereinigung` = noch nie geprüft (höchste Priorität)
4. Wähle: ältestes Datum zuerst; noch nie geprüft schlägt jedes echte Datum; bei
   Gleichstand alphabetisch. Die frontmatterlosen Dateien aus dem Scope (`.agents/rules/*`,
   `AGENTS.md`) bleiben hier außen vor, sie stünden sonst dauerhaft als "noch nie geprüft"
   vorn und die Warteschlange käme nie voran.

**Sofort-Trigger (springt vor jede Warteschlange):**
- Eine Person, mit der zusammengearbeitet wurde, ist aus dem Bild raus (Firmenwechsel o.ä.)
  → ihre Personen-Notiz sofort prüfen, nicht auf die Zufallsreihenfolge warten. Faktische
  und berufliche Reste dürfen als Institutionswissen bleiben, rein persönliche oder
  wertende Einschätzungen ohne fortlaufenden Zweck kommen raus.
- Eine Person bittet aktiv um Löschung ihrer Daten → hart löschen, unabhängig vom
  History-Wert. Übersticht jede "ist doch Historie"-Abwägung.

### Schritt 2: Datei vorlegen

- **Vollständigen Inhalt der Datei wortwörtlich ausgeben**, den kompletten Dateitext als
  eigenen Text- oder Codeblock in der Chat-Antwort zeigen, keine Zusammenfassung. Reicht
  nicht: nur auf das Tool-Ergebnis verweisen.
- Zugehörigen MOC-Eintrag zeigen (falls vorhanden)
- Alter der Notiz nennen (`erstellt:` oder letztes Änderungsdatum)
- **Kontext kurz verifizieren:** genannte Dateipfade, Tools, Repos kurz prüfen (Glob/Read),
  ob sie noch existieren und das beschriebene Verfahren noch aktuell ist

### Schritt 3: Prüfung, gemeinsam

Jede Frage einzeln stellen, auf Antwort warten. **Grundhaltung: ein gutes Brain wird aktiv
verschlankt.** Unnötiges und Ineffektives konsequent angehen statt aus Bequemlichkeit stehen
lassen. Arbeitsaufwand (mehrere Backlinks umbiegen) ist kein Gegenargument gegen eine an
sich richtige Löschung oder Kürzung.

**F1: Wird diese Datei noch gebraucht?**
- Nein → **vor dem Löschen** per Grep den exakten Dateinamen über den ganzen Vault suchen.
  Backlinks verstecken sich oft in Tabellen oder fremden Notizen, die nicht offensichtlich
  zugehörig wirken. Dann löschen und alle gefundenen Links auf Plaintext umbiegen.
- **Löschen oder archivieren, und die Löschung nie stillschweigend.** Beides wird
  vorgeschlagen und bestätigt, nie einfach ausgeführt: Der Mensch sieht den vollständigen
  Inhalt (Schritt 2) und entscheidet. Reiner Ballast wird gelöscht; was niemand mehr braucht,
  aber auch niemand wegwerfen will, wandert nach `.agents/rules/ablage.md` ins
  `<Thema>-Archiv.md`. Im Zweifel
  archivieren statt löschen, **außer** es gibt kein Backup des Vaults; dann ist jede
  Löschung endgültig und verdient die härtere Rückfrage. Ob ein Backup existiert, steht
  nicht im Vault: einmal nachfragen statt annehmen.
- Bei Rollen- oder Themenwechsel auch strukturelle Doku prüfen, nicht nur einzelne Notizen.
  `AGENTS.md`, `index.md` und Vorlagen können noch auf einen veralteten Bereich verweisen,
  lange nachdem die Einzelnotizen dazu schon ausgemustert wurden.
- **Vorsicht bei "viele Backlinks" als Gegenargument:** Anzahl allein rechtfertigt keinen
  Verbleib. Prüfen, ob die Backlinks das Ziel als eigenständigen Inhalt brauchen, oder es
  nur als Quellenverweis zitieren, während der Fakt längst in der zitierenden Notiz steht.
- Unklar → gemeinsam einschätzen. Ja → weiter mit F2.

**F2: Sollte sie gekürzt werden?**
- Was kann weg, ohne Präzision zu verlieren? Vorschlag zeigen, auf OK warten, dann kürzen.

**F3: Stimmt der Inhalt noch?**
- Pfadangaben kurz verifizieren (Glob/Read), gegen aktuell gelebte Praxis prüfen.
- Bei MOCs zusätzlich ein Vollständigkeits-Check: alle Wissens-Notizen mit passendem
  `themengebiet` per Grep sammeln und gegen die in der MOC verlinkten Notizen abgleichen.
- **Persönliche Interaktionsclaims aktiv hinterfragen, nicht nur Pfade und Tools
  verifizieren.** Eine einzelne halluzinierende Session kann dieselbe erfundene Interaktion
  (Gespräch, Mail, Zitat) gleichzeitig in mehrere Dateien schreiben. Cross-Referenzierung
  über mehrere Notizen ist **kein** Beweis für Wahrheit. Bei Behauptungen über persönliche
  Gespräche oder Mails mit konkret genannten Personen aktiv nachfragen "stimmt das
  wirklich?", statt die Häufung an Cross-Links selbst als Bestätigung zu werten.

**F3b: Ist das Frontmatter vollständig?**
- `tags:`, `themengebiet:`, `type:`, `description:` vorhanden und korrekt?
- Falls Datenschutz-Klassifizierung genutzt wird: `sichtbarkeit:` gesetzt?
- Skill-Dateien: `name:`, `description:` noch korrekt (Auslöse-Phrasen aktuell)?
- Bei Wissens-Notizen: `type` korrekt? *(nur falls Lernen aktiv)* Testet die Notiz
  Kern-Können, gibt es dazu aber noch keine Karte in `Lernen/Karten.md` (per `Quelle`-Link
  auf diese Notiz)? → eine gute Karte vorschlagen. Zeigt eine bestehende Karte ein
  Formulierungsproblem? → umformulieren oder streichen.

**F4: Kann man eine neue oder schärfere Regel ableiten?**
- Nur wenn das Review ein Pattern sichtbar macht, das noch keine eigene Regel hat.
- Wenn nichts Neues: kurz "keine neue Regel nötig" sagen.

**F5: Datenschutz-Klassifizierung** *(nur falls genutzt)*
- Personen-Notiz: Besteht die Zusammenarbeit noch? Enthält sie mehr als Rolle und faktische
  Zusammenarbeit, also wertende Charaktereinschätzungen, Privates, sensible Kategorien? Das
  kommt raus, unabhängig davon, ob der Kontakt noch besteht.
- Kunden- und Projektinhalt: wird das noch aktiv gebraucht, oder ist es reines
  Abschlusswissen? Bei generischem Wissen mit nur zufälligem Bezug: Bezug entkoppeln,
  fachlichen Kern behalten.
- Am Ende immer `sichtbarkeit:` setzen oder bestätigen.

### Schritt 4: Stempeln

`letzte-bereinigung: YYYY-MM-DD` in das Frontmatter der geprüften Datei schreiben.

### Schritt 5: Keine offenen Todo-Checkboxen stehen lassen *(nur falls Todos extern leben)*

Findet die Bereinigung eine offene `- [ ]`-Zeile: sofort behandeln wie in
`.agents/rules/ablage.md` beschrieben.

## Verwandt

- [Brain-Optimieren-Vorgehen](</.agents/skills/brain-optimieren/SKILL.md>): der
  periodische Tiefenputz (mechanischer Check plus Tiefen-Modus); dessen Tiefen-Modus zieht
  die F5-Antworten von hier zu einem Sammel-Rollup zusammen
- [Brain-Input-Vorgehen](</.agents/skills/brain-input/SKILL.md>): die laufende Pflege am
  Ende eines Chats, ergänzt diese Routine
- [Merk-Dir-Das-Vorgehen](</.agents/skills/merk-dir-das/SKILL.md>): gezieltes
  Einzel-Festhalten einer Info
