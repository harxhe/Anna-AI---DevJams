GROQ_API_KEY = "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"

from langchain_groq import ChatGroq

with open('data.txt', 'r') as file:
    text = file.read()

llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0.0,
    max_retries=2,
    api_key= "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"
)

user_input=input("Hello, Welcome to ANNA AI. How can I help you today?")
messages = [
    ("system", f"You are a helpful bot named anna. Your task is to help your college juniors with their doubts. Here is some additional context from a file: {text} "),
    ("human",  user_input),
]
print(llm.invoke(messages).content)

