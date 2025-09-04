#from langchain.llms import OpenAI
#from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os
import streamlit as st
load_dotenv()


#key=os.getenv('OPENAI_API_KEY')

#FUNCTION TO LOAD OPEN API MODEL AND GET RESPONSE
def get_openai_response(prompt):
    llm = ChatOpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'),model_name="gpt-4o",temperature=0.6)
    messages = [HumanMessage(content=prompt)]
    response = llm.invoke(messages)
    return response.content
    #response = llm(prompt)
    #return response

#initializing streamlit app
st.set_page_config(page_title="Q&A CHATBOT")
st.header("Langchain Application")
input=st.text_input("Enter your weird question")
#response=get_openai_response(input)
submit=st.button("Ask the weird Question")

#if asked button is clicked

if submit and input:
   response=get_openai_response(input)
   st.subheader("The Response is")
   st.write(response)
