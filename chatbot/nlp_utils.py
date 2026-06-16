import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()


def ensure_nltk_data():
    resources = {
        "punkt": "tokenizers/punkt",
        "wordnet": "corpora/wordnet",
        "omw-1.4": "corpora/omw-1.4",
    }

    for package, resource_path in resources.items():
        try:
            nltk.data.find(resource_path)
        except LookupError:
            nltk.download(package)


def clean_tokens(tokens):
    return {lemmatizer.lemmatize(token.lower()) for token in tokens}


def tokenize_and_lemmatize(sentence):
    tokens = nltk.word_tokenize(sentence)
    return [lemmatizer.lemmatize(token.lower()) for token in tokens]


def bag_of_words(sentence, vocabulary):
    sentence_words = tokenize_and_lemmatize(sentence)
    bag = [0] * len(vocabulary)

    for word in sentence_words:
        for index, vocab_word in enumerate(vocabulary):
            if vocab_word == word:
                bag[index] = 1

    return np.array(bag)

