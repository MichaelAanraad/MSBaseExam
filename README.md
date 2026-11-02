# AI-500 Exam Buddy

500 practice questions for Microsoft exam **AI-500: Designing and Implementing
Multi-Agent AI Solutions**, spread over all 55 objectives in the official
[study guide](https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-500),
weighted by domain, at three difficulty levels. Original questions, not exam dumps.

Open `docs/index.html` in a browser, or host it on GitHub Pages:

1. Push this folder to a GitHub repository.
2. Repository **Settings** -> **Pages** -> Source: *Deploy from a branch*,
   branch `main`, folder `/docs`.
3. Open `https://<your-user>.github.io/<repo>/`.

Progress is stored in your browser (localStorage), per device.

Question types, as on the real exam: single and multiple choice, build list
(ordering, mostly real `az`/`azd`/SDK command sequences), drag and drop,
code completion with drop-down lists, yes/no statements, problem-solution
series (no going back) and case studies. Every choice, value and option has an
explanation of what it does and when it would be right.

Modes: practice (feedback per question), exam (feedback at the end), and exam
simulation: 50 questions weighted by domain, 100 minutes, no hints, mark for
review, review screen, and series and case study sections you cannot return
to. Multi-part questions earn partial credit. Labs are not simulated.

## A base for other exams

This project is meant as a starting point for colleagues who want to build
the same kind of practice exam for another Microsoft certification (AZ-104,
AI-102, PL-200, ...). The app, the validator, the writing briefs and the skills
do not depend on AI-500; only the objective map and the questions do.

Example: you want a bank of 700 questions for AZ-104:

1. Fork or copy this repository.
2. Open it in Claude Code and ask: *"Rewrite objectives.py for AZ-104 from the
   live study guide, TOTAL = 700, weighted by domain."* The skills fetch the
   study guide through the Microsoft Learn MCP server. `TOTAL` in
   `objectives.py` is the only place the bank size is set; the per-objective
   counts (`GROUPS` and `OVERRIDE`) must add up to it, which
   `python objectives.py` checks.
3. Replace the AI-500 parts: the exam name in `BRIEF.md`, the title and intro
   text in `template.html`, and the `ai500.` storage keys in `template.html`
   (otherwise progress mixes with this exam in the same browser).
4. Empty `data/` and let Claude Code write questions per objective group,
   following `BRIEF.md` and `DISTRACTORS.md`. Then run the conversion pass
   (`CONVERT.md`) and an independent verification pass (`VERIFY.md`).
5. `python validate.py` until 0 errors, then `python build.py`, and publish
   `docs/` with GitHub Pages.
6. Practice in exam simulation mode until you score clearly above 70% several
   times. The real exam passes at 700 on a scale of 1 to 1000; that scaled
   score is not exactly 70% correct, so keep a margin.

The `ai500-buddy` skill is a thin layer over `ms-cert-item-creator`; copy it,
change the exam ID, and you have a chat buddy for your own exam.

## Claude Code skills

Open this folder in Claude Code and the project skills load automatically:

- `ai500-buddy`: interactive AI-500 quiz partner in chat, with score and
  weak-domain tracking. Say "AI-500" or "ai500 buddy".
- `ms-cert-item-creator`: writes exam-realistic questions for any Microsoft
  exam, following the WWL style guide.
- `/cert-quiz exam=AI-102 count=5`: slash command wrapper around the item
  creator.

The skills read the live study guide through the Microsoft Learn MCP server,
configured in `.mcp.json` (no key needed; approve it when Claude Code asks).

## Editing questions

Questions live in `data/<group>.json`, case studies in `data/cases_*.json`.
Format examples for each type: `examples/`. Writing briefs: `BRIEF.md`,
`DISTRACTORS.md`, `CONVERT.md`, `VERIFY.md`. After a change:

```
python validate.py   # coverage, counts, style checks
python similar.py    # look-alike questions across objectives
python build.py      # regenerates docs/index.html
```
