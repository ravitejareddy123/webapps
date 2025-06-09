import streamlit as st
from gpt4all import GPT4All

model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf", model_path="./", allow_download=False)

st.title("Streamlit GPT4All")

user_input = st.text_input("Enter your text:")

if st.button("Generate Response"):
    if user_input:
        response = model.generate(user_input)
        st.write(response)
    else:
        st.write("Please enter some text.")
