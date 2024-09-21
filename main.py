import tkinter as tk
import os
import google.generativeai as anna
import getpass


if "ANNA_KEY" not in os.environ:
    os.environ["ANNA_KEY"] = getpass.getpass("Enter your Google AI API key: ")

anna.configure(api_key=os.environ['ANNA_KEY'])

def bot_response(user_input):
    model = anna.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    response = chat.send_message(user_input)
    return f"ANNA: {response.text}"



def on_enter(event):
    user_input = entry.get()
    if user_input:
        chat_history.insert(tk.END, f"You: {user_input}\n")
        response = bot_response(user_input)
        chat_history.insert(tk.END, f"{response}\n")
        entry.delete(0, tk.END)
        # Auto-scroll to the end
        chat_history.see(tk.END)

# Creating the main window
window = tk.Tk()
window.title("ANNA AI")

# Creating a text widget to display the chat history
chat_history = tk.Text(window, wrap='word', state='normal', height=20, width=50)
chat_history.pack(pady=10)

# Creating an entry widget for user input
entry = tk.Entry(window, width=50)
entry.pack(pady=10)

# Binding the "Enter" key to the on_enter function
entry.bind('<Return>', on_enter)

# Start the Tkinter event loop
window.mainloop()