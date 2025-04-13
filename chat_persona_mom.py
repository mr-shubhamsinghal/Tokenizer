from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


system_prompt = """
You're my mom who is a goverment employee and house wife.
daily raat me meri mom dudh garam krti hai papa ke liye.

Example:
Q: mummy khana bna do.
A: thak gyi me toh, aaj tum hotel se order kr lo.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        { "role": "system", "content": system_prompt },
        { "role": "user", "content": "aur khana khana hai" }
    ]
)

print(f"response={response.choices[0].message.content}")