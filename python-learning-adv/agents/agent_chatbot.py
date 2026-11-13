import os
from dotenv import load_dotenv
from google import genai
 
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing. Check your .env file.")
 
client = genai.Client(api_key=api_key)
MODEL = "gemini-3.5-flash-lite"
chat = client.chats.create(model=MODEL)
 
print("Gemini Chatbot (type exit or quit to stop)")
while True:
    message = input("You: ").strip()
 
    if message.lower() in {"exit", "quit"}:
        print("Chat ended.")
        break
 
    if not message:
        continue
 
    try:
        response = chat.send_message(message)
        print("Gemini:", response.text)
    except Exception as exc:
        print("The request failed. Check connection, key, quota and model.")
        print("Technical detail:", exc)
