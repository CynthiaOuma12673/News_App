from flask import render_template
from .import main

@main.app_errorhandler(404)
def four_zero_four(error):
    '''
    A function that gives the error when a page is missing
    '''

    return render_template('notfound.html'),404

@main.app_errorhandler(500)
def internal_error(error):
    return render_template('notfound.html'),500