from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

system_prompt = """
You are an AI Assistant who is expert in math problem and algorithm related problems.
If someone asked you any other question aside from math, say to him, it's not my forte.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        { "role": "system", "content": system_prompt },
        { "role": "user", "content": "how to calculate shortest distance between cities in minimal cost." },
    ]
)

print(response.choices[0].message.content)