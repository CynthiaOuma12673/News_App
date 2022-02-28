from flask import render_template
from app import app

@app.route('/')
def index():

    '''
    view root page that returns the index page and its data
    '''
    title = 'Home - Welcome to the News App'
    return render_template('index.html', title = title)