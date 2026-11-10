# Exam Buddy

Practice exams for Microsoft certifications, 500 questions each, spread over
every objective in the official study guide, weighted by domain, at three
difficulty levels. Original questions, not exam dumps.

| Exam | Title | Site |
|---|---|---|
| AI-500 | Designing and Implementing Multi-Agent AI Solutions | `docs/ai500/` |
| AB-650 | Administering Microsoft 365 and AI Services | `docs/ab650/` |

Open `docs/index.html` in a browser, or host it on GitHub Pages:

1. Push this folder to a GitHub repository.
2. Repository **Settings** -> **Pages** -> Source: *Deploy from a branch*,
   branch `main`, folder `/docs`.
3. Open `https://<your-user>.github.io/<repo>/` and pick an exam.

Progress is stored in your browser (localStorage), per device and per exam.
The pages work offline and on phones.

Question types, as on the real exam: single and multiple choice, build list
(ordering, mostly real command sequences: `az`/`azd`/SDK for AI-500,
Microsoft Graph and Exchange Online PowerShell for AB-650), drag and drop,
code completion with drop-down lists, yes/no statements, problem-solution
series (no going back) and case studies. Every choice, value and option has an
explanation of what it does and when it would be right.

Modes: practice (feedback per question), exam (feedback at the end), and exam
simulation: 50 questions weighted by domain, 100 minutes, no hints, mark for
review, review screen, and series and case study sections you cannot return
to. Multi-part questions earn partial credit. Labs are not simulated.

## Layout

```
exams/<exam>/objectives.py   exam id, title, study guide, domains, objectives, counts
exams/<exam>/AUDIENCE.md     audience, code language, product names, exam rules
exams/<exam>/data/           questions (<group>.json) and case studies (cases_*.json)
docs/<exam>/index.html       built site for that exam
docs/index.html              start page with a link per built exam
template.html                the app (shared by all exams)
validate.py build.py similar.py   tools; the first argument is the exam folder
BRIEF.md WRITE.md DISTRACTORS.md CONVERT.md VERIFY.md REVIEW.md   briefs for writers and reviewers
examples/                    one example of every question type
```

```
python validate.py ab650          # coverage, counts, format and style checks
python validate.py ab650 2.1 2.2  # only these groups
python similar.py ab650           # look-alike questions across objectives
python build.py ab650             # writes docs/ab650/index.html and docs/index.html
python exams/ab650/objectives.py  # target count per objective
```

## Add another exam

The app, the validator, the briefs and the skills are exam-neutral. Example:
AZ-104.

1. Copy `exams/ab650/` to `exams/az104/` and empty its `data/` folder.
2. Open the project in Claude Code and ask: *"Rewrite exams/az104/objectives.py
   for AZ-104 from the live study guide, TOTAL = 500, weighted by domain, and
   rewrite AUDIENCE.md from its audience profile."* The skills fetch the study
   guide through the Microsoft Learn MCP server.
   `python exams/az104/objectives.py` checks that the counts add up to `TOTAL`.
3. Let Claude Code write the questions per objective group with `WRITE.md`
   (one agent per group works well), then run an independent verification
   pass with `VERIFY.md`.
4. `python validate.py az104` until 0 errors, then `python build.py az104`,
   commit and push. The start page picks up the new exam.
5. Practice in exam simulation mode until you score clearly above 70% several
   times. The real exam passes at 700 on a scale of 1 to 1000; that scaled
   score is not exactly 70% correct, so keep a margin.

| Setting in `objectives.py` | What it sets |
|---|---|
| `EXAM`, `EXAM_TITLE` | page title, header, start page, browser storage prefix |
| `STUDY_GUIDE` | source for the objectives |
| `DOMAINS`, `GROUPS`, `OVERRIDE` | domains, weights, questions per objective |
| `TOTAL` | bank size the validator and build check |

The simulation (50 questions, 100 minutes) matches role-based exams; adjust it
in `template.html` if your exam differs.

## Claude Code skills

Open this folder in Claude Code and the project skills load automatically:

- `ai500-buddy` / `ab650-buddy`: interactive quiz partner in chat for AI-500
  or AB-650, with score and weak-domain tracking. Say "AI-500" or "AB-650".
  For another exam, copy one of these folders and change the exam ID.
- `ms-cert-item-creator`: writes exam-realistic questions for any Microsoft
  exam, following the WWL style guide.
- `/cert-quiz exam=AZ-104 count=5`: slash command wrapper around the item
  creator; works for any exam.

The skills read the live study guide through the Microsoft Learn MCP server,
configured in `.mcp.json` (no key needed; approve it when Claude Code asks).
