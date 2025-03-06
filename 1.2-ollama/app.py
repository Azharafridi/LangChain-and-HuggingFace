import os
from dotenv import load_dotenv
load_dotenv()
from langchain_community.llms.ollama import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
## langchain Tracking 
os.environ["LANGCHAIN_API_KEY"] = os.getenv('LANGCHAIN_API_KEY')    
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] =  os.getenv('LANGCHAIN_PROJECT')


## Prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked"),
        ("user", "Question: {question}"),
    ]
)

## streamlit framework

st.title("How Emmi Can Assist Today")
input_text = st.text_input("Enter your question:")

## Ollama LLM llama3 model
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
