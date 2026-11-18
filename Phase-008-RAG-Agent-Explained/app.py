"""Streamlit chat UI for the ShopEasy shopping agent (for demos — not a production UI).

Every question goes to the CrewAI crew from agent.py together with the last six chat
messages as short-term memory. The sidebar shows the live contents of cart.xlsx.

Run with: streamlit run app.py
"""
import os
import pandas as pd
import streamlit as st
from agent import crew

folder = os.path.dirname(os.path.abspath(__file__))
cart_file = os.path.join(folder, "cart.xlsx")

# Brand assets are used as they are from the repository's zz-Brand-Assets folder.
brand_folder = os.path.join(os.path.dirname(folder), "zz-Brand-Assets")
logo_file = os.path.join(brand_folder, "Dragon-Motivation-Logo.png")
strip_file = os.path.join(brand_folder, "ShasuVathanan-GEN AI-Product-Manager.png")
negot_file = os.path.join(brand_folder, "NeGot-My-AI-Avatar.png")
BRAND = "Shasu Vathanan - GEN AI - Product Manager"

st.set_page_config(
    page_title="ShopEasy Assistant | Shasu Vathanan",
    page_icon=logo_file if os.path.exists(logo_file) else "🛍️",
    layout="wide",
)

st.markdown(
    """
    <style>
        .stApp h1 { color: #031273; }
        .brand-line { color: #FF4A62; font-size: 0.8rem; font-weight: 700; letter-spacing: 0.08em;
                      text-transform: uppercase; margin: 0; }
        .brand-rule { height: 4px; border-radius: 2px; margin: 0.4rem 0 1rem 0;
                      background: linear-gradient(90deg, #FF4A62, #FF5A45); }
        .brand-footer { text-align: center; color: #031273; font-size: 0.85rem; }
        .brand-footer a { color: #FF4A62; text-decoration: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

head_logo, head_strip = st.columns([1, 9], vertical_alignment="center")
if os.path.exists(logo_file):
    head_logo.image(logo_file, width=56)
if os.path.exists(strip_file):
    head_strip.image(strip_file, width=420)
else:
    head_strip.markdown(f'<p class="brand-line">{BRAND}</p>', unsafe_allow_html=True)
st.markdown('<div class="brand-rule"></div>', unsafe_allow_html=True)

st.title("🛍️ ShopEasy Shopping Assistant")
st.write("Ask about products or manage your cart. Example: *Which smart watch do you have?* or *Add 2 power banks to my cart*")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Ask about a product or your cart...")

if question:
    history = ""
    for msg in st.session_state.messages[-6:]:
        history = history + msg["role"] + ": " + msg["content"] + "\n"

    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = crew.kickoff(inputs={"history": history, "question": question})
            answer = result.raw
        st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

st.sidebar.header("🛒 Your Cart")
if os.path.exists(cart_file):
    cart = pd.read_excel(cart_file)
    if cart.empty:
        st.sidebar.write("Your cart is empty.")
    else:
        st.sidebar.dataframe(cart, hide_index=True)
        st.sidebar.subheader("Total: Rs. " + str(cart["total"].sum()))
else:
    st.sidebar.write("Your cart is empty.")

st.markdown('<div class="brand-rule"></div>', unsafe_allow_html=True)
foot_left, foot_mid, foot_right = st.columns([4, 1, 4])
if os.path.exists(negot_file):
    foot_mid.image(negot_file, width=56)
st.markdown(
    f"""
    <div class="brand-footer">
        <strong>{BRAND}</strong> &nbsp;&middot;&nbsp; NeGot, my AI avatar<br>
        <a href="https://shasuvathanan.com" target="_blank">SHASUVATHANAN.COM</a>
        &nbsp;&middot;&nbsp;
        <a href="https://www.linkedin.com/in/shasuvathanan" target="_blank">LinkedIn</a>
        &nbsp;&middot;&nbsp;
        <a href="https://github.com/shasu1pm/Genai-Architect-Journey" target="_blank">GitHub</a>
    </div>
    """,
    unsafe_allow_html=True,
)
