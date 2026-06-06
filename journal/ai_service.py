import google.generativeai as genai
from django.conf import settings

# fetchin api key from setting
genai.configure(api_key=settings.GEMINI_API_KEY)

def generate_ai_content(prompt_text):
    try:
        # 'gemini-1.5-flash' model ka use kar rahe hain kyunki ye text processing ke liye sabse fast hai
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        # AI ko prompt bhejna aur response lena
        response = model.generate_content(prompt_text)
        
        # Extra spaces ya newlines hata kar clean text return karna
        return response.text.strip()
        
    except Exception as e:
        # Agar net band ho ya API limit cross ho jaye, toh backend crash na kare
        print(f"GenAI Integration Error: {e}")
        return "⚪ Neutral"