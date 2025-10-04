import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import pandas as pd
from datetime import datetime

# Load environment variables
load_dotenv()

# --- Page Configuration ---
st.set_page_config(
    page_title="VeriWell",
    page_icon="🌿",
    layout="wide",
)

# --- Custom CSS for a more polished UI ---
st.markdown("""
<style>
    /* Main container */
    .st-emotion-cache-1y4p8pa {
        padding-top: 2rem;
    }
    /* Main content area */
    .st-emotion-cache-1v0mbdj {
        padding-left: 2rem;
        padding-right: 2rem;
    }
    /* Sidebar styling */
    .st-emotion-cache-16txtl3 {
        padding: 1.5rem 1rem;
        background-color: #F0F2F6; /* Light grey background for sidebar */
    }
    /* Center align the main title */
    .st-emotion-cache-1kyxreq {
        justify-content: center;
    }
    h1 {
        color: #0a2959; /* Dark blue for main title */
        font-weight: bold;
    }
    h2, h3 {
        color: #0a2959; /* Dark blue for subheaders */
    }
    /* Style for the chat bubbles */
    .st-emotion-cache-1c7y2kd {
        background-color: #FFFFFF;
        border: 1px solid #E0E0E0;
        border-radius: 10px;
        padding: 1rem;
    }
    /* Style for user chat bubble */
    .st-emotion-cache-4oy321 {
         background-color: #E1F5FE; /* Light blue for user messages */
    }
</style>
""", unsafe_allow_html=True)


# --- AI Model and Session State Initialization ---
def initialize_session():
    """Initializes the AI model and session state variables."""
    try:
        # Configure the generative AI model with the API key
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

        # Initialize chat session in state if it doesn't exist
        if "chat_session" not in st.session_state:
            generation_config = {
              "temperature": 0.7, "top_p": 0.95, "top_k": 64,
              "max_output_tokens": 8192, "response_mime_type": "text/plain",
            }
            safety_settings = [
              {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
              {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
              {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
              {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            ]
            system_instruction = "You are VeriWell, a friendly and knowledgeable AI wellness coach. " \
            "Your purpose is to help college students understand the connection between their daily habits " \
            "and their overall well-being. Engage in supportive conversations, provide actionable advice on " \
            "topics like sleep, nutrition, exercise, and stress management. Keep your responses concise, " \
            "encouraging, and easy to understand. Ask clarifying questions to better understand the " \
            "student's needs and provide personalized recommendations."

            model = genai.GenerativeModel(
              model_name="gemini-pro-latest",
              safety_settings=safety_settings,
              generation_config=generation_config,
              system_instruction=system_instruction,
            )
            st.session_state.chat_session = model.start_chat(history=[])

        # Initialize habit history and insights
        if "habit_history" not in st.session_state:
            st.session_state.habit_history = []
        if "latest_insight" not in st.session_state:
            st.session_state.latest_insight = "Log your habits in the sidebar to get your first wellness insight!"

    except Exception as e:
        st.error(f"Failed to configure the AI model. Please check your API key. Error: {e}")
        st.stop()

initialize_session()

# --- Sidebar for Habit Logging ---
with st.sidebar:
    st.header("📝 Log Your Daily Habits")

    with st.form("habit_form"):
        sleep_hours = st.number_input("😴 How many hours did you sleep?", min_value=0.0, max_value=24.0, step=0.5, format="%.1f")
        stress_level = st.slider("😟 What's your stress level?", min_value=1, max_value=10, value=5)
        exercise_minutes = st.number_input("🏃‍♂️ How many minutes did you exercise?", min_value=0, step=10)

        submitted = st.form_submit_button("Log Habits & Get Insight")

        if submitted:
            log_entry = {"date": datetime.now(), "sleep": sleep_hours, "stress": stress_level, "exercise": exercise_minutes}
            st.session_state.habit_history.append(log_entry)

            with st.spinner("Analyzing your habits..."):
                habit_prompt = f"""
                As VeriWell, a wellness coach, analyze these habits for a college student:
                - Sleep: {sleep_hours} hours
                - Stress: {stress_level}/10
                - Exercise: {exercise_minutes} minutes
                Provide a brief, encouraging, and actionable insight (2-3 sentences). Focus on the most important area for improvement.
                """
                
                # Use a temporary model instance for this specific generation
                insight_model = genai.GenerativeModel(model_name="gemini-pro-latest")
                insight_response = insight_model.generate_content(habit_prompt)
                st.session_state.latest_insight = insight_response.text

                st.success("Insight generated! Check the Dashboard.")

# --- Main Page Layout ---
st.title("🌿 VeriWell")
st.write("Your AI wellness coach to help you connect daily habits to your well-being.")

chat_tab, dashboard_tab = st.tabs(["💬 Chat", "📊 Dashboard"])

# --- Chat Tab ---
with chat_tab:
    st.header("Chat with VeriWell")
    # Display chat history
    for message in st.session_state.chat_session.history:
        role = "assistant" if message.role == "model" else message.role
        with st.chat_message(role):
            st.markdown(message.parts[0].text)

    # Chat input
    if user_input := st.chat_input("Ask for wellness advice..."):
        with st.chat_message("user"):
            st.markdown(user_input)
        with st.spinner("VeriWell is thinking..."):
            try:
                response = st.session_state.chat_session.send_message(user_input)
                with st.chat_message("assistant"):
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred while communicating with the AI: {e}")

# --- Dashboard Tab ---
with dashboard_tab:
    st.header("Your Wellness Dashboard")

    # Display latest insight
    st.subheader("💡 Your Latest Insight")
    st.info(st.session_state.latest_insight)
    st.markdown("---")

    if not st.session_state.habit_history:
        st.info("Log your habits in the sidebar to see your wellness trends here!")
    else:
        df = pd.DataFrame(st.session_state.habit_history).set_index('date')

        st.subheader("Your Habit Trends")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Avg. Sleep", value=f"{df['sleep'].mean():.1f} hrs")
            st.line_chart(df['sleep'], color="#3498db") # Blue
        with col2:
            st.metric(label="Avg. Stress", value=f"{df['stress'].mean():.1f}/10")
            st.line_chart(df['stress'], color="#e74c3c") # Red
        with col3:
            st.metric(label="Avg. Exercise", value=f"{df['exercise'].mean():.0f} mins")
            st.line_chart(df['exercise'], color="#2ecc71") # Green