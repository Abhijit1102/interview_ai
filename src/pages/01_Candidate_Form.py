import streamlit as st
from logger import logging

st.set_page_config(page_title="Candidate Form", layout="wide")

st.title("📋 Candidate Information Form")

# Initialize session state variables
if "candidate_data" not in st.session_state:
    st.session_state.candidate_data = {}
if "interview_started" not in st.session_state:
    st.session_state.interview_started = False

logging.info("Candidate Form page loaded.")

with st.form(key="candidate_form"):
    name = st.text_input("Full Name", value="")
    email = st.text_input("Email", value="")
    phone = st.text_input("Phone Number", value="")
    experience = st.selectbox("Years of Experience", options=[str(i) for i in range(1, 21)], index=None, placeholder="Select years of experience")
    position = st.text_input("Position Applied For", value="")
    location = st.text_input("Location", value="")
    tech_stack = st.text_area("Tech Stack (comma separated)", value="")

    submit_button = st.form_submit_button("Submit")

if submit_button:
    if not name or not email or not phone or not experience or not position or not location or not tech_stack:
        st.error("🚨 All fields are required! Please fill in all details before submitting.")
        logging.warning("Form submission failed: Some fields were left empty.")
    else:
        logging.info(f"Form submitted by candidate: {name}, Email: {email}")

        st.session_state.candidate_data = {
            "name": name,
            "email": email,
            "phone": phone,
            "experience": experience,
            "position": position,
            "location": location,
            "tech_stack": tech_stack
        }
        st.session_state.interview_started = True

        logging.info(f"Candidate data stored in session: {st.session_state.candidate_data}")

        st.success(f"✅ Form submitted! Interview started for {name}.")

        # Display submitted data
        st.write("### Submitted Information:")
        st.json(st.session_state.candidate_data)

        logging.info("Candidate redirected to chat page.")

        # Button to go to chat page
        st.page_link("pages/02_Chat_UI.py", label="Go to Chat UI →", icon="💬")
