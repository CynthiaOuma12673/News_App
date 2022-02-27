from flask import Flask
from newsapi import NewsApiClient  

app = Flask(__name__)

@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key='4c3735dffe684922bb8b27745a5a30d1')
    top_headlines = newsapi.get_top_headlines(sources = "al-jazeera-english")


    articles = top_headlines['articles']

    description = []
    news = []
    image = []

    