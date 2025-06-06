import streamlit as st
import requests

# Function to get response from GPT-4 API
def get_gpt4_response(prompt):
    response = requests.get(f"http://localhost:5500/?text={prompt}")
    return response.text

# Streamlit UI
st.title("GPT-4 Chatbot")

user_input = st.text_input("You: ", "")

if st.button("Send"):
    if user_input:
        response = get_gpt4_response(user_input)
        st.text_area("GPT-4:", value=response, height=200)
