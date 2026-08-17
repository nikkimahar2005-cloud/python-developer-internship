# Task 3 - AI Chatbot with NLP
# This chatbot uses NLTK to process user input
# and provide answers to common questions.

import nltk
import random
import string

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# Download required NLTK data
nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("wordnet")


# Create lemmatizer
lemmatizer = WordNetLemmatizer()


# Chatbot training data
intents = {
    "greeting": {
        "patterns": [
            "hello",
            "hi",
            "hey",
            "good morning",
            "good afternoon",
            "good evening"
        ],
        "responses": [
            "Hello! How can I help you?",
            "Hi! Nice to meet you.",
            "Hey! How can I assist you?"
        ]
    },

    "name": {
        "patterns": [
            "what is your name",
            "who are you",
            "tell me your name"
        ],
        "responses": [
            "My name is Python NLP Chatbot.",
            "I am an AI chatbot created using Python and NLTK."
        ]
    },

    "purpose": {
        "patterns": [
            "what can you do",
            "what is your purpose",
            "how can you help me"
        ],
        "responses": [
            "I can answer simple questions and have a basic conversation with you.",
            "I am designed to answer common user queries using NLP."
        ]
    },

    "python": {
        "patterns": [
            "what is python",
            "tell me about python",
            "what is python programming"
        ],
        "responses": [
            "Python is a popular programming language used for web development, data analysis, automation, AI and machine learning."
        ]
    },

    "nltk": {
        "patterns": [
            "what is nltk",
            "tell me about nltk",
            "what is natural language toolkit"
        ],
        "responses": [
            "NLTK stands for Natural Language Toolkit. It is a Python library used for working with human language and Natural Language Processing."
        ]
    },

    "thanks": {
        "patterns": [
            "thank you",
            "thanks",
            "thank you very much"
        ],
        "responses": [
            "You're welcome!",
            "Happy to help!",
            "No problem!"
        ]
    },

    "goodbye": {
        "patterns": [
            "bye",
            "goodbye",
            "see you",
            "exit",
            "quit"
        ],
        "responses": [
            "Goodbye! Have a great day!",
            "See you again!",
            "Bye! Take care!"
        ]
    }
}


def preprocess_text(text):
    """
    Tokenize and lemmatize the user's input.
    """
    tokens = word_tokenize(text.lower())

    # Remove punctuation
    tokens = [
        word for word in tokens
        if word not in string.punctuation
    ]

    # Lemmatize words
    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]

    return tokens


def get_response(user_input):
    """
    Find the most suitable response for the user's input.
    """

    user_tokens = preprocess_text(user_input)

    best_intent = None
    highest_score = 0

    for intent, data in intents.items():

        for pattern in data["patterns"]:

            pattern_tokens = preprocess_text(pattern)

            # Count matching words
            matching_words = set(user_tokens) & set(pattern_tokens)

            score = len(matching_words)

            if score > highest_score:
                highest_score = score
                best_intent = intent

    if best_intent and highest_score > 0:
        return random.choice(intents[best_intent]["responses"])

    return (
        "Sorry, I don't understand that question. "
        "Please try asking something else."
    )


def chatbot():
    """
    Start the chatbot conversation.
    """

    print("=" * 50)
    print("       PYTHON NLP CHATBOT")
    print("=" * 50)
    print("Type 'bye', 'exit', or 'quit' to end the chat.")
    print()

    while True:

        user_input = input("You: ")

        if not user_input.strip():
            print("Bot: Please type something.")
            continue

        response = get_response(user_input)

        print("Bot:", response)

        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break


# Start the chatbot
if __name__ == "__main__":
    chatbot()