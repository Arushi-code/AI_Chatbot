import streamlit as st
from chatbot.engine import ChatbotEngine

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Sidebar ----------------
with st.sidebar:
    st.title("🤖 AI Chatbot")
    st.markdown("### About")
    st.write("This is an AI chatbot using NLP + ML + fallback LLM.")
    
    if st.button("Clear Chat"):
        st.session_state.chat_history = []

# ---------------- Main UI ----------------
st.title("💬 Chat Assistant")

bot = ChatbotEngine()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- Chat Input ----------------
user_input = st.chat_input("Type your message...")

# ---------------- Response Handling ----------------
if user_input:
    result = bot.reply(user_input)
    bot_response = result["response"]

    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("bot", bot_response))

# ---------------- Chat Display ----------------
for role, message in st.session_state.chat_history:
    if role == "user":
        with st.chat_message("user"):
            st.markdown(f"**You:** {message}")
    else:
        with st.chat_message("assistant"):
            st.markdown(f"**Bot:** {message}")
