from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

# while True:
#     query = input("User : ")
#     if query.lower() in ["bye" , "quit", "exit" , "stop" , "end"] : 
#         print("GoodBye")
#         break
#     res = llm.invoke(query)
#     print("AI : " , res.content , "\n")

st.title("🤖 AskBuddy - Ai QnA Bot")
st.markdown("My QnA bot with Langchain and Google Gemini. ")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask Anything ?") # continue running

if query:
    st.session_state.messages.append({"role":"user" , "content":query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.session_state.messages.append({"role":"ai" , "content":res.content})
    st.chat_message("ai").markdown(res.content)
