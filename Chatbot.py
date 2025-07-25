import streamlit as st
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="<Enter your api>", 
)

st.set_page_config(page_title="Support Node", page_icon="🤖")

st.title("ChatCare")
st.markdown("Type below to chat.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1-0528:free",
        messages=st.session_state.chat_history,
        extra_headers={
            "HTTP-Referer": "https://yourdomain.com",
            "X-Title": "OpenRouterChat",
        },
    )

    reply = completion.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": reply})

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
