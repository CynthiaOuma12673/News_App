from app import app
import urllib.request,json
from .models import new

New = new.New

#Getting api key
api_key = app.config[NEWS_API_KEY]

#getting api url
base_url = app.config['NEWS_API_BASE_URL']