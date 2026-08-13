# Links

> Teil der Vault-Schreibkonventionen (`.agents/rules/`, Übersicht in `AGENTS.md`). Nur laden, wenn Vault-Inhalte **angelegt oder editiert** werden.

- **Standard-Markdown, keine Wikilinks:** `[Text](</Wissen/X.md>)`, bundle-relativer Pfad (führendes `/` ab Vault-Root), in spitze Klammern gewrappt (Dateinamen enthalten oft Leerzeichen). Als Linktext den Notiztitel, nicht den Pfad. Grund: funktioniert auch außerhalb von Obsidian (GitHub-Preview, jeder Markdown-Reader), reine Obsidian-Wikilinks tun das nicht.
- **Nie in Backticks.** Ein Link im Code-Span erzeugt keine Graph-Verbindung. Tote Links sind dagegen harmlos.
- **Jeder Link braucht einen Kontext-Halbsatz**, mit Doppelpunkt angehängt: `[X](</Wissen/X.md>): warum die Verbindung relevant ist`. Eine kontextlose "see also"-Liste verwässert das Netz. Lieber 3 erklärte als 9 nackte Links. (Kein Gedankenstrich als Trenner, siehe Typografie-Regel in `.agents/rules/sprache-und-dateinamen.md`.)
- **4 bis 8 Links pro `## Verwandt` als Orientierung**, der Qualität nachgeordnet, nicht auf die Zahl auffüllen. Harte Grenzen: unter 2 = isolierte Notiz (selten richtig), über 10 = Stern-Hub (vermeiden).
- **In beide Richtungen verlinken, wenn tragend:** verweist A auf B und die Verbindung ist auch aus B-Sicht wichtig, ergänzt B einen eigenen Link zurück zu A. Sonst genügt der automatische Backlink.
- **Mindmap-Stil, kein Hub-Stil:** Querverbindungen direkt zwischen Notizen, nicht alles über den Index.
