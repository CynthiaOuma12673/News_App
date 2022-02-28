import urllib.request, json
from flask.templating import render_template
from .models import Article,Source


api_key = None
category_url = None
source_url = None
headline_url = None