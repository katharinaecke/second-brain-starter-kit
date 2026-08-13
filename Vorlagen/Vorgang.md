---
type: Vorgang               # nenn den type wie deine Arbeitseinheit heißt (Ticket, Auftrag, Fall, Session)
description:                # Ein Satz: Problem + Lösung
externe-id:                  # z.B. Jira-ID, Auftragsnummer, leer lassen, wenn es keine gibt
datum: YYYY-MM-DD
status: offen | in-arbeit | erledigt
tags: [vorgang]
sichtbarkeit:                # optional, siehe .agents/rules/frontmatter.md
---

# {{ID}}: {{Titel}}

> Filename-Konvention: `<ID>_<Kurztitel>.md` (ohne Datum), z.B. `AB-42_Login-Bug.md`. Ohne
> externe ID: einfach `<Kurztitel>.md`.

## Kontext / Problem
Worum ging's? Was war zu tun / kaputt / gewünscht?

## Was ich vorgefunden habe
-

## Was ich gemacht habe
-

## Lessons Learned
Was hab ich gelernt? Verlinke auf Wissens-Notizen als echte Markdown-Links (nicht in
Backticks, sonst kein Graph-Link): [Konzeptname](</Wissen/Konzeptname.md>)
-

## Verwandt
-
