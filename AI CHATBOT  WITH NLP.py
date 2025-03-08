import nltk
import random
import re

# Download NLTK resources for tokenization and wordnet
nltk.download('punkt')
nltk.download('wordnet')

# Sample responses categorized by intent
responses = {
    "greeting": ["Hello!", "Hi there!", "Greetings!", "How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Glad to help!"],
    "default": ["I'm sorry, I don't understand that.", "Can you rephrase that?", "I'm not sure how to respond to that."]
}

# Predefined patterns to match user input with corresponding response keys
patterns = {
    r'hi|hello|hey': "greeting",  # Matches greetings
    r'bye|goodbye': "goodbye",     # Matches farewells
    r'thank(s| you)': "thanks"     # Matches expressions of gratitude
}

# Function to preprocess user input
def preprocess_input(user_input):
    # Convert input to lowercase
    user_input = user_input.lower()
    # Remove extra spaces
    user_input = re.sub(r'\s+', ' ', user_input)
    return user_input

# Function to get a response based on user input
def get_response(user_input):
    # Preprocess the user input
    user_input = preprocess_input(user_input)
    
    # Check each pattern to find a match
    for pattern, response_key in patterns.items():
        if re.search(pattern, user_input):  # If the pattern matches the user input
            return random.choice(responses[response_key])  # Return a random response from the matched category
    
    # If no patterns match, return a default response
    return random.choice(responses["default"])

# Main chatbot loop
def chatbot():
    print("Chatbot: Hello! I'm a simple chatbot. Type 'exit' to end the conversation.")
    
    while True:
        # Get user input
        user_input = input("You: ")
        # Check if the user wants to exit the chat
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")  # Farewell message
            break  # Exit the loop
        
        # Get a response based on the user input
        response = get_response(user_input)
        # Print the chatbot's response
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()