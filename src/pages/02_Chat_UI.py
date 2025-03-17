import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from promptTemplate import generate_system_message
from logger import logging
import os
import random

# Load environment variables
load_dotenv()
openai_api_key = os.getenv("openai_api_key")

# Streamlit Page Configuration
st.set_page_config(page_title="Chat UI", layout="wide")
st.title("💬 AI Interview Chat")

logging.info("Streamlit application started.")

# Restrict access if form is not submitted
if "interview_started" not in st.session_state or not st.session_state.interview_started:
    logging.warning("User attempted to access chat without completing the Candidate Form.")
    st.warning("🚨 Please complete the Candidate Form first before accessing the chat.")
    st.stop()

if "candidate_data" not in st.session_state or not st.session_state.candidate_data:
    logging.error("Candidate data is missing.")
    st.error("⚠️ Candidate data is missing. Please submit the form again.")
    st.stop()

# List of required fields
required_fields = ["name", "email", "phone", "experience", "position", "location", "tech_stack"]

# Check for missing fields
missing_fields = [field for field in required_fields if not st.session_state.candidate_data.get(field)]

if missing_fields:
    logging.error(f"Missing required candidate fields: {missing_fields}")
    st.error(f"⚠️ Missing required fields: {', '.join(missing_fields)}. Please complete the form.")
    st.stop()

logging.info("All required candidate fields are present.")

candidate_data = st.session_state.candidate_data
logging.info(f"Candidate data retrieved: {candidate_data}")

# Generate System Message
system_message = generate_system_message(candidate_data)
logging.info("System message generated.")

# Initialize Chat Model
try:
    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5, api_key=openai_api_key)
    logging.info("ChatOpenAI model initialized successfully.")
except Exception as e:
    logging.error(f"Error initializing ChatOpenAI: {e}")
    st.error("⚠️ Failed to initialize AI model. Please check API settings.")
    st.stop()

# Fixed Chat History (No session state)
chat_history = [SystemMessage(content=system_message.content)]

# AI Greeting - Add only if it's the first time chat is started
if "messages" not in st.session_state:
    st.session_state.messages = []
    
    greeting_message = f"Hello {candidate_data['name']}! 😊 Welcome to your AI interview session. I'm here to assist you. Feel free to ask me anything related to your interview. 🚀"
    
    st.session_state.messages.append({"role": "assistant", "content": greeting_message})

# Display Chat History (Avoids duplicate greeting)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
user_input = st.chat_input("Type your message...")

EXIT_COMMANDS = {"exit", "quit", "stop", "end", "goodbye", "bye"}

# Define fallback responses
FALLBACK_RESPONSES = [
    "Could you please clarify your question?",
    "I'm here to discuss technical topics. Could you provide more details?",
    "That doesn't seem related to the interview. Let's focus on technical aspects.",
    "I didn’t quite understand. Can you rephrase your question?",
]

# Check if chat has already ended
if "chat_ended" in st.session_state and st.session_state.chat_ended:
    st.warning("🚨 Chat session has ended. Please refresh the page to start a new session.")
    st.stop()

if user_input:
    logging.info(f"User input received: {user_input}")

    # Check if user wants to exit
    if user_input.strip().lower() in EXIT_COMMANDS:
        farewell_message = "Thank you for your time! 😊 I enjoyed our discussion. Best of luck in your interview! 🎯"
        st.session_state.messages.append({"role": "assistant", "content": farewell_message})
        
        with st.chat_message("assistant"):
            st.markdown(farewell_message)
         
        st.session_state.chat_ended = True
        logging.info("User exited the chat session.")
        st.stop()  # End execution to stop further chat processing

    # Add user message to session
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    # Append user input to chat history
    chat_history.append(HumanMessage(content=user_input))

    try:
        # Generate AI response
        ai_response = model.invoke(chat_history)

        # If AI response is empty or nonsensical, use a fallback response
        if not ai_response or not ai_response.content.strip():
            fallback_message = random.choice(FALLBACK_RESPONSES)
            logging.warning(f"AI generated an unclear response. Using fallback: {fallback_message}")
            ai_response = AIMessage(content=fallback_message)

        chat_history.append(AIMessage(content=ai_response.content))

        # Store AI response in session
        st.session_state.messages.append({"role": "assistant", "content": ai_response.content})

        with st.chat_message("assistant"):
            st.markdown(ai_response.content)

        logging.info(f"AI response generated: {ai_response.content}")

    except Exception as e:
        logging.error(f"Error generating AI response: {e}")
        fallback_message = random.choice(FALLBACK_RESPONSES)
        st.session_state.messages.append({"role": "assistant", "content": fallback_message})

        with st.chat_message("assistant"):
            st.markdown(fallback_message)
        
        st.error("⚠️ An error occurred while processing your message. Please try again.")
