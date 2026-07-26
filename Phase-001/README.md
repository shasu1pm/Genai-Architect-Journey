# Student Grade System

A terminal-based Python program that converts a mark from 0 to 100 into a
letter grade.

## Run

```powershell
python grade_system.py
```

## Grade scale

| Mark | Grade |
|---|---|
| 90–100 | A |
| 80–89.999… | B |
| 70–79.999… | C |
| 60–69.999… | D |
| Below 60 | E |

## Example terminal runs

```text
Enter your mark (0-100): 95
Mark: 95 -> Grade: A

Enter your mark (0-100): 85
Mark: 85 -> Grade: B

Enter your mark (0-100): 59
Mark: 59 -> Grade: E
```

Invalid input is handled without crashing. Non-numeric values produce a clear
request to enter a number, while values outside 0–100 (including non-finite
values such as `nan`) produce a clear range error.
