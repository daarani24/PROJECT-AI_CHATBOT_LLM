import streamlit as st
from chatbot import get_ai_response

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are a friendly AI assistant."
        }
    ]

for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(message["content"])

question = st.chat_input("Type your message...")

if question:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )
    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = get_ai_response(st.session_state.messages)
            st.write(answer)
            
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )