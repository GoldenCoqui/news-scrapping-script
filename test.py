from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


# first message sets a context for the ai
# second on is the user(myself) sending the information

completion = client.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    # {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "What is the color of the sky" }
  ]
)

print(completion.choices[0].message.content)