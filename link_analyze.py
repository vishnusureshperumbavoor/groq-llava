from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found. Please set it in your .env file.")

client = Groq(api_key=GROQ_API_KEY)

image_url = "https://patient.info/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fxxv4b9mbhlgd%2Fimg_7326%2Fe78f4f9231fa4d7b1e872b426d515e2e%2F54d65006-315b-4500-b1a3-e9bb79743760.png&w=1600&q=75"

try:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Can you find any abnormalities in this CT scan image?"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                        },
                    },
                ],
            }
        ],
        model="llava-v1.5-7b-4096-preview",
    )

    print(chat_completion.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")
