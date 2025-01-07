from speak import speak
import webbrowser as web
from pytube import Search

def search_music(name):
    speak(f"Playing {name}")
    try:
        search = Search(name)
        first_result = search.results[0]
        videoUrl = first_result.watch_url
        web.open(videoUrl)
    except Exception as e:
        speak(f"Could not play the video")
        print("error", e)