import os

from flask import Flask, render_template, request, session, redirect, url_for, flash

from .util import news

app = Flask(__name__)

app.secret_key = os.urandom(32)

PAYWALLS = ["New York Times","Bloomberg","Vanity Fair","National Post","The Economist","The Guardian","The Wall Street Journal","The Washington Post","Financial Times","Medium"]

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/entertainment', methods=['GET','POST'])
def entertainment():
    articles = {}
    headlines = {}
    raw_json = {}
    titles = []
    urls = []
    descriptions = []
    authors = []
    imgs = []

    # try-except block added in case the API calls fail
    try:
        keywords = []
        # check if user has entered text into the search bar
        if request.method == 'POST':
            keywords = request.form.get('search')
            keywords = keywords.split(" ")
            # print(keywords)
            flash("Search is successful!", "success")
        else:
            # retrieve information about top headlines related to entertainment from News API
            headlines_raw_json = news.top_headlines_by_topic('entertainment')
            headlines_titles = news.list_article_titles(headlines_raw_json)
            headlines_urls = news.list_article_urls(headlines_raw_json)
            headlines_descriptions = news.list_article_desc(headlines_raw_json)
            headlines_imgs = news.list_article_imgs(headlines_raw_json)
            headlines_authors = news.list_article_authors(headlines_raw_json)
            headlines_sources = news.list_article_sources(headlines_raw_json)
            headlines_paywalls = [True if source in PAYWALLS else False for source in headlines_sources]
            # print(paywalls)
            headlines_dates = news.convert_dates(news.list_article_dates(headlines_raw_json))
            for i in range(len(headlines_titles)):
                headlines[headlines_titles[i]] = [headlines_urls[i], headlines_descriptions[i], headlines_authors[i], headlines_imgs[i], headlines_sources[i], headlines_dates[i], headlines_paywalls[i]]
        # retrieve information about all news related to entertainment from News API
        raw_json = news.search('entertainment', keywords)
        # print(raw_json)
        titles = news.list_article_titles(raw_json)
        urls = news.list_article_urls(raw_json)
        descriptions = news.list_article_desc(raw_json)
        authors = news.list_article_authors(raw_json)
        imgs = news.list_article_imgs(raw_json)
        sources = news.list_article_sources(raw_json)
        paywalls = [True if source in PAYWALLS else False for source in sources]
        dates = news.convert_dates(news.list_article_dates(raw_json))
    except:
        flash("Unable to retrieve articles.", "danger")

    for i in range(len(titles)):
        articles[titles[i]] = [urls[i], descriptions[i], authors[i], imgs[i], sources[i], dates[i], paywalls[i]]
    # print(articles)
    return render_template("entertainment.html", articles=articles, headlines=headlines)

@app.route('/sports', methods=['GET','POST'])
def sports():
    articles = {}
    headlines = {}
    raw_json = {}
    titles = []
    urls = []
    descriptions = []
    authors = []
    imgs = []

    # try-except block added in case the API calls fail
    try:
        keywords = []
        # check if user has entered text into the search bar
        if request.method == 'POST':
            keywords = request.form.get('search')
            keywords = keywords.split(" ")
            # print(keywords)
            flash("Search is successful!", "success")
        else:
            # retrieve information about top headlines related to entertainment from News API
            headlines_raw_json = news.top_headlines_by_topic('sports')
            headlines_titles = news.list_article_titles(headlines_raw_json)
            headlines_urls = news.list_article_urls(headlines_raw_json)
            headlines_descriptions = news.list_article_desc(headlines_raw_json)
            headlines_authors = news.list_article_authors(headlines_raw_json)
            headlines_imgs = news.list_article_imgs(headlines_raw_json)
            headlines_sources = news.list_article_sources(headlines_raw_json)
            headlines_paywalls = [True if source in PAYWALLS else False for source in headlines_sources]
            headlines_dates = news.convert_dates(news.list_article_dates(headlines_raw_json))
            for i in range(len(headlines_titles)):
                headlines[headlines_titles[i]] = [headlines_urls[i], headlines_descriptions[i], headlines_authors[i], headlines_imgs[i], headlines_sources[i], headlines_dates[i], headlines_paywalls[i]]
        # retrieve information about all news related to sports from News API
        raw_json = news.search('sports', keywords)
        print(raw_json)
        titles = news.list_article_titles(raw_json)
        urls = news.list_article_urls(raw_json)
        descriptions = news.list_article_desc(raw_json)
        authors = news.list_article_authors(raw_json)
        imgs = news.list_article_imgs(raw_json)
        sources = news.list_article_sources(raw_json)
        paywalls = [True if source in PAYWALLS else False for source in sources]
        dates = news.convert_dates(news.list_article_dates(raw_json))
    except:
        flash("Unable to retrieve articles.", "danger")

    for i in range(len(titles)):
        articles[titles[i]] = [urls[i], descriptions[i], authors[i], imgs[i], sources[i], dates[i], paywalls[i]]
    # print(articles)
    return render_template("sports.html", articles=articles, headlines=headlines)

@app.route('/technology', methods=['GET','POST'])
def technology():
    articles = {}
    headlines = {}
    raw_json = {}
    titles = []
    urls = []
    descriptions = []
    authors = []
    imgs = []

    # try-except block added in case the API calls fail
    try:
        keywords = []
        # check if user has entered text into the search bar
        if request.method == 'POST':
            keywords = request.form.get('search')
            keywords = keywords.split(" ")
            # print(keywords)
            flash("Search is successful!", "success")
        else:
            # retrieve information about top headlines related to entertainment from News API
            headlines_raw_json = news.top_headlines_by_topic('technology')
            headlines_titles = news.list_article_titles(headlines_raw_json)
            headlines_urls = news.list_article_urls(headlines_raw_json)
            headlines_descriptions = news.list_article_desc(headlines_raw_json)
            headlines_authors = news.list_article_authors(headlines_raw_json)
            headlines_imgs = news.list_article_imgs(headlines_raw_json)
            headlines_sources = news.list_article_sources(headlines_raw_json)
            headlines_paywalls = [True if source in PAYWALLS else False for source in headlines_sources]
            headlines_dates = news.convert_dates(news.list_article_dates(headlines_raw_json))
            for i in range(len(headlines_titles)):
                headlines[headlines_titles[i]] = [headlines_urls[i], headlines_descriptions[i], headlines_authors[i], headlines_imgs[i], headlines_sources[i], headlines_dates[i], headlines_paywalls[i]]
        # retrieve information about all news related to technology from News API
        raw_json = news.search('technology', keywords)
        # print(raw_json)
        titles = news.list_article_titles(raw_json)
        urls = news.list_article_urls(raw_json)
        descriptions = news.list_article_desc(raw_json)
        authors = news.list_article_authors(raw_json)
        imgs = news.list_article_imgs(raw_json)
        sources = news.list_article_sources(raw_json)
        paywalls = [True if source in PAYWALLS else False for source in sources]
        dates = news.convert_dates(news.list_article_dates(raw_json))
    except:
        flash("Unable to retrieve articles.", "danger")

    for i in range(len(titles)):
        articles[titles[i]] = [urls[i], descriptions[i], authors[i], imgs[i], sources[i], dates[i], paywalls[i]]
    # print(articles)
    return render_template("technology.html", articles=articles, headlines=headlines)

@app.errorhandler(404)
def page_not_found(e):
    # address return code
    return render_template('404.html'), 404
