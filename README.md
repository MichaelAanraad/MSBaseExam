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
