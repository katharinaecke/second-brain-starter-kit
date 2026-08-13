---
name: brain-setup
description: Richtet dieses Starter-Kit einmalig als persönliches Second Brain ein, führt durch das Interview und baut danach Ordner, Vorlagen und Skills. Nur auf ausdrücklichen Aufruf, nie von selbst.
disable-model-invocation: true
---

# Second Brain aufsetzen

> **Einmal-Skill.** Er baut die Struktur dieses Ordners um: legt Ordner an, löscht nicht
> gebrauchte Skills und Vorlagen, schreibt `AGENTS.md` neu. Auf einem bereits eingerichteten
> Vault würde er die vorhandene Struktur überschreiben. Deshalb steht
> `disable-model-invocation: true` im Frontmatter: Er läuft **ausschließlich**, wenn jemand
> `/brain-setup` tippt, und wird nie von selbst gewählt.

## Vorgehen

0. **Zuerst fragen, wo das Brain entstehen soll, bevor irgendetwas anderes passiert.**
   Das Kit ist die **Vorlage**, nicht das Ergebnis: Der Normalfall ist ein **neuer, eigener
   Ordner**, in den das Gebrauchte kopiert wird. Frag nach Pfad und Ordnername, schlag etwas
   vor (z.B. einen Nachbarordner des Kits, `MeinBrain`), entscheide aber nicht allein.

   Warum nicht einfach im Kit-Ordner: Das Kit hängt am GitHub-Remote des Starter-Kits. Ein
   Brain, das darin wächst, erbt ihn. Ein `git pull` überschreibt eigene Dateien, und wer
   Push-Rechte auf dieses Repo hat, veröffentlicht mit einem unbedachten `git push` private
   Notizen. Außerdem soll das Brain heißen wie sein Mensch will, und das Kit für ein zweites
   Brain (oder ein Team-Brain) nutzbar bleiben.

   Der Umbau **im** Kit-Ordner ist nur zulässig, wenn er ausdrücklich verlangt wird. Dann
   klar sagen, dass das Kit danach kein Kit mehr ist und ein Rückweg nur über Git existiert.

   **Nicht vom Kontext ablenken lassen.** Sind weitere Ordner in der Session sichtbar, etwa
   ein bereits eingerichteter Vault mit eigener `AGENTS.md`, ist das **nie** der
   Zielordner, egal wie sehr er nach "dem Brain" aussieht. Fremde Vaults sind Kulisse und
   werden **niemals** angefasst.

   Nenne den gewählten Zielpfad absolut und lass ihn bestätigen, bevor du schreibst:
   "Ich lege dein Second Brain unter `<absoluter Pfad>` an. Das Kit bleibt unverändert.
   Richtig?" Erst nach einem Ja weiter.

1. **Prüfen, ob im Zielordner schon ein Brain steht.** Ein *leerer oder noch nicht
   existierender* Zielordner ist der Normalfall, dann sofort weiter zu Schritt 2, ohne
   Rückfrage. Vorsicht ist nur geboten, wenn dort schon Inhalt liegt: eine `AGENTS.md` ohne
   den TEMPLATE-Hinweisblock, angelegte Vault-Ordner oder eine `SETUP-PROMPT-erledigt.md`.
   Dann **nicht** einfach loslegen: sagen, was du siehst, und fragen, ob wirklich neu
   aufgesetzt werden soll. Bei "ja" vorher darauf hinweisen, dass vorhandene Struktur
   überschrieben wird.

   **Nicht am Kit selbst festmachen:** dass hier im Kit-Ordner eine `SETUP-PROMPT.md` liegt,
   sagt nichts über den Zielordner. Sie bleibt auch nach einem erfolgreichen Setup liegen,
   weil das Kit Vorlage bleibt. Umgekehrt fehlt sie im Zielordner grundsätzlich; das ist
   **kein** Zeichen für ein fertiges Brain, sondern der erwartete Zustand.

2. **Fragen, welcher Weg**, eine Frage, zwei Optionen:
   - **Ausführlich** (rund ein Dutzend Fragen): baut ein Setup, das genau zum Alltag passt.
   - **Kurz** (drei Fragen): Minimal-Vault, mit dem sich sofort arbeiten lässt; der Rest
     wächst später nach.

3. **`SETUP-PROMPT.md` lesen** und den Block befolgen, der zur Antwort passt, also den langen
   Prompt-Block oder den Abschnitt "Kurz-Einstieg: drei Fragen". Die Datei ist die einzige
   Quelle: Änderungen am Ablauf gehören dorthin, nicht in diesen Skill.

4. **Am Ende aufräumen, je nach gewähltem Weg unterschiedlich:**
   - **Eigener Ordner (Normalfall):** Im neuen Brain gibt es diesen Skill gar nicht erst
     (er wird nicht mitkopiert). Das **Kit bleibt vollständig unverändert**, damit es ein
     zweites Mal nutzbar ist. Zum Schluss sagen, wo das Brain liegt und wie es ab jetzt
     bedient wird.
   - **Umbau im Kit-Ordner (Ausnahme):** `SETUP-PROMPT.md` wird laut Anleitung in
     `SETUP-PROMPT-erledigt.md` umbenannt, dann zeigt dieser Zeiger ins Leere. Also
     `.claude/skills/brain-setup/` löschen und erwähnen, dass das Setup nicht mehr
     versehentlich startbar ist, der Fragebogen aber nachlesbar bleibt.
