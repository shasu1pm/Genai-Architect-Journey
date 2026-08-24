# Student Grade System

**Shasu Vathanan - GEN AI - Product Manager**

$\textcolor{#FF4A62}{\rule{26em}{4pt}}$

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

$\textcolor{#FF4A62}{\rule{20em}{2pt}}$

## Contributing

Feel free to fork this repository, improve the content, and share your knowledge with the community.

---

**Created and Maintained by:**

### **Shasu Vathanan - GEN AI - Product Manager**

<a href="https://shasuvathanan.com" target="_blank">SHASUVATHANAN.COM</a> &nbsp;&#8226;&nbsp; <a href="https://www.linkedin.com/in/shasuvathanan" target="_blank">LinkedIn</a>
