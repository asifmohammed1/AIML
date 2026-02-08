import gradio as gr
import os
import time
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

# ------------------------------------------------------------------
# CONFIGURATION & SECURITY
# ------------------------------------------------------------------
# 1. Force-find the 'config.env' file
script_dir = Path(__file__).parent
env_path = script_dir / "config.env"  # <--- CHANGED NAME HERE

print(f"🔍 Looking for config file at: {env_path}")

# 2. Load the file explicitly
load_dotenv(dotenv_path=env_path)

# 3. Get the key
API_KEY = os.getenv("OPENROUTER_API_KEY")

# 4. Debug Check
if not API_KEY:
    print("\n❌ ERROR: API Key still not found!")
    print(f"   I checked this specific file: {env_path}")
    print("   1. Rename your key file to 'config.env'")
    print("   2. Open it and ensure it contains: OPENROUTER_API_KEY=sk-or-...")
    # Stop the script if no key
    raise ValueError("API Key not found. Please check the terminal for details.")
else:
    print(f"✅ API Key loaded successfully! (Key starts with: {API_KEY[:10]}...)")

# ------------------------------------------------------------------

def create_client():
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=API_KEY,
        timeout=20.0,
    )

def predict(message, history):
    client = create_client()
    
    # --- HISTORY CONVERTER ---
    messages_payload = []
    for item in history:
        if isinstance(item, (list, tuple)) and len(item) >= 2:
            if item[0]: messages_payload.append({"role": "user", "content": str(item[0])})
            if item[1]: messages_payload.append({"role": "assistant", "content": str(item[1])})
        elif isinstance(item, dict):
            messages_payload.append(item)
    messages_payload.append({"role": "user", "content": message})
    # -------------------------

    # --- STRATEGY 1: AUTO-ROUTER ---
    try:
        # print("🔄 Auto-Router: Finding best free model...")
        response = client.chat.completions.create(
            model="openrouter/free", 
            messages=messages_payload,
            stream=True,
            extra_headers={
                "HTTP-Referer": "http://localhost:7860", 
                "X-Title": "Gradio Auto-App",
            },
        )

        partial_message = ""
        for chunk in response:
            if chunk.choices[0].delta.content:
                partial_message += chunk.choices[0].delta.content
                yield partial_message
        return 

    except Exception as e:
        print(f"⚠️ Auto-Router busy: {e}")

    # --- STRATEGY 2: MANUAL BACKUP LIST ---
    BACKUP_MODELS = [
        "liquid/lfm-40b:free",
        "nvidia/nemotron-3-nano-30b:free",
        "huggingfaceh4/zephyr-7b-beta:free",
        "microsoft/phi-3-mini-128k-instruct:free",
    ]

    for model_id in BACKUP_MODELS:
        try:
            # yield f"🔄 Switching to backup: {model_id.split('/')[1]}..."
            time.sleep(1)
            
            response = client.chat.completions.create(
                model=model_id,
                messages=messages_payload,
                stream=True,
            )

            for chunk in response:
                if chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
            return 

        except Exception as e:
            print(f"❌ Failed {model_id}: {e}")
            continue

    yield "❌ Global Outage: All free models are currently down. Please try again in 10 minutes."

# Define the interface
demo = gr.ChatInterface(
    fn=predict,
    title="OpenRouter Infinite (Free)",
    description="Securely loads API key from config.env. Automatically finds free models.",
    examples=[["Explain quantum computing."]],
    cache_examples=False,
)

if __name__ == "__main__":
    demo.launch(share=True)
