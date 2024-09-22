# ANNA AI

**DESCRIPTION** 

This is a simple Chatbot built using Python and Groq AI. The bot can respond to user commands and provide information or perform specific tasks based on the commands given. This chatbot can handle a variety of commands, making it a useful tool for both casual users and developers.
An AI chatbot based on VIT. Anna AI gives information about different courses and curriculum in VIT.

![alt text](<Screenshot 2024-09-22 091608.png>)

**FEATURE**:  

- **Course Information**: Provides details about various academic programs, including course descriptions, prerequisites, and faculty information.  
- **Event Updates**: Provides important updates about upcoming university events, workshops, and seminars.  
- **Admissions Assistance**: Offers guidance on the application process, deadlines, and required documents for prospective students.  
- **Exam Information**:Provides all the information regarding CATs and FATs conducted during the academic year.  
- **FAQs**: Answers frequently asked questions about campus facilities, student services, and academic policies.


**OPERATION** : 

This is a simple Flask-based chatbot named ANNA AI. This application allows users to have a conversation with a chatbot named "Anna," which assists college juniors with their doubts using a large language model (LLM) powered by Groq. We used langchain to give prompt to the system to respond to the user's queries about VIT. We have given certain data about VIT to the prompt so that the model has some context about VIT and the aspects associated with it 

We are using Groq API to authenticate the connection to the Groq language model and we used Flask to create a simple web application that allows interaction between a user and a chatbot and to manage the web interface and handles communication between the frontend (user) and the backend (the chatbot).

### Tech Stack:
- **Backend**: Flask
- **LLM**: Groq (integrated with LangChain for prompt structuring)
- **Programming Language**: Python


