import os
import time
from google import genai
from google.genai import errors
from dotenv import load_dotenv

# 1. Load the vault
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# 2. Configuration - Now 'model_id' is accessible everywhere
MODEL_ID = "gemini-3-flash-preview"
client = genai.Client(api_key=api_key)

def extract_tasks_pro(user_input):
    prompt = f"Extract tasks, people, and times as JSON from: {user_input}"
    
    try:
        response = client.models.generate_content(
            model=MODEL_ID, 
            contents=prompt
        )
        return response.text
    except errors.ClientError as e:
        if "429" in str(e):
            return f"⚠️ {MODEL_ID} is a Pro model. It currently has a 'Zero Quota' for your project. You must link a billing account in Google Cloud Console to unlock it."
        return f"❌ An error occurred: {e}"

if __name__ == "__main__":
    text = "I need to send a project update to Rahul by Monday morning."
    print(f"--- 🧠 Thinking with {MODEL_ID} ---")
    result = extract_tasks_pro(text)
    print(result)