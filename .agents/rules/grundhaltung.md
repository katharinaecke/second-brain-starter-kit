# Grundhaltung

> Teil der Vault-Schreibkonventionen (`.agents/rules/`, Übersicht in `AGENTS.md`). Nur laden, wenn Vault-Inhalte **angelegt oder editiert** werden.

- **Die AI ist die einzige schreibende Instanz.** Der Mensch schreibt nichts selbst hinein, er liest über die AI. Alle Regeln hier sind **Pflicht der AI**, nie eine Bitte an den Menschen ("du solltest X so schreiben" ist sinnlos, die AI schreibt X selbst korrekt).
- **Abweichungen sofort und vollständig korrigieren, ohne nachzufragen.** Datei anpassen, alle Backlinks umbiegen, gegenprüfen, dass nichts auf den alten Stand zeigt. Vault-Dateioperationen (inkl. Löschen/Umbenennen) sind dabei erlaubt, das ist Vault-Pflege, keine destruktive Aktion im Sinne von Code-Deploy oder `git push`.
- **Beim Umbau eines Vorgehens reicht die Markdown-Suche nicht.** Auch `Skripte/*`, `.agents/skills/*/SKILL.md`, `Vorlagen/` und `index.md` auf Referenzen zur alten Regel prüfen.
- **Maßstab ist Context-Engineering-Effizienz, nicht Sammelmenge.** Wenige gelesene Notizen sollen guten Kontext liefern. Dafür stehen die MOCs als lesbare Landkarten, das `type`-Feld trennt Lernstoff von Nachschlagewissen, kontextualisierte Links ersetzen nackte Listen. Link-Dichte kostet trotzdem: nicht der Link selbst, aber sein Kontext-Halbsatz wird jedes Mal mitgelesen. Lieber wenige tragende als viele vollständige.
