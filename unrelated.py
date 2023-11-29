from openai import OpenAI
from dotenv import load_dotenv
import json

# Load environment variables from .env file, won't work for me otherwise
load_dotenv()

# Create the client to gain access to openai api
client = OpenAI()

# Opening JSON file
f = open('examples.json')

# returns JSON object as a dictionary
examples = json.load(f)

for example in examples:
    completion = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a marketing expert. Help me rephrase rephrase/reword the product listing title I provide you to optimize it for selling on numerous different online marketplaces. Make sure not to leave out important things like the variation of the product (color, size, style, etc.) or any key content about the product that the customer should know before purchasing."},
        {"role": "user", "content": example["Listing"]}
    ]
    )
    print(completion.choices[0].message)
    print("Initial Listing:",example["Listing"])