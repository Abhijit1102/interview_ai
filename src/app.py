import streamlit as st

# Configure page settings
st.set_page_config(page_title="Candidate Interview App", layout="wide")

# Custom CSS for improved UI
st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #4A90E2;
            text-align: center;
        }
        .subtitle {
            font-size: 20px;
            color: #666;
            text-align: center;
        }
        .instructions {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 10px;
            margin: 20px 0;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown('<h1 class="title">🤖 AI Interview Chatbot</h1>', unsafe_allow_html=True)

# Subtitle
st.markdown('<p class="subtitle">Your AI-powered assistant for automated interviews</p>', unsafe_allow_html=True)

# Instructions Box
st.markdown("""
    <div class="instructions">
        <h3>📌 How to Get Started</h3>
        <ol>
            <li><b>Go to the Candidate Form</b> and enter your details.</li>
            <li>Submit the form to unlock the Chatbot.</li>
            <li>Once submitted, navigate to the Chat UI and start chatting!</li>
        </ol>
        <b>⚠️ Note:</b> The Chat UI will remain locked until you complete the form.
    </div>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
st.sidebar.success("➡️ Select a page above to begin!")

# Call-to-action buttons
col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/01_Candidate_Form.py", label="📝 Fill Candidate Form", icon="📝")
with col2:
    st.page_link("pages/02_Chat_UI.py", label="💬 Access Chatbot", icon="💬")

# Footer
st.markdown("<br><hr><p style='text-align: center; color: #888;'>© 2024 AI Interview Chatbot. All rights reserved.</p>", unsafe_allow_html=True)
