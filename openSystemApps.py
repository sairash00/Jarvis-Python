import os
from speak import speak
from systemAppCommands import app_commands
def openSystemApps(filename):
    command = app_commands.get(filename)
    print(filename)
    if command:
        speak(f"opening {filename}")
        os.system(command)
    else:
        speak(f"{command} is not recognized as system application, sorry!")