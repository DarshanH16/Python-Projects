import nltk
import random
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to assist you.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!", "I'm fine, thank you!",]
    ],
    [
        r"(.*) sorry (.*)",
        ["It's okay, no worries.", "No problem, don't apologize.",]
    ],
    [
        r"(.*) (happy|excited|good|great)",
        ["That's fantastic!", "I'm glad to hear that!",]
    ],
    [
        r"(.*) (sad|disappointed|bad|unhappy)",
        ["I'm sorry to hear that. Is there anything I can do to help?",]
    ],
    [
        r"(.*) (hungry|eat|food)",
        ["I'm just a computer program and don't need to eat, but I'm here to talk to you!",]
    ],
    [
        r"(.*) (sleepy|tired|rest)",
        ["I don't sleep, but I'm always here to chat with you!",]
    ],
    [
        r"(.*) (love|hate) (.*)",
        ["Love and hate are complex emotions. What specifically do you love/hate about %3?",]
    ],
    [
        r"what are your hobbies?",
        ["I enjoy helping people and chatting with users like you!",]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!",]
    ],
    [
        r"(.*) (movie|book|TV show)",
        ["I don't watch movies, read books, or watch TV shows, but I can recommend some based on your preferences!",]
    ],
    [
        r"(.*) (recommend|suggest) (.*)",
        ["Sure, I can suggest something. What genre are you interested in?",]
    ],
    [
        r"(.*) (genre)",
        ["Some popular genres include action, comedy, drama, horror, romance, science fiction, and fantasy.",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye, have a great day!",]
    ],
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def personal_chat():
    print("Hi! I'm your personal chatbot. You can talk to me about anything. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("ChatBot:", response)
        if user_input.lower() == 'quit':
            break

if __name__ == "__main__":
    personal_chat()
