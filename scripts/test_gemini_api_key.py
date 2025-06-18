import os
import google.generativeai as genai

def test_gemini_api_key():
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("[ERROR] GOOGLE_API_KEY environment variable not set.")
        return
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("Say hello, Gemini!")
        print("Gemini API key is working. Response:")
        print(response.text)
    except Exception as e:
        print(f"[ERROR] Gemini API key test failed: {e}")

if __name__ == "__main__":
    test_gemini_api_key()
