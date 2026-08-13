---
type: Log
description: Der zentrale Kartenstapel, Frage, Antwort und Lernstand pro Zeile, gelesen und fortgeschrieben von der Lernrunde.
tags: [lernen]
---

# Karten (Spaced Repetition)

> **VORLAGE.** Wird beim Setup, nur falls aktives Lernen gewählt wurde, als
> `Lernen/Karten.md` in den Vault kopiert (Ordnername anpassbar). Bleibt Lernen aus, kann
> diese Datei gelöscht werden.
>
> Der **zentrale, kuratierte Kartenstapel**: Frage, Antwort und Lernstand in einer Datei,
> damit eine Lernrunde mit **einem** Datei-Read auskommt (tokensparend). **Pflegt die AI
> automatisch**, siehe [Lernkarten-Vorgehen](</.agents/skills/lernen/SKILL.md>). Muss nicht
> von Hand editiert werden. Am Anfang leer, das ist normal.
>
> **Aufnahmekriterium (hart):** Eine Karte entsteht nur für Wissen, das **aus dem Kopf
> gekonnt werden muss** (Daily, Review, Gespräch), nicht für Wissen, das nachgeschlagen
> werden kann. Das meiste Vault-Wissen ist Nachschlage-Wissen und wird **keine** Karte.
> Karten entstehen bewusst über Brain-Input (beim Reinkommen) und Brain-Bereinigen
> (Qualitätswächter), siehe `.agents/rules/karteikarten.md`.
>
> **Kartenqualität:** atomar (eine Karte = eine Sache), Anwendung statt Definition ("was
> tust du, wenn X?" statt "was ist X?"), Antwort knapp. `|` in Frage/Antwort als `\|`
> schreiben.
>
> **Lernstand:** Box 1 bis 6, Intervalle 1 / 2 / 4 / 7 / 15 / 30 Tage. `Fällig` = ISO-Datum.
> `Historie` neuestes rechts: `✓` richtig, `~` teilweise, `✗` falsch. `ID` = fortlaufende
> Nummer (nie recyceln).

| ID | Frage | Antwort | Box | Fällig | Historie | Quelle |
|----|-------|---------|-----|--------|----------|--------|
