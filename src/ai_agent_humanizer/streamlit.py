import streamlit as st
from main import get_human_written_text 

# Page configuration
st.set_page_config(
    page_title="AI Humanizer",
    page_icon="🧠",
    layout="centered"
)

# App title and description
st.markdown("<h1 style='text-align: center;'>🧠 AI Text Humanizer</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center;'>Paste your text below. We'll rewrite it to sound <b>natural and human</b> — "
    "not like it came straight from an AI.</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# User input
user_input = st.text_area(
    label="Enter your AI-generated or robotic text:",
    height=300,
    placeholder="Example: The following document outlines the procedural methodology..."
)

col1, col2 = st.columns([1, 1])

# Run button
with col1:
    check = st.button("✅ Check text")


# Handle check
if check:
    if not user_input.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Humanizing your text... 🤔"):
            result = get_human_written_text(user_input)
        st.success("✅ Done! Here's the humanized version:")
        st.text_area("Humanized Text:", value=result, height=250)


# Footer
st.markdown("---")
