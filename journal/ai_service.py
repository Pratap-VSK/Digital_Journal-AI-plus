import os
from google import genai
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent  
load_dotenv(os.path.join(BASE_DIR, '.env'))

client = genai.Client()

def analyze_journal_entry(content):
    """
    User ki entry ka content padh kar Gemini AI se uska Mood Tag generate karwane ka logic.
    """
    if not content:
        return "⚪ Analyzed"
        
    try:
        # Prompt to get a perfect response for our custom badge
        prompt = (
            "Analyze the emotional tone of the following journal entry. "
            "Return ONLY a single emoji and a one-word mood indicator "
            "capitalized (e.g., '😊 Happy', '😢 Sad', '🔥 Motivated', '🧘 Calm', '📝 Neutral'). "
            f"Entry text:\n\n{content}"
        )

        response = client.models.generate_content(
            model='gemini-2.5-flash',  
            contents=prompt,
        )
        
        if response.text:
            return response.text.strip()
        return "⚪ Analyzed"

    except Exception as e:
        print(f"❌ Gemini SDK Error: {e}")
        return "⚪ Analyzed"  