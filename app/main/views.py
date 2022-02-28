from flask import render_template
from . import main

# from models import Article, Source

@main.route('/')
def index():

    '''
    view root page that returns the index page and its data
    '''
    return render_template('index.html')