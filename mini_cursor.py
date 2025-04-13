import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

system_prompt = """
You are an AI Assistant which can create, modify and delete file.

Example:
Input: Create a file.
Output: {{ step: "analyse", content: "User is interested in creating a file" }}
Output: {{ step: "think", }}
"""

messages = []
messages.append(system_prompt)

while True:

    query = input("Enter prompt: ")
    messages.append(query)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            { "role": "system", "content": system_prompt },
            { "role": "user", "content": query }
        ]
    )