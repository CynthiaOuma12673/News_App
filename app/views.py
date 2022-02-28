from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():

    '''
    view root page that returns the index page and its data
    '''
    pupular_news = get_news('popular')
    title = 'Home - Welcome to the News App'
    return render_template('index.html', title = title, popular = popular_news)