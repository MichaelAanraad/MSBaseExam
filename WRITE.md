# One-pass writing brief (new exam)

For a new exam, writers produce final-quality questions in one pass: the
writing rules (`BRIEF.md`), plausible distractors (`DISTRACTORS.md`), the real
exam formats and teaching explanations (`CONVERT.md`) all at once. A separate
verification pass (`VERIFY.md`) follows.

Read, in this order: `BRIEF.md`, `exams/<exam>/AUDIENCE.md`,
`DISTRACTORS.md`, `CONVERT.md`, `validate.py` (the exact format rules), and
`examples/examples.json` plus `examples/cases_example.json` (format only; the
content is from another exam, do not copy it). Run
`python exams/<exam>/objectives.py` for your target counts.

Rules on top of those briefs:

- Write each question directly in its final type. The type quota in your
  assignment is exact; every other question is `single`. Spread the types over
  the objectives of your group, and order questions over several objectives.
- CONVERT.md "Task A" (conversion) applies as "write in this format"; "Task B"
  (explanations) applies to every question.
- `BRIEF.md` mentions ordering as four sequences in a single-answer question;
  ignore that and use the `order` type instead.
- A series question counts toward its objective; all items of one series test
  the same objective. A case question counts toward its own objective.
- Verify every fact on Microsoft Learn before writing it. Fewer exotic facts
  and more solid ones is better than one invented setting.
- Save often: write the group file in parts with a small Python script that
  loads, appends and dumps JSON (`indent=1, ensure_ascii=False`).
- Validate: `python validate.py <exam> <group>` (all your groups together if
  you have more than one) until 0 errors.
- Edit only your own group files and your own case file.

Final report (short): counts per type, the case and series ids, sub-topics
where Learn had little and what you did about it, any fact you could not
verify.
