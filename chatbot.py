# Finance-Chatbot
Finance Assistant Chatbot  A Python-based chatbot that answers basic finance and trading queries (forex, crypto, risk management). Uses rule-based NLP with intent matching and JSON data. Demonstrates conversational AI fundamentals and modular design for easy future enhancements.
import json
import random

def load_intents(file_path="intents.json"):
    """Load intents from a JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)

def find_response(user_input, intents_data):
    """Find a matching response based on user input."""
    user_input = user_input.lower()

    for intent in intents_data.get("intents", []):
        for pattern in intent.get("patterns", []):
            if pattern.lower() in user_input:
                return random.choice(intent.get("responses", []))

    return "Sorry, I didn't quite understand that."

def chatbot():
    """Run the chatbot loop."""
    print("Finance Chatbot (type 'quit' to exit)")
    intents_data = load_intents()

    while True:
        user_text = input("You: ").strip()

        if user_text.lower() == "quit":
            print("Bot: Goodbye!")
            break

        reply = find_response(user_text, intents_data)
        print(f"Bot: {reply}")

if __name__ == "__main__":
    chatbot()
