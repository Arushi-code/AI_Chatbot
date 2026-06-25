import streamlit as st
import time
from chatbot.engine import ChatbotEngine
from datetime import datetime

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="AI Chatbot Pro",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>
.chat-container {
    max-width: 800px;
    margin: auto;
}

.timestamp {
    font-size: 10px;
    color: gray;
}

div[data-testid="stChatMessage"] {
    padding: 10px 15px;
    border-radius: 12px;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Backend ----------------
bot = ChatbotEngine()

# ---------------- Session State ----------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- Sidebar ----------------
with st.sidebar:
    st.title("🤖 AI Chatbot Pro")

    st.markdown("### Controls")

    if st.button("🧹 Clear Chat"):
        st.session_state.chat_history = []

    # Download chat
    if st.session_state.chat_history:
        chat_text = "\n".join(
            [f"{role.upper()}: {msg}" for role, msg, _ in st.session_state.chat_history]
        )
        st.download_button(
            "⬇️ Download Chat",
            chat_text,
            file_name="chat_history.txt"
        )

    st.markdown("---")
    st.markdown("Built with ❤️ using Streamlit")

# ---------------- Title ----------------
st.title("💬 AI Chat Assistant")

# ---------------- Chat Input ----------------
user_input = st.chat_input("Type your message...")

# ---------------- Response Logic ----------------
if user_input:
    timestamp = datetime.now().strftime("%H:%M")

    # user message
    st.session_state.chat_history.append(("user", user_input, timestamp))

    with st.chat_message("user"):
        st.markdown(user_input)
        st.caption(timestamp)

    # typing effect
    with st.chat_message("assistant"):
        with st.spinner("Bot is typing..."):
            time.sleep(0.6)

        result = bot.reply(user_input)
        response = result["response"]

        st.markdown(response)
        st.caption(timestamp)

    st.session_state.chat_history.append(("bot", response, timestamp))

# ---------------- Display History ----------------
for role, message, timestamp in st.session_state.chat_history:
    if role == "user":
        with st.chat_message("user"):
            st.markdown(message)
            st.caption(timestamp)
    else:
        with st.chat_message("assistant"):
            st.markdown(message)
<<<<<<< HEAD
            st.caption(timestamp)
=======
            st.caption(timestamp)
>>>>>>> 4e9049d (Add trained chatbot model files)
