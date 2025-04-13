# Installed google_genai package.
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv('GOOGLE_AI_STUDIO_API_KEY'))

response = client.models.generate_content(
    model="gemini-2.0-flash-001", contents='Why is the sky blue'
)

print(response.candidates[0].content.parts[0].text)
