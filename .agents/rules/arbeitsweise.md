# Arbeitsweise

> Teil der Vault-Schreibkonventionen (`.agents/rules/`, Übersicht in `AGENTS.md`). Nur laden, wenn Vault-Inhalte **angelegt oder editiert** werden.

- **Wiederkehrende Sammel- und Auswerteaufgaben per Skript, nicht per Rohdaten-Durchlesen.** Routinen, die viele Notizen sweepen (z.B. "was wurde an Tag X bearbeitet"), gehören als Skript nach `Skripte/`: filtert und dedupliziert, gibt eine kompakte Faktenliste zurück, statt große Dumps selbst durchzulesen. Die AI übernimmt nur das Urteil.
