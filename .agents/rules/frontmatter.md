# Frontmatter

> Teil der Vault-Schreibkonventionen (`.agents/rules/`, Übersicht in `AGENTS.md`). Nur laden, wenn Vault-Inhalte **angelegt oder editiert** werden.

Diese Felder gehören in **jede neu angelegte Notiz**, also in alles, was Vault-Inhalt ist,
einschließlich der Skill-Dateien unter `.agents/skills/` und `.agents/knowledge/`.

**Ausgenommen:** die Regeldateien in `.agents/rules/` selbst (also auch diese hier), `AGENTS.md`,
`README.md` und `ARCHITECTURE.md`. Das sind Konventions- und Meta-Dokumente, keine Notizen.
Sie werden nicht gegreppt, sortiert oder abgefragt, und ein `type:` darauf wäre eine Angabe
ohne Abnehmer.

| Feld | Wo | Werte / Regel |
|---|---|---|
| `type` | überall | `Konzept` / `Referenz` / `Vorgehen` + je nach gewählten Ordnern eigene Typen (z.B. `Vorgang`, `Person`, `Projekt`, `MOC`, `Quelle`, `Log` für den Kartenstapel), Großschreibung, kein Default. Für jeden davon liegt eine Vorlage in `Vorlagen/` |
| `description` | überall | Ein Satz, was die Notiz ist/löst. Macht `Grep: pattern="^description:"` über einen Ordner zur Kurzübersicht, ohne jede Datei zu öffnen |
| `tags`, `themengebiet` | Wissens-Ordner | genau ein `themengebiet`, damit Grep/Dataview funktionieren |

**Felder immer mit Wert füllen, nicht leer stehen lassen.** Ein Feldname ohne Wert sieht im
Editor nach "erledigt" aus, trägt aber keine Information; `brain-check.py` wertet ihn
korrekt als fehlend und meldet die Notiz. Kommentare hinter dem Wert (`# ...`) sind erlaubt,
sie gehören nicht zum Wert.

## `sichtbarkeit`: Datenschutz-Klassifizierung *(nur relevant, wenn im Setup gewählt, sonst diesen Abschnitt löschen)*

Macht den Demo-Vault-Bau für Vorträge/Portfolio mechanisch statt manuell redigiert.

| Wert | Bedeutung |
|---|---|
| `oeffentlich-zeigbar` | unbedenklich für externe Demos/Portfolio (generisches Wissen ohne Kunden- oder Personenbezug) |
| `intern` | intern okay, nicht für externe Demos (Org-Wissen, interne Praktiken/Tools) |
| `vertraulich` | Kunden- und Personendaten, alles Sensible, **niemals** in einen Demo-Vault |
| *(optional weitere Werte)* | z.B. eine eigene Achse für private/berufsfremde Themen, siehe [ARCHITECTURE.md](../../ARCHITECTURE.md#8-fail-closed-bei-sensiblem) |

- **Fail closed:** fehlt das Feld oder steht es leer, gilt die Notiz als `vertraulich`, bis explizit klassifiziert.
- Neue Notizen bekommen das Feld **beim Anlegen**, kein Nachzieh-Rückstand.
