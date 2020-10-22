import os

from flask import Flask, render_template, request, session, redirect, url_for, flash

from .util import news

app = Flask(__name__)

app.secret_key = os.urandom(32)

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
        if request.method == 'POST':
            keywords = request.form.get('search')
            keywords = keywords.split(" ")
            print(keywords)
            flash("Search is successful!", "success")
        else:
            headlines_raw_json = news.top_headlines_by_topic('entertainment')
            headlines_titles = news.list_article_titles(headlines_raw_json)
            headlines_urls = news.list_article_urls(headlines_raw_json)
            headlines_descriptions = news.list_article_desc(headlines_raw_json)
            headlines_imgs = news.list_article_imgs(headlines_raw_json)
            headlines_authors = news.list_article_authors(headlines_raw_json)
            for i in range(len(headlines_titles)):
                headlines[headlines_titles[i]] = [headlines_urls[i], headlines_descriptions[i], headlines_authors[i], headlines_imgs[i]]
        raw_json = news.search('entertainment', keywords)
        print(raw_json)
        titles = news.list_article_titles(raw_json)
        urls = news.list_article_urls(raw_json)
        descriptions = news.list_article_desc(raw_json)
        authors = news.list_article_authors(raw_json)
        imgs = news.list_article_imgs(raw_json)
    except:
        flash("Unable to retrieve articles.", "danger")

    for i in range(len(titles)):
        articles[titles[i]] = [urls[i], descriptions[i], authors[i], imgs[i]]
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
        if request.method == 'POST':
            keywords = request.form.get('search')
            keywords = keywords.split(" ")
            print(keywords)
            flash("Search is successful!", "success")
        else:
            headlines_raw_json = news.top_headlines_by_topic('sports')
            headlines_titles = news.list_article_titles(headlines_raw_json)
            headlines_urls = news.list_article_urls(headlines_raw_json)
            headlines_descriptions = news.list_article_desc(headlines_raw_json)
            headlines_imgs = news.list_article_imgs(headlines_raw_json)
            headlines_authors = news.list_article_authors(headlines_raw_json)
            for i in range(len(headlines_titles)):
                headlines[headlines_titles[i]] = [headlines_urls[i], headlines_descriptions[i], headlines_authors[i], headlines_imgs[i]]
        raw_json = news.search('sports', keywords)
        print(raw_json)
        titles = news.list_article_titles(raw_json)
        urls = news.list_article_urls(raw_json)
        descriptions = news.list_article_desc(raw_json)
        authors = news.list_article_authors(raw_json)
        imgs = news.list_article_imgs(raw_json)
    except:
        flash("Unable to retrieve articles.", "danger")

    for i in range(len(titles)):
        articles[titles[i]] = [urls[i], descriptions[i], authors[i], imgs[i]]
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
        print(keywords)
        if request.method == 'POST':
            keywords = request.form.get('search')
            keywords = keywords.split(" ")
            print(keywords)
            flash("Search is successful!", "success")
        else:
            headlines_raw_json = news.top_headlines_by_topic('technology')
            headlines_titles = news.list_article_titles(headlines_raw_json)
            headlines_urls = news.list_article_urls(headlines_raw_json)
            headlines_descriptions = news.list_article_desc(headlines_raw_json)
            headlines_imgs = news.list_article_imgs(headlines_raw_json)
            headlines_authors = news.list_article_authors(headlines_raw_json)
            for i in range(len(headlines_titles)):
                headlines[headlines_titles[i]] = [headlines_urls[i], headlines_descriptions[i], headlines_authors[i], headlines_imgs[i]]
        raw_json = news.search('technology', keywords)
        print(raw_json)
        titles = news.list_article_titles(raw_json)
        urls = news.list_article_urls(raw_json)
        descriptions = news.list_article_desc(raw_json)
        authors = news.list_article_authors(raw_json)
        imgs = news.list_article_imgs(raw_json)
    except:
        flash("Unable to retrieve articles.", "danger")

    for i in range(len(titles)):
        articles[titles[i]] = [urls[i], descriptions[i], authors[i], imgs[i]]
    # print(articles)
    return render_template("technology.html", articles=articles, headlines=headlines)
