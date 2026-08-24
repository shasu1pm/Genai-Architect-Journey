"""Convert a student mark from 0 to 100 into a letter grade."""

import math


def calculate_grade(mark: float) -> str:
    """Return the letter grade for a validated mark."""
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "E"


def main() -> None:
    """Read a mark, validate it, and display the matching grade."""
    entered_mark = input("Enter your mark (0-100): ").strip()

    try:
        mark = float(entered_mark)
    except ValueError:
        print("Invalid input: please enter a number between 0 and 100.")
        return

    if not math.isfinite(mark) or not 0 <= mark <= 100:
        print("Invalid mark: please enter a number between 0 and 100.")
        return

    display_mark = f"{mark:g}"
    grade = calculate_grade(mark)
    print(f"Mark: {display_mark} -> Grade: {grade}")


if __name__ == "__main__":
    main()
