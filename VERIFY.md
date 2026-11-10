# Independent verification brief (pass 3)

You are a skeptical subject-matter expert for the exam in objectives.py (`EXAM`). Other writers produced and
converted these questions; assume every one may be wrong. Read `BRIEF.md`, `exams/<exam>/AUDIENCE.md`,
`CONVERT.md` and `validate.py` first. Load the Microsoft Learn tools:
ToolSearch `select:mcp__microsoft-learn__microsoft_docs_search,mcp__microsoft-learn__microsoft_docs_fetch,mcp__microsoft-learn__microsoft_code_sample_search`

For EVERY question in your assigned files (and the case study they use):

1. **Key is correct.** Check it against Microsoft Learn (open the `ref`, search
   further when needed). For `order`, the sequence is forced by real
   dependencies and exactly one order works. For commands and code, every
   command, parameter and API exists with that exact spelling (check with
   `microsoft_code_sample_search` / fetched pages). Fix or replace what is
   wrong or unverifiable.
2. **Exactly one defensible answer.** No distractor is also right; no extra
   action in an order question is also required. Sharpen the stem if needed.
3. **Wrong choices are real and plausible**, from the same family as the key,
   ruled out only by a constraint in the stem (no nonsense, no giveaway).
4. **Every explanation teaches.** Each wrong-choice explanation states what
   the option really does, the stem constraint that rules it out, and when it
   would be right, and those facts are TRUE. Each correct-choice explanation
   ties to the stem constraints. Fix false or vague explanations.
5. **Case study questions** actually need the case details, and do not
   contradict the case text. Series items share an identical problem
   statement, and each Yes/No key is right.
6. **Objective fit and difficulty label** are plausible.

Do not change `id`, `obj`, `difficulty` or the type counts. Keep the answer
key consistent with the explanations. English, code only in the language from `AUDIENCE.md`, ASCII in exam
text. Run `python validate.py <exam> <your groups>` until 0 errors.

Final report (short): questions checked, changed ids with one line each on
what was wrong, and anything still unverifiable.
