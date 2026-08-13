---
tags: [pkm, second-brain, vault-pflege]
themengebiet: prozess
type: Vorgehen
description: Schema, um eine einzelne Info mitten im Gespräch festzuhalten, immer erst mit Rückfrage wohin, nie als stilles Auto-Memory.
---

# Merk-Dir-Das-Vorgehen

> **Auslöser:** "merk dir das", "merk dir", "notier dir das", "das solltest du dir merken",
> "festhalten" → diesem Schema folgen. In Claude Code auch als `/merk-dir-das`-Skill.

## Was ist das?

Eine einzelne Info oder Regel, die im Gespräch dauerhaft festgehalten werden soll, an den
**richtigen Ort** schreiben, **nicht automatisch, sondern nach kurzer Rückfrage, wohin**.
Ersetzt ein automatisches, stilles Memory: nichts wird ohne Bestätigung gespeichert, die
Person entscheidet jedes Mal selbst.

## Vorgehen

### 1. Info benennen
Die zu merkende Info/Regel in einem Satz zusammenfassen und zeigen ("Ich halte fest: ..."),
damit klar ist, was gespeichert wird.

### 2. Fragen: wohin?
**Immer** fragen, mit Optionen wie:
1. **Brain** (dieser Vault): Wissen, Fakten, laufender Stand, Personen, Arbeitseinheiten.
2. **Ein anderes Repo/Projekt**, falls es eine Regel/Konvention für ein bestimmtes anderes
   Repo ist. Anonyme/geteilte Repos: nichts Persönliches (kein Klarname/Mail) reinschreiben.
3. **Andere**: anderer Ort/Datei; Pfad erfragen.

### 3. Am Ziel nach dessen Konventionen schreiben
- **Brain:** in den richtigen Ordner nach `.agents/rules/` (Frontmatter inkl.
  `type`/`description`/`sichtbarkeit`, Standard-Markdown-Links, `## Verwandt` mit
  Kontext-Halbsätzen; **kein** `## Quiz`-Block, Karten leben, falls Lernen aktiv ist,
  zentral in `Lernen/Karten.md`). Vorher prüfen, ob es schon eine passende Notiz gibt,
  nicht duplizieren.
- **Anderes Repo:** in dessen `AGENTS.md`/`CLAUDE.md`/README, im Stil der Datei.
- **Grundregel:** repo-spezifisch → Repo; Wissen/Status → Brain; steht es schon woanders →
  dorthin, nicht doppeln.

### 4. Bestätigen
Kurz sagen, was wo gelandet ist.

## Abgrenzung
- **`brain-input`** sichert am Chat-Ende *alles* Relevante, dieser Skill hält gezielt
  **eine** Sache sofort fest.
- Reine Verhaltens-Präferenzen ohne Repo- oder Wissens-Heimat sind selten. Im Zweifel
  nachfragen, statt in ein generisches Memory zu kippen.

## Verwandt
- [Brain-Input-Vorgehen](</.agents/skills/brain-input/SKILL.md>): der Sammel-Bruder am
  Chat-Ende
- [Brain-Bereinigen-Vorgehen](</.agents/skills/brain-bereinigen/SKILL.md>): nimmt die hier
  abgelegten Einzel-Infos rotierend in die F1 bis F5-Prüfung
- [Brain-Optimieren-Vorgehen](</.agents/skills/brain-optimieren/SKILL.md>): prüft dieses
  Vorgehen im Brain-Skills-Konsistenz-Check mit
