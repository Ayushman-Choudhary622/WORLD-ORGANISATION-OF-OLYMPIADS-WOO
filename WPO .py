A colorful and beautiful webpage using Python (with Streamlit)

import streamlit as st

st.set_page_config(page_title="Test Notification", layout="centered", page_icon="⚠️")

st.markdown(""" <style> .main { background: linear-gradient(to right, #6a11cb, #2575fc); color: white; padding: 2rem; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; } .title { color: #ffcc00; text-align: center; font-size: 2.5rem; font-weight: bold; } .section-title { color: #00ffff; font-size: 1.5rem; margin-top: 1.5rem; } .highlight { color: #ffcc00; font-weight: bold; } ul { margin-left: 1rem; } </style> """, unsafe_allow_html=True)

st.markdown("<div class='main'>", unsafe_allow_html=True)

st.markdown("<div class='title'>!! IMPORTANT !!</div>", unsafe_allow_html=True)

st.markdown("""

Dear Student,

This is to inform you that your Test is scheduled on 14-04-25.

Roll No: 23107

Reporting Time: 04:50 PM (Main Bed Room)

Test Timing: 05:00 PM - 06:00 PM

Test Venue: Railway Quarter No E/72/2, Motibagh, Near Kalamandir

Contact for Queries: 7972410890


WPO: AYUSH


---

<div class='section-title'>Syllabus</div>Topic: BASIC MATHEMATICS TOOLS (till Slope of Curve - NSEJS Level)

Trigonometric Ratios + Formulas

Sine Rule

Lami's Theorem

Slope of Curve + Parabola, Hyperbola etc.

Units and Measurements + Formula Derivation

Vernier Callipers

Scalars: Addition, Subtraction, Multiplication, Division

Vectors: Addition, Subtraction, Multiplication, Division

Error and Analysis



---

Video Recommended: Alakh Pandey
Paper Type: 50 Questions, 50 Minutes (SCQ + MCQ)


---

<div style='text-align:center; font-style:italic;'>
Best of luck! Stay calm and give your best.
</div>""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

