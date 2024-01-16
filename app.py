# Q&A Chatbot
from langchain.chat_models import ChatOpenAI 
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from langchain.schema import HumanMessage, SystemMessage
# Function to load OpenAI model and get response
def get_openai_response(question):
    llm = ChatOpenAI(openai_api_key= os.getenv("OPEN_API_KEY"), model_name="gpt-3.5-turbo", temperature=0.5)
    conversation_history = [
        SystemMessage(content="You are an AI assistant"),
        HumanMessage(content="Please provide some info"),
        HumanMessage(content=question)  # Include the user's question in the conversation
    ]

    # Pass the conversation history to the model
    response = llm(conversation_history)
    return response

# initialization of streamlit app
    
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input= st.text_input("Input: ", key= "input")
response = get_openai_response(input)

submit = st.button("Ask the question")
# if submit

if submit :
    st.subheader("The Response is")
    st.write(response)