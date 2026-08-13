# [DEIN NAME]s Second Brain

> **TEMPLATE.** Wird beim Setup mit den tatsächlich gewählten Ordnern gefüllt. Die
> Dataview-Blöcke unten funktionieren nur, wenn du diesen Vault in Obsidian mit dem
> Dataview-Plugin öffnest. Ohne Obsidian einfach löschen oder als reine Übersicht in
> Textform führen.

Mein Wissens-Vault, wächst mit jeder Session.

> **Wenn ein Agent/eine AI reinkommt:** lies `AGENTS.md` für die token-sparsame Navigation
> (Glob/Grep direkt auf Ordner). `CLAUDE.md` ist nur ein Stub, der `AGENTS.md` importiert.
> Die Dataview-Queries unten kann ein Agent nicht ausführen, die füllen sich nur im
> Obsidian-Rendering.

## Struktur

- [Platzhalter: Kurzbeschreibung pro Ordner, siehe `AGENTS.md`]

## Wissens-Landkarten (MOCs)

- [Platzhalter: ein Link pro Themengebiet]

## Wie ich das nutze

1. **Neues Wissen gelernt?** → Notiz in den Wissens-Ordner mit passender Vorlage.
2. **Auffrischen?** → Die AI fragt aus `Lernen/Karten.md` ab (falls Lernen genutzt wird).

```dataview
TABLE
  themengebiet AS "Bereich",
  tags AS "Tags"
FROM "Wissen"
SORT themengebiet ASC, file.name ASC
```

---

**Hinweis zur Pflege:** Bei neuer Notiz nur Frontmatter konsequent ausfüllen. Falls
Dataview genutzt wird, aktualisiert sich der Index dann selbst; die MOCs bleiben
handkuratiert.
