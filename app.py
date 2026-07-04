import streamlit as st
from chatbot import get_ai_response

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI Chatbot")

with st.sidebar:
    st.header("⚙️ Settings")
    model = st.selectbox(
        "Choose Model",
        [
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
            "gemma2-9b-it"
        ]
    )
    temperature = st.slider(
        "Temperature",
        0.0,
        1.0,
        0.7
    )
    max_tokens = st.slider(
        "Max Tokens",
        100,
        2048,
        1024
    )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = [
            {
                "role":"system",
                "content":"You are a friendly AI assistant."
            }
        ]
        st.rerun()
    st.divider()
    st.markdown("### About")
    st.write(
        "AI Chatbot powered by Groq + Llama."
    )

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
            answer = get_ai_response(st.session_state.messages,model, temperature, max_tokens)
            st.write(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )