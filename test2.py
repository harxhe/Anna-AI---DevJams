import os
import google.generativeai as anna
import streamlit as st

anna.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = anna.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

print("Welcome to ANNA AI !")
print("What do you need help with today? ")

run=True
while run:
    user_input = input("You: ")
    if user_input.lower() in ['end', 'quit', 'bye']:
        print("Goodbye!")
        run= False
    else:
        response = chat.send_message(user_input)
        print(f"Bot: {response.text}")
