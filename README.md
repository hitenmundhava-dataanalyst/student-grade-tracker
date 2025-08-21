# 🎓 Student Grade Tracker with Retests

A simple **Python project** to track student grades with **retest options** if marks are below the passing threshold (40).  
Grades are automatically assigned, and results are saved into a **CSV file** for record-keeping.

---

## 🚀 Features
- Accepts marks for multiple students across subjects.
- Retest option if a student scores below 40.
- Assigns grades based on marks:
  - `A`: 90+
  - `B`: 75–89
  - `C`: 60–74
  - `D`: 40–59
  - `F`: Below 40
- Saves results to **grades.csv** (all subjects in one row per student).
- Handles invalid inputs (e.g., negative numbers, >100, non-integers).

---

## 📂 Example CSV Output

```csv
Name,Math,Science,English
Hiten,A,B,C
Ravi,D,C,A
