import json
import pickle
import random
from pathlib import Path

import nltk
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD

from chatbot.nlp_utils import bag_of_words, clean_tokens, ensure_nltk_data


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "intents.json"
MODEL_DIR = BASE_DIR / "models"
MODEL_PATH = MODEL_DIR / "chatbot_model.keras"
WORDS_PATH = MODEL_DIR / "words.pkl"
CLASSES_PATH = MODEL_DIR / "classes.pkl"


def load_intents():
    with DATA_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def build_training_data(intents):
    words = []
    classes = []
    documents = []
    ignore_letters = {"?", "!", ".", ","}

    for intent in intents["intents"]:
        tag = intent["tag"]
        if tag not in classes:
            classes.append(tag)

        for pattern in intent["patterns"]:
            tokens = nltk.word_tokenize(pattern)
            words.extend(tokens)
            documents.append((pattern, tag))

    words = sorted(set(clean_tokens(words) - ignore_letters))
    classes = sorted(set(classes))

    training = []
    output_empty = [0] * len(classes)

    for pattern, tag in documents:
        bow = bag_of_words(pattern, words)
        output_row = output_empty[:]
        output_row[classes.index(tag)] = 1
        training.append([bow, output_row])

    random.shuffle(training)
    train_x = np.array([item[0] for item in training])
    train_y = np.array([item[1] for item in training])

    return words, classes, train_x, train_y


def create_model(input_size, output_size):
    model = Sequential(
        [
            Dense(128, input_shape=(input_size,), activation="relu"),
            Dropout(0.5),
            Dense(64, activation="relu"),
            Dropout(0.5),
            Dense(output_size, activation="softmax"),
        ]
    )

    optimizer = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
    model.compile(loss="categorical_crossentropy", optimizer=optimizer, metrics=["accuracy"])
    return model


def main():
    ensure_nltk_data()
    MODEL_DIR.mkdir(exist_ok=True)

    intents = load_intents()
    words, classes, train_x, train_y = build_training_data(intents)

    model = create_model(len(train_x[0]), len(train_y[0]))
    model.fit(train_x, train_y, epochs=250, batch_size=5, verbose=1)

    model.save(MODEL_PATH)

    with WORDS_PATH.open("wb") as file:
        pickle.dump(words, file)

    with CLASSES_PATH.open("wb") as file:
        pickle.dump(classes, file)

    print("Training complete.")
    print(f"Model saved to: {MODEL_PATH}")


if __name__ == "__main__":
    main()

