import streamlit as st
from gpt4all import GPT4All

# Replace with the actual filename of the GPT4All 13B Snoozy model
model = GPT4All("ggml-gpt4all-j-v1.3-groovy.gguf", model_path="./", allow_download=False)

st.title("Streamlit GPT4All")

user_input = st.text_input("Enter your text:")

if st.button("Generate Response"):
    if user_input:
        response = model.generate(user_input)
        st.write(response)
    else:
        st.write("Please enter some text.")
