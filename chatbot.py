import os
from dotenv import load_dotenv
from google import genai

# Load env
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=API_KEY)

def summarize_notes(notes):
    try:
        prompt = f"""
Summarize these study notes in exactly this format:

SHORT SUMMARY:
(4–5 lines)

KEY POINTS:
- Point 1
- Point 2
- Point 3
- Point 4

EXAM READY BULLETS:
• Bullet 1
• Bullet 2
• Bullet 3
• Bullet 4

Notes to summarize:
{notes}
"""

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"