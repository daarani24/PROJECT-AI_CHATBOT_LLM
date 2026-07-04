import streamlit as st

st.set_page_config(
    page_title="AI CHATBOT",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI CHATBOT")
st.write("Welcome! This is Our First Streamlit application.")

question=st.text_input("Ask me anything: ")

if st.button("Send"):
    if question.strip():
        st.success(f"You asked: {question}")
    else:
        st.warning("Please enter a question.")

