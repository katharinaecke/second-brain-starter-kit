---
tags: [prozess, schreiben, kommunikation, stil]
themengebiet: prozess
type: Vorgehen
description: Schema, um Texte in der eigenen Stimme statt generisch zu schreiben, je Register kalibriert über das Schreibstil-Profil. Optionales Modul.
---

# Formulieren-Vorgehen

> **Auslöser:** "formulier mir ...", "schreib mir eine Mail/Nachricht an ...", "wie sag ich das
> ...", "bring das in meinen Stil", "klingt das zu nach AI", "Schreibstil kalibrieren" o.ä. In
> Claude Code zusätzlich als `/formulieren`-Skill.
>
> **Optionales Modul**, nur relevant, wenn beim Setup gewünscht. Sonst diesen Skill-Ordner
> und `.agents/knowledge/schreibstil-profil.md` löschen.

## Was ist das?
Eine Routine, die einen Text so formuliert (oder umschreibt), dass er **nach dir** klingt
und **nicht nach AI**, im richtigen Ton für den jeweiligen Kanal und Empfänger. Eine
Nachricht an einen engen Kollegen ist etwas anderes als eine Mail an einen Kunden.

Zwei Betriebsarten:
- **Anwenden** (Normalfall): du willst einen konkreten Text. Entwurf, Stichpunkte, oder die
  AI **interviewt** dich und baut daraus den fertigen Text.
- **Kalibrieren** (einmal pro Kanal, bei Bedarf nachschärfen): die AI sammelt deine echten
  Formulierungen ein und schreibt daraus das
  [Schreibstil-Profil](</.agents/knowledge/schreibstil-profil.md>).

## Warum brauche ich das?
AI-Text ist erkennbar und unpersönlich: Gedankenstriche als Satzverbinder, Dreierfiguren,
Füllfloskeln, Höflichkeitsschleifen, glatte Symmetrie. Generische "Humanizer" machen Text
nur neutral-menschlich; das Ziel hier ist **deine** Stimme im **passenden Register**.

## Interviewen statt raten
Die AI stellt **simple Fragen**, du antwortest frei so, wie du es wirklich schreiben
würdest, als wär's schon die Nachricht. Aus diesen Roh-Antworten entsteht der Text (bzw.
beim Kalibrieren das Profil). Vorteil: keine ausgedachte "Schreibstimme", sondern deine
echte.

Gute Interview-Fragen sind klein und konkret, z.B.:
- "Was soll am Ende rüberkommen, in einem Satz?"
- "Was ist der Anlass?"
- "Gibt's was, das unbedingt rein muss?"
- "Wie nah bist du mit der Person, eher locker oder sachlich?"

## Wie funktioniert's? Anwenden

### 1. Register bestimmen
Kanal und Empfänger aus dem Auftrag ableiten, sonst kurz nachfragen (eine Frage, nicht fünf).
Registerliste beim Kalibrieren selbst aufbauen (Beispiele: Chat an engen Kollegen, Chat an
weniger vertraute Person, Mail intern, Mail an Kunden, formelle Dokumentation).

### 2. Inhalt klären
Entwurf vorhanden → **umschreiben oder nur korrigieren, genau unterscheiden.** "Bring das
in meinen Stil" darf umgebaut werden. "Nur Rechtschreibung/Grammatik" ist ein reiner
Korrektur-Lauf: Wortwahl, Satzbau, Reihenfolge unangetastet lassen. Im Zweifel die kleinere
Dosis. Nur Stichpunkte → ausformulieren. Nichts → **interviewen**.

### 3. Stilprofil laden
[Schreibstil-Profil](</.agents/knowledge/schreibstil-profil.md>) lesen und den Block für
das Register anwenden. Noch nicht kalibriert: mit neutralen Defaults arbeiten und eine
kurze Kalibrierung anbieten (3-4 Fragen).

### 4. Anti-AI-Pass (immer)
Vor der Ausgabe typische AI-Tells rausnehmen:
- **Gedankenstriche als Satzverbinder**, Punkt oder Komma stattdessen.
- **"nicht X, sondern Y"-Antithesen** und Verwandte, auflösen oder direkt sagen.
- **Marketing-Einzelwörter** (nahtlos, ganzheitlich, entscheidend, robust ...).
- **AI-Satzeinstiege** ("In der heutigen Zeit", "Lass uns", "Zusammenfassend lässt sich
  sagen") und Füllfloskeln ("darüber hinaus", "letztendlich", "es ist wichtig zu
  betonen, dass").
- **Dreierfiguren**, gleichförmiger Satzrhythmus, Über-Formatierung (Fettdruck-Listen),
  Struktur-Ankündigungen ("Hier ist ein Überblick").
- **Typografie:** gerade Anführungszeichen, kein Em- oder En-Dash, kein Ellipsenzeichen `…`,
  keine geschützten/schmalen Leerzeichen, reine Tastatur-Typografie, weil AI-Ausgabe
  Zeichen mitschleppt, die kein Mensch tippt.
- **Positiv gegensteuern:** Satzlänge variieren, konkret statt abstrakt, aktiv statt Passiv,
  Haltung zeigen.

### 5. Ausgeben
Fertigen Text kopierfertig ausgeben, keine drei Varianten auf Vorrat. Rechtschreibung,
Grammatik und Kommas immer still korrigieren, Stimme, Wortwahl und Satzbau unangetastet
lassen. Bei Änderung eines Satzes in einem längeren Absatz: den **kompletten Block** neu
ausgeben, kein Schnipsel.

## Wie funktioniert's? Kalibrieren
1. **Register wählen.**
2. **Interviewen:** 3-5 realistische Mini-Szenarien für genau dieses Register, du
   antwortest frei so, wie du es wirklich tippen würdest.
3. **Muster ziehen:** Anrede, Grußformel, Satzlänge, Förmlichkeit, Lieblingswörter, was
   weggelassen wird, Emoji-Verhalten.
4. **Ins Profil schreiben:** den Register-Block in
   [Schreibstil-Profil](</.agents/knowledge/schreibstil-profil.md>) füllen, mit 1-2 echten
   Beispielsätzen als Anker. Datum stempeln.
5. Pro Session ruhig nur 1-2 Register kalibrieren.

## On the go mitlernen
Nach jeder echten Formulier-Aufgabe das Profil für das benutzte Register still nachziehen,
beobachtete Muster ergänzen, fertigen Text als Anker aufnehmen. Änderst du am Vorschlag noch
etwas: das als Stil-Signal ins Profil übernehmen, auch bei bereits kalibrierten Registern.

## Stolpersteine
- **Unaufgefordert auffüllen** (Zitate, Quellen, Vorbehalte) ist meist unerwünscht, lieber
  schlank ausgeben und auf Wunsch ergänzen.
- **Register raten statt fragen.**
- **Zu glatt machen.** Ziel ist "klingt nach dir", nicht "perfektes Hochdeutsch".
- **Profil ist deine Stimme, nicht die der AI.** Beim Kalibrieren nur verwenden, was du im
  Interview wirklich getippt hast, nicht aus dem Vault selbst "lernen" (der ist von der AI
  geschrieben, das wäre zirkulär).

## Verwandt
- [Schreibstil-Profil](</.agents/knowledge/schreibstil-profil.md>): die gefüllte Stimme
  pro Register
