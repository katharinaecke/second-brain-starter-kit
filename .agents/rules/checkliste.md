# Checkliste beim Anlegen

> Teil der Vault-Schreibkonventionen (`.agents/rules/`, Übersicht in `AGENTS.md`). Nur laden, wenn Vault-Inhalte **angelegt oder editiert** werden.

1. Mit der passenden `Vorlagen/`-Datei starten, Frontmatter vollständig ausfüllen (jedes Feld mit Wert, siehe `.agents/rules/frontmatter.md`).
2. Vor `## Verwandt` aktiv nach verwandten Notizen greppen: gleiches `themengebiet` (1-3 nächste), gleiche Tags, inhaltliche Brücke in ein anderes Themengebiet.
3. Links mit Kontext-Halbsatz setzen, Rücklinks ergänzen (siehe `.agents/rules/links.md`).
4. *(nur falls Lernen aktiv)* Verdient die Notiz eine Karte? → in `Lernen/Karten.md`, nicht in die Notiz (siehe `.agents/rules/karteikarten.md`).
5. Neue Wissens-Notiz in die passende `MOCs/<Themengebiet>.md` einhängen, mit einer Halbzeile was sie bringt. MOCs sind handkuratiert und veralten sonst.
6. `index.md` **nicht** manuell ergänzen, Dataview-Queries (falls genutzt) aktualisieren sich selbst.
