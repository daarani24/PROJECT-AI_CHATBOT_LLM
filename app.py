import streamlit as st
from chatbot import get_ai_response

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chatbot using Groq")
question = st.text_input("Ask me anything")

if st.button("Send"):
    if question:
        with st.spinner("Thinking..."):
            answer = get_ai_response(question)
        st.success("Response")
        st.write(answer)
    else:
        st.warning("Please enter a question.")