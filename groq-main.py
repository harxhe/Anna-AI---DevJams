GROQ_API_KEY = "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"

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0.0,
    max_retries=2,
    api_key= "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"
)

messages = [
    ("system", "You are a helpful bot named anna. Your task is to help your college juniors with their doubts.  "),
    ("human", "Hello anna, what can you do  "),
]
print(llm.invoke(messages).content)

