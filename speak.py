import pyttsx3 as ttx

engine = ttx.init()

def speak(command):
    engine.say(command)
    engine.runAndWait()