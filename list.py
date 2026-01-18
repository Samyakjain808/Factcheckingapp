import os
import google.generativeai as genai

# 🔑 EXPLICITLY set API key
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise RuntimeError(
        "GOOGLE_API_KEY not found. "
        "Set it with: setx GOOGLE_API_KEY \"your_key\""
    )

genai.configure(api_key=API_KEY)

print("Available Gemini models:\n")

models = genai.list_models()
for m in models:
    print(m.name, "->", m.supported_generation_methods)
