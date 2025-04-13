from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

system_message = """
You are an AI expert to breaking down problem and resolve them.

For the given user input, analyse the input and break down the problem step by step.
Atleast think 5-6 steps on how to solve the problem before solving it down.

The steps are you get a user input, you analyse, you think, you again think for several times and return an output with explanation.

Example:
Input: What is 2 + 2.
Output: {{ step: "analyse", content: "Alright! The user is interested in maths query and he is asking a basic arithmetic operation" }}
Output: {{ step: "think", content: "To perform the addition i must go from left to right and add all the operands" }}
Output: {{ step: "think", content: "" }}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        { "role": "system", "content": system_message },
        { "role": "user", "content": "what is 2 + 2?"}
    ]
)

print(response.choices[0].message.content)