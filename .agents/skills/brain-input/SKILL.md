---
tags: [pkm, second-brain, vault-pflege]
themengebiet: prozess
type: Vorgehen
description: Schema für die Vault-Pflege am Ende einer Session, was aus dem Chat dauerhaft ins Brain gehört, mit Vorschau vor dem Schreiben.
---

# Brain-Input-Vorgehen

> **Auslöser:** "brain input", "ab ins brain", "ins brain", "alles ins brain", "Chat
> abschließen" → diesem Schema folgen ohne Rückfrage. In Claude Code auch als
> `/brain-input`-Skill.

## Was ist das?

Gezielte Vault-Pflege am Ende einer Chat-Session: Was aus diesem Chat ist dauerhaft wert,
im Brain zu stehen? Identifizieren, hinschreiben, Abschlusssatz.

## Was gehört ins Brain?

- **Abgeschlossene Arbeitseinheiten** (falls dieser Ordner existiert): Was wurde bearbeitet?
  → Notiz anlegen/aktualisieren (aus `Vorlagen/Vorgang.md`), Datum stempeln, Status ehrlich
  setzen.
- **Neues Wissen:** Was wurde gelernt, das in 6 Monaten noch wahr ist? → Wissens-Notiz mit
  Frontmatter (aus `Vorlagen/Wissensnotiz.md`), aus der Arbeitsnotiz dorthin verlinken.
  *(nur falls Lernen aktiv)* **Karten nicht automatisch:** pro neuer Konzept-Notiz bewusst
  entscheiden "muss das aus dem Kopf gekonnt werden, oder reicht Nachschlagen?", nur bei
  echtem Kopf-Wissen 1-2 atomare Karten in `Lernen/Karten.md` anlegen (mit Link zur Notiz)
  und im Vorschau-Schritt mitzeigen. Im Zweifel keine Karte. **Kein `## Quiz`-Block in die
  Notiz**, Karten leben nur zentral (siehe `.agents/rules/karteikarten.md`).
- **Entscheidungen / laufender Stand:** Hat sich an einer laufenden Sache etwas geändert?
  → die entsprechende Projekt-/Bereichs-Notiz aktualisieren (überschreiben, nicht anhängen).
- **Personen** (falls dieser Ordner existiert): Neue relevante Kontakte? → Personen-Notiz
  aus `Vorlagen/Person.md`.
- **Extern belegte Fakten** (Studie, Statistik, Blogpost, Doku-Stelle), die später wieder
  gebraucht werden: → Quellen-Notiz aus `Vorlagen/Quelle.md`, statt die Zahl nur im Fließtext
  einer anderen Notiz zu vergraben. Siehe `.agents/rules/ablage.md`.
- **Meetings** (falls dieser Ordner existiert): **Keine reine Meeting-Notiz als Default.**
  Jede Info einzeln prüfen und nur die dauerhafte Erkenntnis in die passende Themen-Notiz
  destillieren. Eine eigene Meeting-Notiz nur, wenn der Gesprächsverlauf selbst dauerhaft
  nachvollziehbar bleiben muss.

## Wissen aktiv abholen *(vor allem im Team-Vault)*

Die Ernte aus dem Chat ist nur die Hälfte. Das meiste Fachwissen steht nie in einer Session,
es steckt im Kopf der Person, die gerade erklärt hat, warum etwas so funktioniert. Deshalb am
Ende der Ernte **ein bis drei gezielte Fragen** stellen, statt nur zusammenzufassen. Gute
Anlässe für so eine Frage:

- In der Session tauchte ein **Hausbegriff** auf, der nirgends im Vault erklärt wird.
  ("Was genau heißt bei euch <Begriff>?" → Glossar-Zeile.)
- Etwas wurde **so gemacht, wie es gemacht wurde**, ohne dass der Grund im Chat stand.
  ("War das eine bewusste Entscheidung, und weißt du noch warum?")
- Eine Erklärung war **auffällig teuer** (langes Suchen im Code, Rückfrage an jemanden).
  Genau die lohnt eine Notiz, siehe Filter unten.
- Beim Schreiben fällt auf, dass eine Notiz **eine offensichtliche Lücke** hat.

Der Ton ist Angebot, kein Verhör: höchstens drei Fragen, "weiß ich nicht" ist eine gültige
Antwort, und was unbeantwortet bleibt, wird nicht geraten. Im Solo-Vault ist das ein
Nice-to-have; im Team-Vault ist es der eigentliche Zweck, weil das Wissen sonst in den
Köpfen bleibt.

## Der Filter: lohnt sich die Zeile?

Zwei Fragen, beide müssen mit ja beantwortet sein:

1. **Müsste ich das sonst teuer neu herleiten?** Also Code lesen, jemanden fragen, erneut
   recherchieren. Die Schwelle ist der Vergleich: Ist Neu-Herausfinden teurer als die Zeile,
   die es hier kostet? Wenn nicht, nicht aufschreiben.
2. **Bleibt es stabil?** Was sich nächsten Monat ohnehin ändert, gehört in die laufende
   Projekt-Notiz, nicht ins Wissen.

Dazu die Richtungsfrage: **Schlägt die AI das später nach (Pull), oder muss es immer gelten
(Push)?** Nur Pull-Wissen gehört in den Vault. Generelle Arbeitsanweisungen gehören in
`AGENTS.md`, im Vault würden sie übersehen, siehe
[ARCHITECTURE.md](</ARCHITECTURE.md>) Abschnitt 12.

## Was gehört NICHT ins Brain?

- Ephemere Debugging-Schritte ohne Lernwert
- Dinge, die nur für diese eine Session relevant waren
- Was schon im Vault steht (kein Duplikat). **Aktualisieren statt danebenlegen:** gibt es
  schon eine Notiz zum Thema, wird sie ergänzt. Widerspricht das Neue dem, was dort steht,
  erst nachfragen, dann ersetzen, nie beide Fassungen stehen lassen.
- Anweisungen, die immer gelten (Push-Wissen, siehe oben)

## Vorschau vor dem Schreiben

Nie direkt schreiben. Erst **alles zusammen** im Chat auflisten, bevor auch nur eine Datei
angefasst wird: pro geplanter Notiz/Änderung den Zielpfad und den **vollständigen
Textinhalt** (nicht nur Stichpunkte oder eine Zusammenfassung), inklusive Frontmatter,
damit z.B. eine Datenschutz-Klassifizierung mitgeprüft werden kann. Bei Änderungen an
bestehenden Notizen reicht der geänderte/neue Abschnitt im Volltext.

Erst nach Bestätigung (oder Korrekturen) tatsächlich in den Vault schreiben. Grund:
ungeprüft landet zu leicht eine Fehlinterpretation des Chats im Brain. Der Schreibmoment
ist der günstigste Zeitpunkt, das abzufangen, nicht erst bei der nächsten Bereinigung.

**Bei großer Ernte stückeln.** Ab etwa drei bis vier geplanten Notizen wird eine
Gesamtvorschau so lang, dass sie niemand mehr wirklich liest. Dann ist das "passt" ein
Reflex und die Schutzwirkung genau weg. Also in Häppchen vorlegen und je einzeln bestätigen
lassen (z.B. erst die Wissens-Notizen, nach OK die Projekt-/Status-Updates, zuletzt
Personen). Was schon bestätigt ist, wird geschrieben; der Abschlusssatz kommt trotzdem erst,
wenn alle Häppchen durch sind.

## Personendaten im geteilten Vault *(nur im Team-Vault)*

**In einem geteilten Vault werden keine personenbezogenen Daten geschrieben, unabhängig
davon, ob eine Klassifizierung genutzt wird.** Das ist keine Abwägung im Einzelfall: Jeder
mit Zugriff liest mit, und bei einem Vault im Projekt-Repo ist das potenziell die ganze
Entwicklungsmannschaft plus alle, die das Repo später bekommen.

Konkret bleiben draußen: Einschätzungen über Kollegen, Kundendaten, private Details, alles
aus den sensiblen Kategorien. Drin bleiben darf die fachliche Zuständigkeit ("<Person> kennt
das Abrechnungsmodul") und die Quellenangabe zu einer Aussage ("laut <Person>, <Datum>"),
denn im Team ist "wer sagt das" Teil der Aussage selbst.

Taucht in der Ernte etwas auf, das darunter fällt, wird es in der Vorschau benannt und der
fachliche Kern ohne den Personenbezug angeboten. Still weglassen wäre falsch, dann weiß
niemand, dass die Information da war. Siehe `.agents/rules/team.md`.

## Datenschutz-Check beim Schreiben *(nur falls Datenschutz-Klassifizierung genutzt wird)*

Der Schreibmoment ist der beste Zeitpunkt, Overexposure abzufangen. Bevor eine
Personen-Notiz oder eine Namensnennung mit wertendem/kritischem Inhalt übernommen wird:
kurz prüfen, ob es faktisch und beruflich bleibt, statt eine subjektive Einschätzung
wortwörtlich zu übernehmen. Im Zweifel neutraler formulieren.

`sichtbarkeit:` sofort setzen, nicht auf später verschieben.

## Todos *(nur falls Todos in einem externen Tool leben, nicht im Vault)*

Neues loses Todo ohne eigenen Ticket-/Arbeits-Bezug? Keine Checkbox ins Vault schreiben.
Stattdessen im externen Todo-Tool anlegen; braucht die Notiz trotzdem einen Hinweis, reicht
ein Fließtext-Satz mit Link am Ende.

## Abschluss

Erst wenn alles wirklich im Vault steht, als letzten Satz exakt:

> Alles ist im Brain, dieser Chat kann gelöscht werden.

**Nie schreiben, solange noch etwas aus dem Chat fehlt.**

## Verwandt

- [Merk-Dir-Das-Vorgehen](</.agents/skills/merk-dir-das/SKILL.md>): der Sammel-Bruder für
  die gezielte Einzel-Info mitten im Chat, statt am Chat-Ende
- [Brain-Bereinigen-Vorgehen](</.agents/skills/brain-bereinigen/SKILL.md>): der periodische
  Tiefenputz über das, was hier laufend hereinkommt
