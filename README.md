# AI Chatbot Using NLP and Deep Learning

An internship-ready Python project that builds a simple FAQ and conversational chatbot using NLP preprocessing, deep learning-based intent classification, lightweight entity recognition, optional LLM fallback responses, and live web deployments via Flask and Streamlit.

## 🎯 Project Goal

Develop an interactive AI chatbot capable of answering FAQs and carrying out contextual conversations using robust Natural Language Processing (NLP) techniques and deep learning classifiers.

## 🛠️ Tools Used

- **Python** (Core Development)
- **NLTK** (Text Preprocessing, Tokenization, Lemmatization)
- **TensorFlow / Keras** (Deep Learning Intent Classification)
- **Flask** (Full-featured Web App Interface)
- **Streamlit** (Rapid UI Prototyping & Live Cloud Deployment)
- **NumPy** (Numerical Computations & Vector Operations)
- **OpenAI API** (Optional LLM Fallback Mechanism)

## ✨ Features

- **Intent Classification**: Deep neural network architecture built with Keras.
- **NLP Pipeline**: Automated tokenization, cleaning, and lemmatization via NLTK.
- **Feature Extraction**: Bag-of-Words (BoW) vector representation for model input.
- **Rule-Based Entity Recognition**: Custom regex and keyword pipelines to extract critical information (emails, names, dates, course names, phone numbers).
- **Hybrid Response Generation**: Match engine responds based on confidence thresholds.
- **LLM Fallback Module**: Routes low-confidence inputs to OpenAI (`gpt-4o-mini`) to eliminate "I don't understand" dead-ends.
- **Dual-Frontends**: 
  - **Flask App**: Features a landing page dashboard, architectural breakdown, module overviews, and live trace panels.
  - **Streamlit App**: Features a streamlined conversational interface, real-time sidebar model trace data, and ready-to-test example prompts.
- **Extendable Knowledge Base**: Organized via a clean, structured JSON format (`intents.json`).

---

## 📂 Project Structure

```text
ai_nlp_deep_learning_chatbot/
  ├── app.py                  # Flask Application Entry Point
  ├── streamlit_app.py        # Streamlit Application Entry Point
  ├── train.py                # Deep Learning Model Training Script
  ├── requirements.txt        # Python Dependencies
  ├── README.md               # Project Documentation
  ├── data/
  │   └── intents.json        # Structured Intent Dataset (JSON)
  ├── chatbot/
  │   ├── __init__.py
  │   ├── engine.py           # Core Response Matcher & Pipeline Execution
  │   ├── llm_helper.py       # OpenAI Fallback Integration
  │   └── nlp_utils.py        # Tokenization & Lemmatization Utilities
  ├── models/
  │   ├── chatbot_model.keras # Saved Trained Keras Neural Network
  │   ├── words.pkl           # Pickled Preprocessing Vocabulary
  │   └── classes.pkl         # Pickled Classification Target Classes
  ├── static/
  │   └── style.css           # Flask Custom Styling
  └── templates/
      └── index.html          # Flask Web UI Template
```

---

## ⚙️ How It Works

1. **Data Ingestion**: Training pattern text and respective tags are ingested from `data/intents.json`.
2. **Text Standardization**: Sentences are tokenized into word arrays, down-cased, and lemmatized using NLTK algorithms.
3. **Vocabulary Assembly**: Unique word lists and target intent classes are compiled and pickled (`words.pkl`, `classes.pkl`).
4. **Vectorization**: Sentences convert into a mathematical binary Bag-of-Words representation.
5. **Model Inference**: A dense Keras Sequential neural network learns mappings to accurately predict corresponding intent tags.
6. **Execution Pipeline**:
   - The user inputs a query.
   - The engine extracts custom rule-based entities (e.g., detecting names or emails).
   - If the intent prediction crosses the confidence threshold, a predefined response is fired.
   - If confidence falls below the cutoff, it falls back to the OpenAI LLM helper (if API keys are valid).

---

## 🚀 Setup & Installation

### 1. Initialize Virtual Environment
```bash
python -m venv .venv
```
Activate the environment:
* **Windows**: `.venv\Scripts\activate`
* **macOS/Linux**: `source .venv/bin/activate`

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables (Optional LLM Fallback)
Create a `.env` or `.env.local` file in the root directory to store your credentials:
```text
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
```
*Note: The system functions completely without this file; it will simply skip the LLM generation step for low-confidence inputs.*

---

## 📊 Running the Project

### Phase 1: Train the Model
You must train the intent classifier before starting either web server:
```bash
python train.py
```

### Phase 2: Launch the Applications

#### Option A: Run the Flask Web Site
```bash
python app.py
```
* Access the app in your browser at: `http://127.0.0.1:5000`
* Includes: Dashboard, model tracing, workflow architecture diagrams, and system component breakdowns.

#### Option B: Run the Streamlit Interface
```bash
streamlit run streamlit_app.py
```
* Access the app in your browser at: `http://localhost:8501`
* Includes: Chat view, structured entity/confidence sidebar parsing, and clickable prompt suggestions.

---

## 📝 Example Prompts for Testing

### Conversational / Greeting
- *Hello!*
- *How are you doing?*
- *Who are you?*
- *Are you online?*

### Project / Technical Questions
- *What is artificial intelligence?*
- *What tools are used in this project?*
- *How does the chatbot work?*
- *Explain this project for my viva / presentation.*
- *How can I improve this chatbot?*

### Entity Extraction Prompts
- *I want to apply for an internship.*
- *My email is student@example.com*
- *Call me Rahul.*

---

## 🛠️ Extending the Chatbot Knowledge Base

To add custom functionality or unique chat tracks, modify `data/intents.json`:

```json
{
  "tag": "new_custom_intent",
  "patterns": [
    "example user question 1",
    "how do i ask this alternative question"
  ],
  "responses": [
    "This is the immediate chatbot response.",
    "Alternative varied response from the bot."
  ]
}
```
*Important: Always rerun `python train.py` after editing this file to rebuild the neural network paths.*


## 🎯 Internship Learning Outcomes

- Formulate end-to-end NLP text preprocessing pipelines.
- Build, compile, and evaluate multi-class Dense Neural Networks using Keras.
- Construct complex regular expression patterns for entities.
- Implement API middleware layers (OpenAI) to support intelligent application fallbacks.
- Develop and deploy multi-framework production endpoints using both Flask and Streamlit ecosystems.
