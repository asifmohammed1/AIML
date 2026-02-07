import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(page_title="Gemma 3 OpenRouter Chat", page_icon="🤖")
st.title("Gemma 3 12B Chatbot")

# Sidebar for API Key and Configuration
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Enter OpenRouter API Key", type="password")
    st.info("Get your key at [openrouter.ai](https://openrouter.ai/keys)")

# Initialize the OpenAI client for OpenRouter
if api_key:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is on your mind?"):
    if not api_key:
        st.error("Please enter your OpenRouter API key in the sidebar.")
    else:
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        try:
            with st.chat_message("assistant"):
                response_placeholder = st.empty()
                full_response = ""
                
                # Make the API call
                response = client.chat.completions.create(
                    model="google/gemma-3-12b-it:free",
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    # OpenRouter requires these headers for rankings/tracking (optional)
                    extra_headers={
                        "HTTP-Referer": "http://localhost:8501", 
                        "X-Title": "Streamlit Gemma 3 App",
                    },
                    stream=True,
                )

                # Stream the response
                for chunk in response:
                    if chunk.choices[0].delta.content:
                        full_response += chunk.choices[0].delta.content
                        response_placeholder.markdown(full_response + "▌")
                
                response_placeholder.markdown(full_response)
            
            # Add assistant response to history
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"An error occurred: {e}")