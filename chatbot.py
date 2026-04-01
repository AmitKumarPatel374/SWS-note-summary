# -------------------- IMPORTS --------------------
import os
from dotenv import load_dotenv
import google.generativeai as genai

# -------------------- LOAD ENV --------------------
load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    print("❌ API Key not found")
else:
    print("✅ API Key loaded successfully")

# -------------------- CONFIGURE GEMINI --------------------
genai.configure(api_key=API_KEY)

# -------------------- FUNCTION --------------------
def summarize_notes(notes):
    try:
        # Initialize model
        model = genai.GenerativeModel("gemini-1.5-flash-latest")

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

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"