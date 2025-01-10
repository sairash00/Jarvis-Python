from speak import speak
import requests

def tell_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()
        setup = joke.get("setup")
        punchline = joke.get("punchline")

        speak(f"{setup}..... {punchline}")
    else:
        speak("uhhhh! sorry i couldn't get any joke")