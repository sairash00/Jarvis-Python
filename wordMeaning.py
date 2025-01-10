import requests
from speak import speak

def get_meaning(word):
    speak("Searching...")
    try:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            # Extracting the first definition
            meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
            example = data[0]["meanings"][0]["definitions"][0].get("example", "No example available.")

            # Formatted meaning output
            meaning_format = (
                f"The meaning of the word {word} is: {meaning}. "
                f"Here is an example: {example}"
            )
            speak(meaning_format)
        else:
            speak(f"Sorry, I couldn't find the meaning of {word}. Please try again.")

    except Exception as e:
        print("Error:", e)
        speak(f"Could not retrieve the meaning of {word} due to an error.")
