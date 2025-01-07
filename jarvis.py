import speech_recognition as sr
from webChecker import check_website_availability
from speak import speak

r = sr.Recognizer()

def listen_for_wake_word():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio).lower()
            return text
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

def listen_for_command():
    with sr.Microphone() as source:
        speak("Ya")
        print("Listening for your command...")
        audio = r.listen(source)
        try:
            # Recognize speech using Google Web Speech API
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            speak("Sorry, I could not understand what you said.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

# Main loop
if __name__ == "__main__":
    while True:
        wake_word = listen_for_wake_word()
        if "jarvis" in wake_word:
            command = listen_for_command()
            if "open" in command:
                word = command.split()[1]
                check_website_availability(word)
                