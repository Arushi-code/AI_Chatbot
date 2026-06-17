import json
import pickle
import random
import re
from pathlib import Path

import numpy as np

from chatbot.llm_helper import LLMHelper
from chatbot.nlp_utils import bag_of_words, ensure_nltk_data


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "intents.json"
MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "chatbot_model.keras"
WORDS_PATH = MODEL_DIR / "words.pkl"
CLASSES_PATH = MODEL_DIR / "classes.pkl"


class ChatbotEngine:
    def __init__(self):
        ensure_nltk_data()
        self.intents = self._load_intents()
        self.intent_map = {intent["tag"]: intent for intent in self.intents["intents"]}
        self.model = None
        self.words = []
        self.classes = []
        self.llm = LLMHelper()
        self._load_model_artifacts()

    def _load_intents(self):
        with DATA_PATH.open("r", encoding="utf-8") as file:
            return json.load(file)

    def _load_model_artifacts(self):
        if not MODEL_PATH.exists() or not WORDS_PATH.exists() or not CLASSES_PATH.exists():
            return

        self.model = load_model(MODEL_PATH)

        with WORDS_PATH.open("rb") as file:
            self.words = pickle.load(file)

        with CLASSES_PATH.open("rb") as file:
            self.classes = pickle.load(file)

    def reply(self, message):
        entities = self.extract_entities(message)
        intent = self.predict_intent(message)

        if intent is None:
            llm_response = self.generate_llm_fallback(message, entities)
            if llm_response:
                return {
                    "response": llm_response,
                    "intent": "llm_fallback",
                    "confidence": 0.0,
                    "entities": entities,
                    "source": "llm",
                }

            return {
                "response": "I am not fully trained for that yet. Try asking about AI, NLP, internships, tools, or project workflow.",
                "intent": "fallback",
                "confidence": 0.0,
                "entities": entities,
                "source": "rule_based_fallback",
            }

        response = self.generate_response(intent["intent"], entities)
        return {
            "response": response,
            "intent": intent["intent"],
            "confidence": round(intent["probability"], 4),
            "entities": entities,
            "source": "intent_classifier",
        }

    def predict_intent(self, message):
        if self.model is None:
            return self.rule_based_intent(message)

        bow = bag_of_words(message, self.words)
        prediction = self.model.predict(np.array([bow]), verbose=0)[0]
        best_index = int(np.argmax(prediction))
        probability = float(prediction[best_index])

        if probability < 0.25:
            return None

        return {"intent": self.classes[best_index], "probability": probability}

    def rule_based_intent(self, message):
        text = message.lower()
        keyword_map = {
            "greeting": [
                "hello",
                "hi",
                "hey",
                "good morning",
                "good evening",
                "are you there",
            ],
            "small_talk": [
                "how are you",
                "how are you doing",
                "how is it going",
                "what's up",
                "whats up",
                "how are things",
                "are you okay",
                "how do you feel",
            ],
            "bot_identity": ["who are you", "what are you", "tell me about yourself", "what can you do"],
            "bot_status": ["are you working", "are you online", "are you active", "are you available"],
            "goodbye": ["bye", "goodbye", "see you"],
            "thanks": ["thanks", "thank you"],
            "ai_definition": ["what is ai", "artificial intelligence", "define ai"],
            "nlp_definition": ["what is nlp", "natural language processing"],
            "deep_learning": ["deep learning", "neural network", "keras", "tensorflow"],
            "project_tools": ["tools", "technology", "python", "flask"],
            "internship_apply": ["internship", "apply", "resume"],
        }

        for intent, keywords in keyword_map.items():
            if any(keyword in text for keyword in keywords):
                return {"intent": intent, "probability": 0.5}

        return None

    def generate_response(self, intent_name, entities):
        intent = self.intent_map.get(intent_name)
        if not intent:
            return "I do not have a prepared response for that intent yet."

        response = random.choice(intent["responses"])

        if entities.get("name") and intent_name in {"greeting", "internship_apply"}:
            response = f"{response} Nice to meet you, {entities['name']}."

        if entities.get("email") and intent_name == "internship_apply":
            response = f"{response} I captured your email as {entities['email']}."

        return response

    def generate_llm_fallback(self, message, entities):
        try:
            return self.llm.generate_response(message, entities)
        except Exception:
            return None

    def extract_entities(self, message):
        entities = {}

        email_match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", message)
        phone_match = re.search(r"\b(?:\+?\d{1,3}[-.\s]?)?\d{10}\b", message)
        time_match = re.search(r"\b(?:[01]?\d|2[0-3])(?::[0-5]\d)?\s?(?:am|pm)?\b", message, re.IGNORECASE)
        date_match = re.search(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", message)
        name_match = re.search(r"\b(?:my name is|call me|i am|i'm)\s+([A-Z][a-zA-Z]+)\b", message)

        course_keywords = ["python", "ai", "artificial intelligence", "nlp", "deep learning", "machine learning", "flask"]
        found_courses = [keyword for keyword in course_keywords if keyword in message.lower()]

        if email_match:
            entities["email"] = email_match.group(0)
        if phone_match:
            entities["phone"] = phone_match.group(0)
        if time_match:
            entities["time"] = time_match.group(0)
        if date_match:
            entities["date"] = date_match.group(0)
        if name_match:
            entities["name"] = name_match.group(1)
        if found_courses:
            entities["topics"] = found_courses

        return entities
