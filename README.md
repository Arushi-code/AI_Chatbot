<<<<<<< HEAD
# AI Chatbot Using NLP and Deep Learning

An internship-ready Python project that builds a simple FAQ and conversational chatbot using NLP preprocessing, deep learning based intent classification, lightweight entity recognition, optional LLM fallback responses, and Flask deployment.

## Project Goal

Develop an AI chatbot capable of answering FAQs and carrying simple conversations using NLP techniques.

## Tools Used

- Python
- NLTK
- TensorFlow / Keras
- Flask
- Streamlit
- NumPy
- OpenAI API for optional LLM fallback

## Features

- Intent classification using a neural network
- Tokenization and lemmatization with NLTK
- Bag-of-words feature extraction
- Simple entity recognition using regex and keyword rules
- Response generation using confidence-based intent matching
- Optional LLM fallback for flexible answers when intent confidence is low
- Full Flask website with live chatbot, architecture section, module overview, examples, and model trace panel
- JSON-based intent dataset that is easy to extend

## Project Structure

```text
ai_nlp_deep_learning_chatbot/
  app.py
  streamlit_app.py
  train.py
  requirements.txt
  README.md
  data/
    intents.json
  chatbot/
    __init__.py
    engine.py
    llm_helper.py
    nlp_utils.py
  models/
    .gitkeep
  static/
    style.css
  templates/
    index.html
```

## How It Works

1. Training patterns are loaded from `data/intents.json`.
2. Text is tokenized, cleaned, and lemmatized using NLTK.
3. A vocabulary and intent label list are created.
4. Each sentence is converted into a bag-of-words vector.
5. A Keras neural network learns to classify the user's intent.
6. During chat, the predicted intent is used to select a response.
7. Entity rules extract simple values such as email addresses, phone numbers, dates, times, course names, and names.
8. If the classifier confidence is low and `OPENAI_API_KEY` is available, an LLM generates a helpful fallback answer.

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Optional LLM setup:

Create a `.env.local` file or set an environment variable:

```text
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

The chatbot still works without an API key, but LLM fallback answers will be disabled.

## Train The Model

```bash
python train.py
```

This creates:

- `models/chatbot_model.keras`
- `models/words.pkl`
- `models/classes.pkl`

## Run The Flask App

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Run The Streamlit App

```bash
streamlit run streamlit_app.py
```

Open:

```text
http://localhost:8501
```

The Streamlit version includes the chatbot interface, sidebar model output, example greeting prompts, and example project FAQ prompts.

The website includes:

- First-screen chatbot demo
- Live model output panel
- NLP, deep learning, entity recognition, and LLM module overview
- Hybrid workflow explanation
- Example prompts for testing

## Example Questions

- Hello
- How are you doing?
- Who are you?
- Are you online?

Project questions:

- What is artificial intelligence?
- What tools are used in this project?
- How does the chatbot work?
- Explain this project for my viva
- How can I improve this chatbot?
- I want to apply for an internship
- My email is student@example.com
- Call me Rahul
- Thank you

## Extend The Chatbot

Add new intents in `data/intents.json`:

```json
{
  "tag": "new_intent",
  "patterns": ["example user sentence"],
  "responses": ["example bot response"]
}
```

Then retrain:

```bash
python train.py
```

## Internship Learning Outcomes

- Understand NLP preprocessing and feature extraction
- Build a neural network classifier with Keras
- Implement basic entity recognition
- Integrate an LLM fallback module
- Connect ML inference with a Flask web app
- Package an AI project in a clear, reusable structure
=======
# AI_Chatbot
>>>>>>> 6352fed086e71c69ff0125b812996abd4982d26d
