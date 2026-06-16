import streamlit as st

from chatbot.engine import ChatbotEngine


st.set_page_config(
    page_title="AI NLP Chatbot",
    page_icon="AI",
    layout="wide",
)


@st.cache_resource
def load_bot():
    return ChatbotEngine()


bot = load_bot()

st.title("AI Chatbot Using NLP, Deep Learning, and LLMs")
st.caption("Ask me Anything related to the project")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! Ask me about AI, NLP, deep learning, chatbot workflow, tools, viva questions, or internship guidance.",
        }
    ]

if "last_result" not in st.session_state:
    st.session_state.last_result = {
        "intent": "-",
        "confidence": "-",
        "entities": {},
        "source": "-",
    }

with st.sidebar:
    st.header("Model Output")
    st.metric("Intent", st.session_state.last_result.get("intent", "-"))
    st.metric("Confidence", st.session_state.last_result.get("confidence", "-"))
    st.write("Response Source")
    st.code(st.session_state.last_result.get("source", "-"))
    st.write("Entities")
    st.json(st.session_state.last_result.get("entities", {}))

    st.divider()
    st.subheader("Try Greetings")
    greeting_prompt = st.button("How are you doing?")
    identity_prompt = st.button("Who are you?")

    st.subheader("Try Project Questions")
    nlp_prompt = st.button("What is NLP?")
    workflow_prompt = st.button("How does this chatbot work?")
    viva_prompt = st.button("Explain this project for my viva")


def submit_message(message):
    st.session_state.messages.append({"role": "user", "content": message})
    result = bot.reply(message)
    st.session_state.messages.append({"role": "assistant", "content": result["response"]})
    st.session_state.last_result = result


selected_prompt = None
if greeting_prompt:
    selected_prompt = "How are you doing?"
elif identity_prompt:
    selected_prompt = "Who are you?"
elif nlp_prompt:
    selected_prompt = "What is NLP?"
elif workflow_prompt:
    selected_prompt = "How does this chatbot work?"
elif viva_prompt:
    selected_prompt = "Explain this project for my viva"

if selected_prompt:
    submit_message(selected_prompt)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Ask about the project...")
if user_input:
    submit_message(user_input)
    st.rerun()

