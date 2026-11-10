"""Pick the exam from the first argument: python <script>.py <exam> ...

Loads exams/<exam>/objectives.py and makes data/ paths relative to that folder.
Import this before `objectives`.
"""
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
EXAMS = sorted(d for d in os.listdir(os.path.join(ROOT, "exams"))
               if os.path.isfile(os.path.join(ROOT, "exams", d, "objectives.py")))
if len(sys.argv) < 2 or sys.argv[1] not in EXAMS:
    sys.exit(f"usage: python {os.path.basename(sys.argv[0])} <exam> [...]   exams: {', '.join(EXAMS)}")
KEY = sys.argv.pop(1)
DIR = os.path.join(ROOT, "exams", KEY)
sys.path.insert(0, DIR)
os.chdir(DIR)
