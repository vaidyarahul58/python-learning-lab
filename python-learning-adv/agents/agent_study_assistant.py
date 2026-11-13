import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
 
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing. Check your .env file.")
 
client = genai.Client(api_key=api_key)
MODEL = "gemini-3.5-flash-lite"
 
topic = input("Enter a topic: ").strip()
level = input("Level (beginner/intermediate): ").strip().lower() or "beginner"
 
if not topic:
    raise ValueError("Please enter a topic.")
 
if level not in {"beginner", "intermediate"}:
    print("Unknown level; using beginner.")
    level = "beginner"
 
prompt = f"""Create a study guide about {topic} for a {level} learner.
Include:
1. A simple explanation
2. Five key points
3. One short Python example if relevant
4. Three quiz questions with answers
"""
 
try:
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="You are a supportive programming instructor.",
            temperature=0.4,
            max_output_tokens=1200,
        ),
    )
    print("\n--- Study Guide ---\n")
    print(response.text)
except Exception as exc:
    print("Request failed. Check key, internet, quota and model access.")
    print("Technical detail:", exc)
