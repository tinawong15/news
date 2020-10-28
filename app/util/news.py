import os, json
import urllib.request
import datetime

API_LINK = 'https://newsapi.org/v2/top-headlines?'

DIR = os.path.dirname(__file__) or '.'
DIR += '/../'
KEYS_LINK = DIR + "data/keys.json"
with open(KEYS_LINK, 'r') as f:
    api_dict = json.load(f)

# API_KEY = ""
API_KEY = api_dict["NEWS_API"]

def search(topic, keywords):
    '''This function gets raw json data of articles related to the topic and other keywords'''
    url = ('https://newsapi.org/v2/everything?'
       'q=' + topic)
    for keyword in keywords:
        url += "+"+keyword
    url += ('&'
       'apiKey=' + API_KEY)
    response = urllib.request.urlopen(url)
    return json.loads(response.read())

def top_headlines_by_topic(topic):
    '''This function gets raw json data of top headlines by topic'''
    url = ('https://newsapi.org/v2/top-headlines?'
       'q=' + topic + '&'
       'apiKey=' + API_KEY)
    response = urllib.request.urlopen(url)
    return json.loads(response.read())

def list_article_titles(raw_json):
    '''This function returns a list of article titles based off of raw json data'''
    result = []
    for article in raw_json['articles']:
        if article['title'] == None:
            result.append('No title')
        else:
            result.append(article['title'])
    return result

def list_article_authors(raw_json):
    '''This function returns a list of article authors based off of raw json data'''
    result = []

    for article in raw_json['articles']:
        if article['author'] == None:
            result.append('No author')
        else:
            result.append(article['author'])

    return result

def list_article_desc(raw_json):
    '''This function returns a list of article descriptions based off of raw json data'''
    result = []

    for article in raw_json['articles']:
        if article['description'] == None:
            result.append('')
        else:
            result.append(article['description'])
    return result

def list_article_urls(raw_json):
    '''This function returns a list of article urls based off of raw json data'''
    result = []

    for article in raw_json['articles']:
        if article['url'] == None:
            result.append('')
        else:
            result.append(article['url'])
    return result

def list_article_imgs(raw_json):
    '''This function returns a list of article img urls based off of raw json data'''
    result = []

    for article in raw_json['articles']:
        if article['urlToImage'] == None:
            result.append('')
        else:
            result.append(article['urlToImage'])
    return result

def list_article_sources(raw_json):
    '''This function returns a list of article sources based off of raw json data'''
    result = []

    for article in raw_json['articles']:
        if article['source']['name'] == None:
            result.append('')
        else:
            result.append(article['source']['name'])
    return result

def list_article_dates(raw_json):
    '''This function returns a list of article dates based off of raw json data'''
    result = []

    for article in raw_json['articles']:
        if article['publishedAt'] == None:
            result.append('')
        else:
            result.append(article['publishedAt'])
    return result

def convert_dates(string_dates_list):
    dates = []
    for string_date in string_dates_list:
        dates.append(datetime.datetime.strptime(string_date[:10], "%Y-%m-%d").strftime("%B %d, %Y"))
    return dates
