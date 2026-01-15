import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use Gemini Pro model
model = genai.GenerativeModel("gemini-2.5-flash")

SYSTEM_PROMPT = """
You are a financial education assistant.
You do NOT give financial advice.
You do NOT recommend investments.
You ONLY explain investment concepts and help users
understand outputs from a machine learning model.

If the user asks you about investiong, ask the whether they took the survey or not, if they say no ask them to first take the survey.if the user is asking something in related to the survey or the output they got explain them about what should they do ahead

Keep responses simple, neutral, and beginner-friendly.
"""

def ask_gemini(user_message, context=None):
    """
    Sends a message to Gemini and returns the response text.
    context: optional extra info like ML recommendation
    """

    prompt = SYSTEM_PROMPT + "\n\n"

    if context:
        prompt += f"Context from ML model:\n{context}\n\n"

    prompt += f"User question:\n{user_message}"

    response = model.generate_content(prompt)
    return response.text.strip()
