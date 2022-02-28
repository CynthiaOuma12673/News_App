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

def process_results(new_list):
    '''
    a function that proesses the new result and transform them to list of objects
    Returns :
    new_results: a list of news objects
    '''

    new_results = []
    for new_item in new_list:
        description = new_item.get('description')
        publishedAt = new_item.get('publishedAt')
        urlToImage = new_item.get('urlToImage')

        if description:
            new_object = New(description, publishedAt, urlToImage)
            new_results.append(new_object)
    return new_results