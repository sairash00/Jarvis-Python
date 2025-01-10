import requests
from speak import speak
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("HUGGING_FACE")

API_URL = "https://api-inference.huggingface.co/models/google/gemma-2-2b-it"
headers = {
	"Authorization": f"{API_KEY}",
    "x-use-cache": "true"
    }


def get_answer(payload):
    print(payload["inputs"])
    print("Generating")
    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        print("generation successful")
        output = response.json()
        answer = output[0]["generated_text"]
        speak(answer)
    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry!, couldn't give you the answer.")
	

