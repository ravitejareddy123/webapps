import streamlit as st
from gpt4all import GPT4All
import json
import os

# File to store chat history
HISTORY_FILE = "chat_history.json"

# Load chat history from file
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

# Save chat history to file
def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

# Load the GPT4All model
model = GPT4All("mistral-7b-instruct-v0.1.Q4_K_M.gguf", model_path="./", allow_download=False)

st.title("Streamlit GPT4All - DevOps Chatbot")

# Initialize or load chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = load_history()

# User input
user_input = st.text_input("Enter your text:")

# Generate response
if st.button("Generate Response"):
    if user_input:
        # Add user input to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # Build context from chat history
        context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.chat_history])
        prompt = f"{context}\nbot:"

        # Generate response
        response = model.generate(prompt)

        # Add bot response to chat history
        st.session_state.chat_history.append({"role": "bot", "content": response})

        # Save updated history
        save_history(st.session_state.chat_history)

        # Display response
        st.write(response)
    else:
        st.write("Please enter some text.")

# Optional: Display chat history
with st.expander("Chat History"):
    for msg in st.session_state.chat_history:
        st.markdown(f"**{msg['role'].capitalize()}**: {msg['content']}")
