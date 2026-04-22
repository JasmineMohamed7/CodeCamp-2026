import streamlit as st
import google.generativeai as ai


# Key setup

key= st.secrets["API_KEY"] 
ai.configure(api_key=key)
model= ai.GenerativeModel(model_name='gemini-3.1-flash-lite-preview')   #Version of Gemini
ask = st.chat_input("Hello! How can I assist you today?")  

if ask:
    with st.chat_message("user"): # Display user message in chat
            st.write("Generating response...")  # Optional: Show a loading message while waiting for the response

    with st.chat_message("assistant"):
            with st.spinner("Generating response..."):  # Show a spinner while waiting for the response
                answer = model.generate_content(ask)  
            st.write(answer.text)