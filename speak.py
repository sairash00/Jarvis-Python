import pyttsx3 as ttx

engine = ttx.init()
voices = engine.getProperty('voices')
    
engine.setProperty('voice', voices[1].id)  
engine.setProperty('rate', 170) 
engine.setProperty('volume', 5)  

def speak(command):
    engine.say(command)
    engine.runAndWait()
