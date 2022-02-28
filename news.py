from flask import Flask, render_template
from newsapi import NewsApiClient 
from flask_bootstrap import Bootstrap 

app = Flask(__name__)

@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key='4c3735dffe684922bb8b27745a5a30d1')
    top_headlines = newsapi.get_top_headlines(sources = "al-jazeera-english")


    articles = top_headlines['articles']

    description = []
    # news = []
    image = []
    time = []

    for i in range(len(articles)):
        all_articles = articles[i]  

        # news.append(all_articles['title'])
        description.append(all_articles['description'])
        image.append(all_articles['urlToImage'])
        time.append(all_articles['publishedAt'])


    articles_list = zip(description, image, time)

    return render_template('index.html', context = articles_list)


if __name__ == "__main__":
    app.run(debug = True)