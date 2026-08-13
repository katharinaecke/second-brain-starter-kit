---
tags: [pkm, second-brain, vault-pflege]
themengebiet: prozess
type: Vorgehen
description: Schema für den mechanischen Gesundheitscheck über den ganzen Vault (brain-check.py) samt Triage des Reports, plus periodischer Tiefen-Modus.
---

# Brain-Optimieren-Vorgehen (Vault-Gesundheitscheck)

> **Auslöser:** "Brain optimieren", "Vault-Check", "Brain aufräumen", "großer Brain-Review",
> "ist mein Brain noch effektiv" o.ä. → **immer zuerst kurz fragen, welcher Modus**
> gewünscht ist, statt an der Formulierung zu raten: (1) **Standard** (mechanischer Check,
> günstig) oder (2) **Standard plus Tiefen-Modus** (zusätzlich Nutzung/Redundanz/
> Architektur-Fit/Datenschutz-Rollup, aufwendiger, nur periodisch vorgesehen). Auch bei
> "großer Brain-Review" nicht automatisch in den Tiefen-Modus wechseln, das ist nur ein
> Indiz, keine Zusage.

## Was ist das?

Ein **mechanischer Gesundheitscheck** über den ganzen Vault: kaputte Links, isolierte
Notizen, fehlendes Frontmatter, fehlende `## Verwandt`-Abschnitte, MOC-Abdeckung, zu große
Notizen, Namenskonventionen. Das Skript findet die Treffer, **das Urteil (fixen/löschen/lassen)
macht die AI** anhand des Reports. Das ist der **Standard-Modus**. Der **Tiefen-Modus**
ergänzt das seltener um Fragen, die Mechanik allein nicht beantworten kann.

## Wie funktioniert's?

0. **Modus abfragen** (s. Auslöser oben). Erst nach Antwort weitermachen.
1. **Report holen:** `Skripte/brain-check.py` laufen lassen (Python 3, portabel). `--summary`
   für nur Zählungen, ohne Flag der volle Report mit Trefferlisten.
2. **Triagieren**, Kategorie für Kategorie durchgehen:
   - **Kaputte/verdächtige Links** → echte Tippfehler fixen. **Bewusste Zukunfts-Notizen**
     (noch nicht geschriebene, aber absichtlich schon verlinkte Notizen) lassen.
   - **Backtick-Links** → Backticks entfernen (entwerten den Graph-Link).
   - **Isolierte Notizen (<2 Links)** → Querlinks ergänzen, außer bewusst isoliert
     dokumentiert.
   - **Wissen ohne Frontmatter / ohne `## Verwandt` / nicht in MOC** → ergänzen. Karten
     entstehen dagegen **nicht** hier, sondern über Brain-Input und Brain-Bereinigen (siehe
     `.agents/rules/karteikarten.md`), dieser Check fragt sie bewusst nicht ab.
   - **Links mit Case-Fehler** → immer fixen. Sie funktionieren auf Windows/macOS und brechen
     auf Linux; das ist nie Absicht, anders als ein bewusst toter Zukunfts-Link.
   - **Kaputte Kodierung (kein UTF-8)** → immer fixen, und zwar vor allem anderen. Die Datei
     wurde ersatzweise gelesen, ihre Umlaute stehen also schon im Vault falsch, und jeder
     weitere Edit schreibt den Schaden fest. Datei neu als UTF-8 speichern, danach die
     betroffenen Stellen im Text gegenlesen. Ohne diesen Schritt hätte der Sweep hier
     abgebrochen, statt zu melden.
   - **Skill-Drift** → die gemeldete Stelle angleichen (`Skripte/skills-check.py` zeigt
     Details). Die Auslöser in `AGENTS.md` sind für Tools ohne Skill-Mechanik die einzige
     Quelle, eine fehlende Phrase heißt dort "Skill nicht auslösbar", ohne Fehlermeldung.
   - **Große Notizen** → prüfen, ob splitten/kürzen sinnvoll. Kein Automatismus.
   - **Ohne Datenschutz-Klassifizierung** *(nur falls genutzt)* → hier **nicht** selbst
     klassifizieren (braucht Einzelfall-Urteil), sondern als Fortschritts-Fakt zeigen und an
     die F5-Frage in [Brain-Bereinigen-Vorgehen](</.agents/skills/brain-bereinigen/SKILL.md>)
     weiterreichen.
   - **Fehlende Rücklinks in `## Verwandt`** → **nicht** in einem Lauf bulk-fixen (zu groß,
     zu viel Fließband-Risiko). Zahl als Fortschritts-Fakt zeigen, opportunistisch mitziehen,
     wenn ohnehin schon an einer betroffenen Notiz gearbeitet wird.
3. **Umsetzen** und am Ende kurz bilanzieren, was gefixt und was bewusst gelassen wurde.
4. **Brain-Skills-Konsistenz-Check** (jeder Lauf, kurz und günstig): die eng verzahnten
   Vault-Pflege-Vorgehen selbst gegenlesen, also `brain-optimieren`, `brain-bereinigen`,
   `brain-input`, `merk-dir-das`. Verweisen sie dort, wo es inhaltlich hingehört,
   tatsächlich aufeinander? Stimmen die Auslöser-Kopfzeilen noch mit der `AGENTS.md`-Tabelle
   überein? Das ist **nicht** dasselbe wie ein Review aller Skills, die fachlichen Skills
   bleiben Sache der rotierenden Brain-Bereinigen-Routine.

## Tiefen-Modus (periodisch oder auf Zuruf)

Der Standard-Modus ist rein mechanisch. Der Tiefen-Modus stellt die Frage: nicht nur "ist
der Vault sauber", sondern **"dient er noch seinem Zweck, wird er wirklich genutzt"**. Läuft
seltener, die Fragen brauchen Urteilsvermögen, keine Mechanik.

Vier zusätzliche Dimensionen:
1. **Nutzungscheck:** Welche `type: Konzept`-Notizen wurden lange nicht abgefragt, obwohl
   fällig (falls Lernrunde genutzt wird)? Welche Wissens-Notizen werden aus keinem aktiven
   Arbeitskontext heraus verlinkt (Indiz: nie im echten Arbeitskontext gebraucht)?
2. **Redundanz:** Notizen mit starker Tag- oder Themen-Überlappung und ähnlichem Titel als
   Kandidaten listen, Zusammenführen prüfen, nicht automatisch mergen.
3. **Architektur-Fit:** Wächst die MOC-Struktur noch sinnvoll mit? Braucht ein Themengebiet
   eine Untergliederung (große Cluster in eigene Sub-MOCs auslagern, Ursprungs-MOC bleibt
   Dach-Hub)?
4. **Datenschutz-Rollup** *(nur falls genutzt)*: Sammel-Blick über die F5-Antworten seit dem
   letzten Review, welche Kunden- oder Personendaten sind noch aktiv nötig, welche reif fürs
   Entfernen?

Ergebnis bleibt eine Faktenliste plus Einschätzung, keine automatische Aktion, gleiche
Grundhaltung wie im Standard-Modus.

## Stolpersteine

- **Nicht blind "fixen".** Tote Links sind in vielen Markdown-Renderern (z.B. Obsidian)
  harmlos und teils Absicht (Zukunfts-Notizen). Erst Kontext prüfen.
- Der Report ist eine Faktenliste, kein Befehl, die AI urteilt.

## Verwandt

- [Brain-Input-Vorgehen](</.agents/skills/brain-input/SKILL.md>): die laufende Pflege,
  dieser Check ist der periodische Tiefenputz
- [Brain-Bereinigen-Vorgehen](</.agents/skills/brain-bereinigen/SKILL.md>): liefert die
  F5-Einzelbewertungen, die der Tiefen-Modus hier zum Rollup zusammenzieht
- [Merk-Dir-Das-Vorgehen](</.agents/skills/merk-dir-das/SKILL.md>): gehört zur Gruppe, die
  Schritt 4 im Konsistenz-Check gegenliest
- [AGENTS](</AGENTS.md>): die Vault-Konventionen, gegen die hier geprüft wird
