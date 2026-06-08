import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. ROOT DIRECTORY PATH FINDER (Dotenv Fetching Fix)
# Isse Python ko exact pata chalega ki .env file kahan rakhi hai
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dotenv_path = os.path.join(BASE_DIR, '.env')

# Agar path exist karta hai toh explicitly load karein
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    load_dotenv() # System fallback

# 2. FETCH API KEY FROM ENV
api_key = os.getenv('GEMINI_API_KEY')

# 3. CONFIGURE GENERATIVE AI AGENT
if api_key:
    # Extra brackets hata diye hain jo pichli baar crash kar rahe the
    genai.configure(api_key=api_key)
else:
    print("❌ ERROR: .env file se GEMINI_API_KEY nahi mil saki. Path ya variable name check karein.")

# 4. AI CORE FUNCTION
def generate_ai_content(prompt_text):
    """
    Ye function prompt leta hai aur Gemini Pro agent ko activate karke
    response return karta hai.
    """
    if not api_key:
        return "⚪ Neutral (No API Key)"

    try:
        # Gemini 1.5 Flash agent/model ko initialize kar rahe hain
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # Agent real-time request bhej raha hai
        response = model.generate_content(prompt_text)
        
        # Clean response string return karein
        return response.text.strip()
        
    except Exception as e:
        # Failsafe agar internet, quota limit ya token ka issue aaye
        print(f"❌ Gemini AI Agent Handshake Error: {e}")
        return "⚪ Neutral"