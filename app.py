import os

from flask import Flask, render_template, request, session, redirect, url_for, flash

from util import news

app = Flask(__name__)

app.secret_key = os.urandom(32)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/entertainment', methods=['GET','POST'])
def entertainment():
    # try-except block added in case the API calls fail
    articles = {}
    try:
        keywords = request.form.get('search')
        if request.method == 'POST':
            keywords = keywords.split(" ")
            print(keywords)
            raw_json = news.search('entertainment', keywords)
            titles = news.list_article_titles(raw_json)
            urls = news.list_article_urls(raw_json)
            descriptions = news.list_article_desc(raw_json)
            authors = news.list_article_authors(raw_json)
            flash("Search is successful!", "success")
        else:
            raw_json = news.top_headlines_by_topic('entertainment')
            titles = news.list_article_titles(raw_json)
            urls = news.list_article_urls(raw_json)
            descriptions = news.list_article_desc(raw_json)
            authors = news.list_article_authors(raw_json)
    except:
        flash("Unable to retrieve articles.", "danger")
        raw_json = {}
        titles = []
        urls = []
        descriptions = []
        authors = []

    for i in range(len(titles)):
        articles[titles[i]] = [urls[i], descriptions[i], authors[i]]
    # print(articles)
    return render_template("entertainment.html", articles=articles)

@app.route('/sports', methods=['GET','POST'])
def sports():
    # try-except block added in case the API calls fail
    articles = {}
    try:
        keywords = request.form.get('search')
        if request.method == 'POST':
            keywords = keywords.split(" ")
            print(keywords)
            raw_json = news.search('sports', keywords)
            titles = news.list_article_titles(raw_json)
            urls = news.list_article_urls(raw_json)
            descriptions = news.list_article_desc(raw_json)
            authors = news.list_article_authors(raw_json)
            flash("Search is successful!", "success")
        else:
            raw_json = news.top_headlines_by_topic('sports')
            titles = news.list_article_titles(raw_json)
            urls = news.list_article_urls(raw_json)
            descriptions = news.list_article_desc(raw_json)
            authors = news.list_article_authors(raw_json)
    except:
        flash("Unable to retrieve articles.", "danger")
        raw_json = {}
        titles = []
        urls = []
        descriptions = []
        authors = []

    for i in range(len(titles)):
        articles[titles[i]] = [urls[i], descriptions[i], authors[i]]
    # print(articles)
    return render_template("sports.html", articles=articles)

@app.route('/technology', methods=['GET','POST'])
def technology():
    # try-except block added in case the API calls fail
    articles = {}
    try:
        keywords = request.form.get('search')
        if request.method == 'POST':
            keywords = keywords.split(" ")
            print(keywords)
            raw_json = news.search('technology', keywords)
            titles = news.list_article_titles(raw_json)
            urls = news.list_article_urls(raw_json)
            descriptions = news.list_article_desc(raw_json)
            authors = news.list_article_authors(raw_json)
            flash("Search is successful!", "success")
        else:
            raw_json = news.top_headlines_by_topic('technology')
            titles = news.list_article_titles(raw_json)
            urls = news.list_article_urls(raw_json)
            descriptions = news.list_article_desc(raw_json)
            authors = news.list_article_authors(raw_json)
    except:
        flash("Unable to retrieve articles.", "danger")
        raw_json = {}
        titles = []
        urls = []
        descriptions = []
        authors = []

    for i in range(len(titles)):
        articles[titles[i]] = [urls[i], descriptions[i], authors[i]]
    # print(articles)
    return render_template("technology.html", articles=articles)

if __name__ == "__main__":
    app.debug = True
    app.run()
