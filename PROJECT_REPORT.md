# Project Report: AI Chatbot Using NLP and Deep Learning

## 1. Title

AI Chatbot Using NLP, Deep Learning, and LLMs

## 2. Objective

The objective of this project is to develop an AI chatbot that can answer frequently asked questions and perform simple conversations using Natural Language Processing, a deep learning backend, and optional LLM-based fallback responses.

## 3. Problem Statement

Many users need quick answers to common questions without waiting for human support. A chatbot can automate these interactions by understanding user messages, identifying the user's intent, extracting useful entities, and generating an appropriate response.

## 4. Proposed Solution for this problem statement

This project uses a neural network intent classifier trained on predefined conversational patterns. The chatbot processes the user's text, predicts the intent, extracts simple entities, and returns a response from the matching intent category. If the classifier confidence is low, the system can use an LLM fallback to generate a more flexible answer.

## 5. Technologies Used

- Python for core implementation
- NLTK for tokenization and lemmatization
- TensorFlow/Keras for deep learning model development
- OpenAI API for optional LLM response generation
- Flask and Streamlit for web deployment
- HTML, CSS, and JavaScript for the user interface
- JSON for the intent dataset

## 6. System Modules

### 6.1 NLP Preprocessing

The chatbot uses NLTK to tokenize user sentences and lemmatize words. This reduces words to their base form and improves matching between training data and user input.

### 6.2 Intent Classification

The training script converts sentences into bag-of-words vectors. A Keras neural network is trained to classify each input sentence into one of the available intent categories.

### 6.3 Entity Recognition

The project includes lightweight entity recognition using regular expressions and keyword rules. It can detect:

- Names
- Email addresses
- Phone numbers
- Dates
- Times
- AI-related topics

### 6.4 Response Generation

After predicting the intent, the chatbot chooses a response from the corresponding response list in the intent dataset. If entities are detected, the chatbot can include them in the reply.

### 6.5 LLM Fallback Response Generation

When the neural network classifier is not confident enough, the chatbot can send the user message and extracted entities to an LLM. This improves simple conversation handling while preserving the core NLP and deep learning pipeline.

### 6.6 Web Deployment

The project supports two deployment options:

- Flask website through `app.py`
- Streamlit app through `streamlit_app.py`

The Flask app exposes:

- `/` for the chatbot interface
- `/chat` for chatbot API requests

The Streamlit app provides a fast interactive deployment with a chat interface, model output sidebar, and example prompt buttons.

## 7. Deep Learning Model

The neural network architecture contains:

- Input layer matching the vocabulary size
- Dense hidden layer with ReLU activation
- Dropout layer to reduce overfitting
- Second Dense hidden layer
- Output layer with Softmax activation

The model is trained using categorical cross-entropy loss and the SGD optimizer.

## 8. Dataset

The dataset is stored in `data/intents.json`. Each intent contains:

- `tag`: intent name
- `patterns`: sample user inputs
- `responses`: possible chatbot replies

## 9. Expected Output

Example:

User:

```text
What is NLP?
```

Bot:

```text
Natural Language Processing is a branch of AI that helps computers understand, process, and generate human language.
```

Example with entity extraction:

User:

```text
My email is student@example.com
```

Bot detects:

```json
{
  "email": "student@example.com"
}
```

## 10. Advantages

- Easy to understand and extend
- Uses real NLP preprocessing
- Includes a trainable deep learning backend
- Provides both backend logic and web deployment
- Suitable for internship demonstration and portfolio use

## 11. Limitations

- The chatbot depends on the quality and size of the intent dataset
- Entity recognition is rule-based and limited
- The model does not generate fully original long-form answers
- More training data is needed for production-level accuracy

## 12. Future Enhancements

- Add more intents and training examples
- Use word embeddings or transformer models
- Add database storage for chat history
- Improve entity recognition with spaCy
- Add voice input and multilingual support
- Deploy the app on a cloud platform

## 13. Conclusion

This project demonstrates how NLP and deep learning can be combined to build a practical chatbot. It covers preprocessing, intent classification, entity extraction, response generation, and Flask-based deployment, making it suitable for an AI internship project.
The added LLM fallback makes the chatbot more flexible while still demonstrating the custom-built NLP and deep learning modules required for an internship project.
