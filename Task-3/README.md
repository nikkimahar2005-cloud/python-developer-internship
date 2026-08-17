# Task 3 - AI Chatbot with NLP

## Project Title

AI Chatbot using Natural Language Processing

## Objective

The objective of this project is to build a simple chatbot using Python and Natural Language Processing (NLP). The chatbot uses the NLTK library to process user input and provide suitable responses to common questions.

## Technologies Used

- Python
- NLTK
- Natural Language Processing

## Project Features

- Accepts user queries through the terminal
- Processes user input using NLP techniques
- Uses tokenization to process text
- Uses lemmatization to normalize words
- Identifies the user's query
- Provides suitable responses
- Handles greetings and common questions
- Provides information about Python and NLTK
- Allows the user to end the conversation

## Project Structure

```text
Task-3/
│
├── chatbot.py
├── requirements.txt
└── README.md
```

## How to Run

### Step 1 - Install Required Libraries

Open the terminal in the project folder and run:

```bash
pip install -r requirements.txt
```

### Step 2 - Run the Chatbot

```bash
python chatbot.py
```

## Example Conversation

```text
==================================================
       PYTHON NLP CHATBOT
==================================================
Type 'bye', 'exit', or 'quit' to end the chat.

You: hello
Bot: Hello! How can I help you?

You: what is python
Bot: Python is a popular programming language used for web development, data analysis, automation, AI and machine learning.

You: what is nltk
Bot: NLTK stands for Natural Language Toolkit. It is a Python library used for working with human language and Natural Language Processing.

You: bye
Bot: Goodbye! Have a great day!
```

## Working Process

```text
User Enters Query
        ↓
Tokenize User Input
        ↓
Remove Punctuation
        ↓
Lemmatize Words
        ↓
Compare with Known Patterns
        ↓
Find Matching Intent
        ↓
Generate Response
        ↓
Display Response
```

## NLP Techniques Used

### Tokenization

Tokenization divides the user's sentence into individual words.

### Lemmatization

Lemmatization converts words into their basic or root form to help the chatbot compare words more effectively.

### Pattern Matching

The chatbot compares the processed user input with predefined patterns and selects the most suitable response.

## Conclusion

This project demonstrates how Python and NLTK can be used to build a simple Natural Language Processing chatbot. The chatbot can understand common user queries and provide appropriate responses using text processing and pattern matching techniques.

## Internship Task

Task 3 - AI Chatbot with NLP