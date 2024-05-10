import google.generativeai as genai
import os
from pathlib import Path
from dotenv import load_dotenv
# Build paths inside the project like this: BASE_DIR / 'subdir'.
load_dotenv()
from django.conf import settings
genai.configure(api_key=os.getenv("GOOGLE_APIKEY"))

model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def gemini(question):
    response=chat.send_message(question)
    return response
        
    