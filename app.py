from groq import Groq
import base64
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llava-v1.5-7b-4096-preview"

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

image_path = "medical.png"
base64_image = encode_image(image_path)

client = Groq(api_key=GROQ_API_KEY)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Can you find any abnormalities in this CT scan image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}",
                    },
                },
            ],
        }
    ],
    model=MODEL_NAME,
)

print(chat_completion.choices[0].message.content)
