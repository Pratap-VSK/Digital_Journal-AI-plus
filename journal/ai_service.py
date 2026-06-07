import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

#Fetch the API key directly from the env 
api_key = os.getenv('GEMINI_API_KEY')

#CONFIGURE the GenAI SDK with the fetched key
genai.configure((api_key=api_key))

def generate_ai_content(prompt_text):
    try:
        # 'gemini-2.5-flash' model ka use kar rahe hain kyunki ye text processing ke liye sabse fast hai
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # send the text to ai and get the mood tag
        response = model.generate_content(prompt_text)
        
        # Return the cleaned text (remov extra spaces / new lines)
        return response.text.strip()
        
    except Exception as e:
        # FailSafe in case of internet issues or API limits
        print(f"GenAI Integration Error: {e}")
        return "⚪ Neutral"