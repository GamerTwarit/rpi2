import pygame
import wit

# Initialize pygame mixer
pygame.mixer.init()

# Function to play a specific mp3 file
def play_mp3(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

# Play the welcome message
play_mp3("welcome_start.mp3")

# Initialize the Wit client with your access token
client = wit.Wit('WUG6YPRUU43NJ47HI2GK3TOXTPZYLRHN')

# Define a function to handle messages
def handle_message(message):
    # Send the message to Wit.ai for processing
    resp = client.message(message)
    
    # Extract the intent and entities from the response
    intent = resp['intents'][0]['name'] if 'intents' in resp and resp['intents'] else None
    entities = resp['entities']
    
    # Based on the intent, generate a response and possibly play a sound
    if intent == 'abilities':
        return "I'm not very useful."
    elif intent == 'hello_hi':
        play_mp3("Hi_hello.mp3")
        return "Hello, how can I help you?"
    elif intent == 'angry':
        play_mp3("angry.mp3")
        return "Oh, it's okay. How can I help you calm down?"
    elif intent == 'greet':
        play_mp3("greet.mp3")
        return "I feel great today, how are you feeling?"
    elif intent == 'happy':
        play_mp3("happy.mp3")
        return "Oh great!"
    elif intent == "insult":
        play_mp3("insult.mp3")
        return "I'm sorry, what did I do wrong?"
    elif intent == "thanks":
        play_mp3("thanks.mp3")
    else:
        play_mp3("issue.mp3")
        return "I'm sorry, I didn't understand that."

# Main loop to continuously get user input and respond
while True:
    user_input = input("You: ")
    response = handle_message(user_input)
    print("Bot:", response)
