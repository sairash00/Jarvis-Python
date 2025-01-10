import requests as req
from speak import speak
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
load_dotenv()

yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
key = os.getenv("API_KEY_NEWS")
def getNews(topic):
    print("fetching the news")
    data = req.get(f"https://newsapi.org/v2/everything?q={topic}&from={yesterday}&sortBy=publishedAt&language=en&apiKey={key}")
    speak("Evaluating")
    if data.status_code == 200:
        news = data.json()
        articles = news.get("articles", [])
        if articles:
            speak(f"News about {topic}:")
            for i, article in enumerate(articles[:4], 1): 
                speak(f"...article {i}...{article['title']}")
                speak(f"...from {article['source']['name']}")
                speak(f"... the article says ...{article['description']}")
        else:
            speak(f"No news articles found about {topic}")
    else:
        speak(f"Failed to get news, Sorry!")

    
    