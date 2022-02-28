from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():

    '''
    view root page that returns the index page and its data
    '''
    bbc_news = get_news('bbc-news')
    aljazeera_news = get_news('al-jazeera-english')
    abc_news = get_news('abc-news')
    title = 'Home - Welcome to the News App'
    return render_template('index.html', title = title, bbc_news = bbc-news, aljazeera_news = al-jazeera-english, abc_news = abc-news )
