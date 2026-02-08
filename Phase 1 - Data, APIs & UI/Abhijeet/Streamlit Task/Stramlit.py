import streamlit as st
import requests
import os

# Page title
st.title("Simple AI Chat (OpenRouter + Gemma)")

# Get API key from environment variable
API_KEY = os.getenv("OPENROUTER_API_KEY")


if not API_KEY:
    st.error("OpenRouter API key not found. Set OPENROUTER_API_KEY.")
    st.stop()

# User input
user_prompt = st.text_area("Enter your message")

# Button to generate response
if st.button("Generate Response"):

    if user_prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "google/gemma-3-12b-it:free",
            "messages": [
                {"role": "user", "content": user_prompt}
            ]
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            result = response.json()
            ai_reply = result["choices"][0]["message"]["content"]
            st.subheader("Response:")
            st.write(ai_reply)
        else:
            st.error("Error from OpenRouter API")
            st.write(response.text)
