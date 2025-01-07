import requests
import webbrowser as web
from speak import speak
def check_website_availability(name):
    speak(f"Searching for {name}")

    url = f"https://{name}.com"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            speak(f"Opening {name}")
            web.open(url)
        else:
            speak(f"Sorry couldn't open the site.")
    except requests.ConnectionError:
        speak("site not available")
    except requests.Timeout:
        speak("timeout, please try again")
    except requests.RequestException as e:
        speak("sorry, could not open the site")