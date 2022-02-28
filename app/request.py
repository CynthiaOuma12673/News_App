from app import app
import urllib.request,json
from .models import new

New = new.New

#Getting api key
api_key = app.config[NEWS_API_KEY]

#getting api url
base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
    '''
    a function that gets the json response to our urls request
    '''

    get news_url = base_url.format(category, api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data =url.read()
        get_news_response = json.loads(get_news_data)

        new_results = None 

        if get_news_response['results']:
            new_results_list = get_news_response['results']
            new_results = process_results(new_results_list)

    return new_results