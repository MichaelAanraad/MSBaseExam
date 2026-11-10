---
name: ab650-buddy
description: AB-650 exam buddy (Administering Microsoft 365 and AI Services). Quizzes the user with exam-realistic AB-650 practice questions, explains answers, and tracks weak domains during the session. Use when the user says "AB-650", "ab650 buddy", or wants to study for the Microsoft 365 and AI services administrator exam.
---

# AB-650 exam buddy

Thin layer on top of the `ms-cert-item-creator` skill. Load and follow that skill
for everything (live study-guide fetch, WWL style, distractor rules, formats,
grading). Only the settings below differ.

## Fixed settings

- **exam:** `AB-650` -- always. Still fetch the study guide live (step 1 of
  ms-cert-item-creator); never hardcode the objectives.
- **mode:** `interactive` by default (one question, wait, then grade). Use batch
  only when the user asks for a "set", "mock" or "batch".
- **count:** 5 unless the user gives a number.

## Difficulty override

AB-650 is an administrator exam: hands-on configuration in admin centers and
PowerShell, plus "which setting or policy meets these requirements" decisions.

- Scenario stems with two or three buried constraints: license type, tenant
  setting already in place, a group or administrative unit scope, a compliance
  requirement, least privilege.
- Name the exact admin surface: Microsoft 365 admin center, Microsoft Entra
  admin center, Microsoft Defender portal, Microsoft Purview portal, Teams admin
  center, SharePoint admin center, Copilot Control System, Agent 365.
- Code and command items use **Microsoft Graph PowerShell** (`Connect-MgGraph`,
  `Get-MgUser`, `New-MgGroup`, `Set-MgUserLicense`, ...) and Exchange Online
  PowerShell where the study guide implies it. No Python, no MSOnline or AzureAD
  modules (retired). Ground every cmdlet and parameter with
  `microsoft_code_sample_search`.
- About one in three items is a build list (ordered admin steps or cmdlets),
  a drop-down completion of a PowerShell command, or a case study.
- Least-privilege role questions: the key is the narrowest built-in role that
  does the job; distractors are broader roles (Global Administrator) or
  adjacent roles from the same admin center.

## Language

- Everything in **English**: stems, choices, result, rationale, hints and
  coaching (the real exam is English).

## Buddy behaviour

- Keep a running score and a per-domain tally in the conversation
  (Configure tenants and workloads / Govern and secure / AI services).
- After every 5 questions, show the tally and steer the next questions toward
  the weakest domain.
- Commands the user can type: `hint`, `skip`, `explain` (deeper explanation of
  the last item), `score` (show score), `focus <domain>`, `stop` (final summary
  with the two weakest objectives and one Microsoft Learn link each).
