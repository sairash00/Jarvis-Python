import speech_recognition as sr
from webChecker import check_website_availability
from speak import speak
from searchMusic import search_music
from playPause import play_pause_audio
from getNews import getNews
from openSystemApps import openSystemApps
from getJokes import tell_joke
from getWeather import get_weather
from wordMeaning import get_meaning

r = sr.Recognizer()

def listen_for_wake_word():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio).lower()
            print("you said", text)
            return text
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

def listen_for_command():
    with sr.Microphone() as source:
        speak("Yes")
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
    speak("Hi, I am jarvis")
    while True:
        wake_word = listen_for_wake_word()
        if "jarvis" in wake_word:
            command = listen_for_command()
            if command.startswith("open"):
                word = command.split()[1]
                print(word)
                check_website_availability(word)

            elif command.startswith("play"):
                word = command.split()
                music_name = " ".join(word[1:])
                search_music(music_name)

            elif command.startswith("audio"):
                speak("okay")
                play_pause_audio()

            elif command.startswith("news"):
                country = command.split()[1]
                speak("Searching...")
                getNews(country)

            elif command.startswith("system"):
                speak("Processing...")
                word = command.split()
                app_name = " ".join(word[1:])
                openSystemApps(app_name)

            elif "tell me a joke" in command:
                speak("Got it!")
                tell_joke()

            elif command.startswith("weather"):
                speak("getting weather info")
                place = command.split()[1]
                get_weather(place)

            elif command.startswith("meaning") and "meaning of" in command:
                word = command.split()[2]
                get_meaning(word)

            elif command.startswith("deactivate"):
                speak("Byee, see you soon!")
                break


                