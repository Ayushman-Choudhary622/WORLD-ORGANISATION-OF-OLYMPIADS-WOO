import streamlit as st

# Set up page configuration: title, icon, layout
st.set_page_config(page_title="Test Notification", page_icon="⚠️", layout="wide")

# Custom CSS with media queries for responsiveness
custom_css = """
<style>
/* Global styling */
body {
    background: linear-gradient(to right, #6a11cb, #2575fc);
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Main container */
.main-container {
    background: rgba(0, 0, 0, 0.5);
    border-radius: 20px;
    padding: 2rem;
    max-width: 900px;
    margin: 2rem auto;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
}

/* Title styling */
.title {
    text-align: center;
    font-size: 2.8rem;
    font-weight: bold;
    color: #ffcc00;
    margin-bottom: 1.5rem;
}

/* Section headers */
.section-title {
    font-size: 1.8rem;
    color: #00ffff;
    margin-top: 1.5rem;
    border-bottom: 2px solid #00ffff;
    padding-bottom: 0.5rem;
}

/* Body text styling */
.text {
    font-size: 1.2rem;
    line-height: 1.6;
    margin-bottom: 1rem;
}

/* List styling */
ul {
    margin-left: 1.5rem;
    font-size: 1.2rem;
    line-height: 1.6;
}

/* Footer styling */
.footer {
    text-align: center;
    font-style: italic;
    margin-top: 2rem;
}

/* Media queries for mobile devices */
@media (max-width: 600px) {
    .title {
        font-size: 2rem;
    }
    .section-title {
        font-size: 1.5rem;
    }
    .text, ul {
        font-size: 1rem;
    }
    .main-container {
        padding: 1rem;
        margin: 1rem;
    }
}
</style>
"""

# Inject CSS into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

# Create the main container
st.markdown("<div class='main-container'>", unsafe_allow_html=True)

# Title and Notification Banner
st.markdown("<div class='title'>!! IMPORTANT !!</div>", unsafe_allow_html=True)

# Dynamic content: In a fully dynamic version, you might get these values from a database or user inputs.
# Here we simply define them as variables.
test_date = "14-04-25"
roll_no = "23107"
reporting_time = "04:50 PM"
test_time = "05:00 PM - 06:00 PM"
test_venue = "Railway Quarter No E/72/2, Motibagh, Near Kalamandir"
contact = "7972410890"
wpo = "AYUSH"

# Notification details with HTML for styling
notification_html = f"""
<div class='text'>
    <strong>Dear Student,</strong><br><br>
    This is to inform you that your <strong>Test</strong> is scheduled on <strong>{test_date}</strong>.<br><br>
    <ul>
        <li><strong>Roll No:</strong> {roll_no}</li>
        <li><strong>Reporting Time:</strong> {reporting_time} <em>(Main Bed Room)</em></li>
        <li><strong>Test Timing:</strong> {test_time}</li>
        <li><strong>Test Venue:</strong> {test_venue}</li>
        <li><strong>Contact for Queries:</strong> {contact}</li>
    </ul>
    <br>
    <strong>WPO: {wpo}</strong>
</div>
"""

st.markdown(notification_html, unsafe_allow_html=True)

# Syllabus Section
st.markdown("<div class='section-title'>Syllabus</div>", unsafe_allow_html=True)

syllabus_html = """
<div class='text'>
    <strong>Topic:</strong> BASIC MATHEMATICS TOOLS (till Slope of Curve - NSEJS Level)<br><br>
    <ul>
        <li>Trigonometric Ratios + Formulas</li>
        <li>Sine Rule</li>
        <li>Lami's Theorem</li>
        <li>Slope of Curve + Parabola, Hyperbola etc.</li>
        <li>Units and Measurements + Formula Derivation</li>
        <li>Vernier Callipers</li>
        <li>Scalars: Addition, Subtraction, Multiplication, Division</li>
        <li>Vectors: Addition, Subtraction, Multiplication, Division</li>
        <li>Error and Analysis</li>
    </ul>
    <br>
    <strong>Video Recommended:</strong> Alakh Pandey<br>
    <strong>Paper Type:</strong> 50 Questions, 50 Minutes (SCQ + MCQ)
</div>
"""

st.markdown(syllabus_html, unsafe_allow_html=True)

# Footer or closing message
footer_html = """
<div class='footer'>
    Best of luck! Stay calm and give your best.
</div>
"""

st.markdown(footer_html, unsafe_allow_html=True)

# Close main container div
st.markdown("</div>", unsafe_allow_html=True)
