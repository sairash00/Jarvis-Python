import keyboard
import time

def volumeUp (steps = 1) :
    for i in range(steps):
        keyboard.press_and_release("volume up")
        time.sleep(0.1)

def volumeDown (steps = 1) :
    for i in range(steps):
        keyboard.press_and_release("volume down")
        time.sleep(0.1)

