from flask import Flask, render_template, request, jsonify
from langchain_groq import ChatGroq
import getpass

app = Flask(__name__)

# Load initial data from file
with open('data.txt', 'r') as file:
    text = file.read()

#Get the api key
key=getpass.getpass("Enter your Google AI API key: ")

# Initialize the language model
llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0.0,
    max_retries=2,
    api_key=key
)

# Initial conversation setup
messages = [
    ("system", f"You are a helpful bot named anna. Your task is to help your college juniors with their doubts. Here is some additional context from a file: {text} "),
    ("human", "Hello ")
]

# Print the initial interaction with the bot to the console
initial_response = llm.invoke(messages)
print(initial_response.content)
messages.append(("ai", initial_response.content))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get('message')
    if not user_message:
        return jsonify({'response': 'Please enter a message.'}), 400

    try:
        messages.append(("human", user_message))
        response = llm.invoke(messages)
        response_text = response.content if hasattr(response, 'content') else str(response)
        messages.append(("ai", response_text))

        return jsonify({'response': response_text})
    except Exception as e:
        return jsonify({'response': f'An error occurred: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)

