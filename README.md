# Lab 1 — Grade Evaluator & Archiver

> **ALU · BSE Year 1 · Trimester 2**
> Introduction to Python Programming and Databases

---

## Project Structure

```
lab1_Yannis-sheja/
├── grade-evaluator.py   # A python script: loading, validation, calculations, resubmission
├── organizer.sh         # A bash scritp: Archives and Resets the grades.csv file
├── grades.csv           # Sample grade data(assignment, group, score and weight)
└── README.md            # This file
```
---

## grades.csv Format

The CSV must have exactly these four columns:

```
assignment,group,score,weight
Quiz,Formative,85,20
Group Exercise,Formative,40,20
Functions and Debugging Lab,Formative,45,20
Midterm Project - Simple Calculator,Summative,70,20
Final Project - Text-Based Game,Summative,60,20

```

| Column       | Description                     | Valid values              |
|--------------|---------------------------------|---------------------------|
| `assignment` | Name of the assignment          | Any string                |
| `group`      | Category (`type` also accepted) | `Formative` / `Summative` |
| `score`      | Marks earned                    | 0 – 100                   |
| `weight`     | Percentage weight               | Positive number           |

> **Weight rules enforced by the program:**
> - Total weights must add up to **100**
> - Formative weights must add up to **60**
> - Summative weights must add up to **40**
> - Score must be between **0** and **100**

---

## How to Run the `grade-evaluator.py`
### Prerequisites

Python 3 or higher. No external packages required.

```bash
python3 --version
```

### Run

Both files(grade-evaluator.py and grades.csv) must be in the same directory. Run:

```bash
python3 grade-evaluator.py
```

### What it does

| Step | Feature |
|------|---------|
| 1 | Reads `grades.csv` from the current directory |
| 2 | Validates all scores are in range 0–100 |
| 3 | Validates Formative = 60%, Summative = 40%, Total = 100% |
| 4 | Displays a formatted assignments table |
| 5 | Calculates per-category weighted scores |
| 6 | Computes overall grade and GPA (`(grade / 100) × 5.0`) |
| 7 | Determines PASSED / FAILED (≥ 50% in **both** categories) |
| 8 | Identifies failed formative assignment(s) with highest weight for resubmission |

### Error handling

| Situation | Behaviour |
|-----------|-----------|
| `grades.csv` missing | Prints an error and exits cleanly |
| File is empty | Prints a warning and exits cleanly |
| Invalid score (< 0 or > 100) | Lists offending assignment(s) and exits |
| Weight distribution wrong | Lists all weight issues and exits |

---

## How to run `organizer.sh` 

### Prerequisites

Bash shell (Linux / macOS / WSL on Windows).

```bash
bash --version
```

### Make executable (once)

```bash
chmod +x organizer.sh
```

### Run

```bash
./organizer.sh
# or
bash organizer.sh
```

### What it does

| Step | Action |
|------|--------|
| 1 | Verifies `grades.csv` exists in the current directory |
| 2 | Creates `archive/` directory if it does not exist |
| 3 | Moves `grades.csv` → `archive/grades_YYYYMMDD-HHMMSS.csv` |
| 4 | Creates a fresh empty `grades.csv` in the current directory |
| 5 | Appends a log entry to `organizer.log` |
### Log format(`organizer.log`)

```
[20251105-170000]  original=grades.csv  archived=archive/grades_20251105-170000.csv
[20251106-083012]  original=grades.csv  archived=archive/grades_20251106-083012.csv
```

---

## Typical Workflow

```bash
# 1. Fill grades.csv with student data

# 2. Evaluate the grades
python3 grade-evaluator.py

# 3. Archive the file and reset the workspace for the next batch
bash organizer.sh

# 4. Repeat from step 1 for the next student
```

---

## Grading Formulas

```
Formative Grade  = Σ(score × weight) / Σ(weight)   [Formative assignments only]
Summative Grade  = Σ(score × weight) / Σ(weight)   [Summative assignments only]

Formative Percentage =(Formative Grade / 60) * 100
Summative Percentage =(Summative Grade / 40) * 100

Total Grade      = (Formative Grade) + (Summative Grade)
GPA              = (Total Grade / 100) * 5.0

Status           = PASSED  if Formative >= 50  AND  Summative >= 50
                 = FAILED  otherwise
```

---

*African Leadership University — School of Business and Entrepreneurship*
