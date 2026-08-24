"""Streamlit Student Grade App.

Run with: streamlit run grade_app.py
"""

import streamlit as st


def calculate_grade(mark: float) -> str:
    """Return the letter grade for a validated mark between 0 and 100."""
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "E"


def format_mark(mark: float) -> str:
    """Display whole-number marks without an unnecessary decimal point."""
    return str(int(mark)) if mark.is_integer() else f"{mark:g}"


st.set_page_config(
    page_title="Student Grade App | Shasu Vathanan",
    page_icon="🎓",
    layout="centered",
)

st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(circle at 10% 10%, rgba(255, 74, 98, 0.10), transparent 28rem),
                #F7F8FD;
        }
        .block-container {
            max-width: 760px;
            padding-top: 3rem;
            padding-bottom: 2rem;
        }
        .brand {
            color: #FF4A62;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            margin-bottom: 0.6rem;
            text-transform: uppercase;
        }
        .hero-title {
            color: #031273;
            font-size: clamp(2rem, 6vw, 3.25rem);
            font-weight: 800;
            letter-spacing: -0.04em;
            line-height: 1.05;
            margin: 0;
        }
        .hero-copy {
            color: #5A6391;
            font-size: 1.05rem;
            margin: 0.8rem 0 1.8rem;
        }
        .result-card {
            align-items: center;
            background: linear-gradient(135deg, #FF4A62, #FF5A45);
            border-radius: 18px;
            box-shadow: 0 18px 45px rgba(255, 74, 98, 0.28);
            color: white;
            display: flex;
            justify-content: space-between;
            margin-top: 1.4rem;
            padding: 1.5rem 1.75rem;
        }
        .result-label {
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            opacity: 0.78;
            text-transform: uppercase;
        }
        .result-mark {
            font-size: 1.35rem;
            font-weight: 700;
            margin-top: 0.25rem;
        }
        .result-grade {
            font-size: 3.8rem;
            font-weight: 900;
            letter-spacing: -0.05em;
            line-height: 1;
        }
        .scale-title {
            color: #031273;
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            margin: 2rem 0 0.7rem;
            text-transform: uppercase;
        }
        .scale-row {
            background: white;
            border: 1px solid #DDE1F2;
            border-left: 3px solid #FF4A62;
            border-radius: 12px;
            color: #3B4374;
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.45rem;
            padding: 0.7rem 1rem;
        }
        .scale-row strong { color: #031273; }
        .footer {
            border-top: 1px solid #DDE1F2;
            color: #5A6391;
            font-size: 0.82rem;
            margin-top: 2.2rem;
            padding-top: 1.1rem;
            text-align: center;
        }
        .footer strong { color: #031273; }
        .footer a { color: #FF4A62; text-decoration: none; }
        .footer a:hover { text-decoration: underline; }
        div[data-testid="stTextInput"] input {
            background: white;
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="brand">Shasu Vathanan - GEN AI - Product Manager</div>
    <h1 class="hero-title">Student Grade Calculator</h1>
    <p class="hero-copy">Enter a mark to instantly find the corresponding letter grade.</p>
    """,
    unsafe_allow_html=True,
)

mark_input = st.text_input(
    "Enter your mark (0–100)",
    placeholder="For example: 85",
    help="You may enter a whole number or a decimal value.",
)

cleaned_input = mark_input.strip()

if not cleaned_input:
    st.info("Enter a mark above to calculate a grade.", icon="ℹ️")
else:
    try:
        mark = float(cleaned_input)
        if not 0 <= mark <= 100:
            st.error("Please enter a mark between 0 and 100.", icon="⚠️")
        else:
            grade = calculate_grade(mark)
            displayed_mark = format_mark(mark)
            st.markdown(
                f"""
                <div class="result-card">
                    <div>
                        <div class="result-label">Your result</div>
                        <div class="result-mark">Mark: {displayed_mark} / 100</div>
                    </div>
                    <div>
                        <div class="result-label">Grade</div>
                        <div class="result-grade">{grade}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    except ValueError:
        st.error("That does not look like a number. Please enter a value from 0 to 100.", icon="⚠️")

st.markdown('<div class="scale-title">Grading scale</div>', unsafe_allow_html=True)

for grade_label, mark_range in (
    ("A", "90–100"),
    ("B", "80–89"),
    ("C", "70–79"),
    ("D", "60–69"),
    ("E", "Below 60"),
):
    st.markdown(
        f'<div class="scale-row"><span>{mark_range}</span><strong>Grade {grade_label}</strong></div>',
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="footer">
        <strong>Shasu Vathanan - GEN AI - Product Manager</strong><br>
        <a href="https://shasuvathanan.com" target="_blank">SHASUVATHANAN.COM</a>
        &nbsp;&middot;&nbsp;
        <a href="https://www.linkedin.com/in/shasuvathanan" target="_blank">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True,
)
