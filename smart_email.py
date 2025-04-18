import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("AI_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

def generate_email(bullet_points, tone, max_words):
    prompt = f"""
    Write a {tone} email using the following bullet points:
    {bullet_points}
    The email should be clear, well-structured, and professional and have a maximum of {max_words} words.
    """
    
    response = openai.ChatCompletion.create(
        model="openai/gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    
    return response['choices'][0]['message']['content'].strip()
