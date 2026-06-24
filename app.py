import streamlit as st
from chatbot.engine import ChatbotEngine

st.set_page_config(page_title="AI Chatbot", layout="centered")

st.title("🤖 AI Chatbot")

bot = ChatbotEngine()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:")

if user_input:
    response = bot.get_response(user_input)

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

for sender, msg in st.session_state.chat_history:
    st.write(f"**{sender}:** {msg}")
