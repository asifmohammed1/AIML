import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(page_title="Gemma 3 Streamlit Bot", page_icon="🤖")

st.title("💬 Gemma 3-12b Chatbot")
st.caption("Powered by OpenRouter and Google Gemma 3-12b-it")

# Sidebar for API Key and Configuration
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter OpenRouter API Key", type="password")
    st.markdown("[Get an API Key here](https://openrouter.ai/keys)")
    
    # Model Selection (Fixed as per request)
    model_id = "google/gemma-3-12b-it"
    
    if not api_key:
        st.warning("Please enter your API key to start.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("How can I help you today?"):
    if not api_key:
        st.error("Missing API Key! Please add it in the sidebar.")
    else:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Connect to OpenRouter
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )

        # Generate response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            
            try:
                # API Call
                completion = client.chat.completions.create(
                    extra_headers={
                        "HTTP-Referer": "http://localhost:8501", # Optional
                        "X-Title": "Streamlit Gemma App", # Optional
                    },
                    model=model_id,
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True
                )

                for response in completion:
                    chunk = response.choices[0].delta.content or ""
                    full_response += chunk
                    message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
