import os
from hugchat import hugchat
from hugchat.login import Login
import os
import logging
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env.list
load_dotenv('.env.list')

# Your login credentials
email = "lalithasribhavani@gmail.com"
password = "Siyaram@08"

# Create a Login instance and log in
sign = Login(email, password)
cookies = sign.login()

# Specify a valid directory path to save cookies
cookie_path_dir = "D:\chatbot"

# Make sure the directory exists before attempting to save cookies
if not os.path.exists(cookie_path_dir):
    os.makedirs(cookie_path_dir)

# Save cookies to the specified directory
sign.saveCookiesToDir(cookie_path_dir)

# Instantiate HugChat ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

def get_response(message, history):
    # Continue with the rest of your code...
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    chat_response = chatbot.chat(message)
    chat_response_c = str(chat_response)
    return chat_response_c

def main():
    st.title("Fitness Agent")
    st.markdown("A simple chatbot using a Fitness Agent and Streamlit with conversation history")

    message = st.text_input("You:", "")
    history = st.text_area("Conversation History:", "", height=200)

    if st.button("Send"):
        response = get_response(message, history)
        st.text_area("Fitness Agent:", response)

if __name__ == "__main__":
    main()
