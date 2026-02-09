import gradio as gr
import requests

#  Put your OpenRouter API key here
OPENROUTER_API_KEY = "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"

# OpenRouter API URL
API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Function to call OpenRouter
def chat_with_model(user_input):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:7860",
        "X-Title": "Gradio OpenRouter App"
    }

    payload = {
        "model": "meta-llama/llama-3.2-3b-instruct:free",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "Error: " + response.text


# Gradio UI
ui = gr.Interface(
    fn=chat_with_model,
    inputs=gr.Textbox(lines=3, placeholder="Ask something..."),
    outputs="text",
    title="OpenRouter Chatbot",
    description="Using LLaMA 3.2 via OpenRouter"
)

ui.launch()
