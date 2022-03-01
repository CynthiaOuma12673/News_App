import urllib.request, json
from flask.templating import render_template
from .models import Article,Source
import datetime,timeago


api_key = None
category_url = None
source_url = None
headline_url = None

def configure_request(app):
    '''
    this is a function that will configure the requests
    '''
    global 
    api_key, 
    source_url, 
    category_url, 
    headline_url

    api_key = app.config['NEWS_API_KEY']
    category_url = app.config['CATEGORY_URL']
    source_url = app.config['SOURCE_URL']
    headline_url = app.config['HEADLINE_URL']

def get_headlines():
    '''
    this is a function that will get the json response for the headlines
    '''
    get_headline_url = headline_url.format(api_key)
    with urllib.request.urlopen(get_headline_url) as url:
        get_headline_data = url.read()
        get_headline_response = json.loads(get_headline_data)
        headline_results = None

        if get_headline_response['articles']:
            headline_results_list = get_headline_response['articles']
            headline_results = process_headline_results(headline_results_list)

    return headline_results

def process_headline_results(headline_list):
    '''
    Function  that processes the headline result and transform them to a list of Objects
    '''
    headline_results = []
    for headline_item in headline_list:
        image = headline_item.get('urlToImage')
        title = headline_item.get ('title')
        author = headline_item.get('author')
        description = headline_item.get('description')
        publishedAt = headline_item.get('publishedAt')
        url = headline_item.get('url')
        
        date_time_readable = datetime.datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%SZ')
        now = datetime.datetime.now() + datetime.timedelta(seconds = 60 * 3.4)
        publishedAt =timeago.format(date_time_readable, now)
        
        if image:
            if description:
                if publishedAt:
                    headline_object = Article(image,title,author,description,publishedAt,url)
                    headline_results.append(headline_object)

    return headline_results

def get_category(category):
    '''
    this is a function that gets the json response to our url for request
    '''
    get_category_url = category_url.format(category, api_key)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_category_response = json.loads(get_category_data)
        category_results = None

        if get_category_response['articles']:
            category_results_list = get_category_response['articles']
            category_results = process_headline_results(category_results_list)

    return category_results

def get_source():
    '''
    this is a function that gets the json response to our source request
    '''
    get_source_url = source_url.format(api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_article_data = url.read()
        get_source_article_response = json.loads(get_source_article_data)
        get_source_article_results = None

        if get_source_article_response['sources']:
            source_results_list = get_source_article_response['sources']
            source_articles_results = process_source_results(source_results_list)

    return source_results_list

def process_source_results(source_list):
    '''
    this is a function  that will process the source result and then change them to a list of Objects
    '''
    source_results= []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        url = source_item.get('url')
        description = source_item.get('description')
        
        if url:
            source_object = Source(id,name,url,description)
            source_results.append(source_object)

    return source_results


def get_source_articles(id):
    '''
    this is a function that gets the json response to our source request
    '''
    get_source_article_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    with urllib.request.urlopen(get_source_article_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        
        source_results = None
        
        if get_source_response['articles']:
            source_results_list =get_source_response['articles']
            source_results = process_source_article_results(source_results_list)
            
    return source_results

def process_source_article_results(headline_list):
    '''
    this is a function that process source result and transform them to an object list
    '''
    headline_results=[]
    for headline_item in headline_list:
        image = headline_item.get('urlToImage')
        title = headline_item.get ('title')
        author = headline_item.get('author')
        description = headline_item.get('description')
        publishedAt = headline_item.get('publishedAt')
        url = headline_item.get('url')

        if image:
            if description:
                if publishedAt:
                    headline_object = Article(image,title,author,description,publishedAt,url)
                    headline_results.append(headline_object)
            
    return headline_results

def search_topic(topic_name):
    '''
    this function will  get the json response to our source request
    '''
    search_topic_url = 'https://newsapi.org/v2/everything?apiKey={}&q={}'.format(api_key,topic_name)
    with urllib.request.urlopen(search_topic_url) as url:
        search_topic_data = url.read()
        search_topic_response = json.loads(search_topic_data)
        search_topic_results = None
        
        
        if search_topic_response['articles']:
            search_topic_list = search_topic_response['articles']
            search_topic_results = process_headline_results((search_topic_list))

            return search_topic_results

        else:
            return render_template('notfound.html')



