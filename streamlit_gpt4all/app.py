import streamlit as st
from gpt4all import GPT4All
import json
import os

# File to store chat history
HISTORY_FILE = "chat_history.json"
import streamlit as st
from gpt4all import GPT4All
import json
import os

HISTORY_FILE = "chat_history.json"

def load_history():
    if os.path.exists(HISTORY_FILE) and os.path.isfile(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []
def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

@st.cache_resource
def load_model():
    return GPT4All("mistral-7b-instruct-v0.1.Q4_K_M.gguf", model_path="./models", allow_download=False)

model = load_model()

st.title("Streamlit GPT4All - DevOps Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = load_history()

user_input = st.text_input("Enter your text:")

if st.button("Generate Response"):
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        context = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state.chat_history])
        prompt = f"{context}\nBot:"

        with st.spinner("Thinking..."):
            response = model.generate(prompt)

        st.session_state.chat_history.append({"role": "bot", "content": response})
        save_history(st.session_state.chat_history)
        st.write(response)
    else:
        st.write("Please enter some text.")

if st.button("Clear Chat"):
    st.session_state.chat_history = []
    save_history([])
    st.experimental_rerun()

with st.expander("Chat History"):
    for msg in st.session_state.chat_history:
        st.markdown(f"**{msg['role'].capitalize()}**: {msg['content']}")
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
