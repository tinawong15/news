import os, json, itertools

from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_paginate import Pagination, get_page_args
from collections import OrderedDict

from .util import news

app = Flask(__name__)

app.secret_key = os.urandom(32)

PAYWALLS = ["New York Times","Bloomberg","Vanity Fair","Boston Globe","The Australian",
            "National Post","The Economist","The Guardian","The Globe And Mail","Minneapolis Star-Tribune",
            "The Wall Street Journal","The Washington Post","Los Angeles Times","The Age","Miami Herald",
            "The Times","The Sunday Times","Financial Times","Medium","Sydney Morning Herald",
            "Dallas Morning News","Chicago Tribune","Houston Chronicle","Seattle Times","San Francisco Chronicle"]

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/search', methods=['GET','POST'])
def search():
    keywords = []
    entertainment = {}
    sports = {}
    technology = {}
    # try-except block added in case the API calls fail
    try:
        # check if user has entered text into the search bar
        if request.method == 'POST':
            keywords = request.form.get('search')
            tags = json.loads(request.form.get('tag_list')) # get categories to search in
            # print(tags)
            keywords = keywords.split(" ") # split multiple keywords
            # print(keywords)

            # if entertainment is selected, get all information for the entertainment articles related to the keywords
            if 'entertainment' in tags:
                entertainment_raw_json = news.search('entertainment', keywords)
                entertainment_titles = news.list_article_titles(entertainment_raw_json)
                entertainment_urls = news.list_article_urls(entertainment_raw_json)
                entertainment_descriptions = news.list_article_desc(entertainment_raw_json)
                entertainment_authors = news.list_article_authors(entertainment_raw_json)
                entertainment_imgs = news.list_article_imgs(entertainment_raw_json)
                entertainment_sources = news.list_article_sources(entertainment_raw_json)
                entertainment_paywalls = [True if source in PAYWALLS else False for source in entertainment_sources] # display whether article requires paywall
                entertainment_dates = news.convert_dates(news.list_article_dates(entertainment_raw_json))
                for i in range(len(entertainment_titles)):
                    entertainment[entertainment_titles[i]] = [entertainment_urls[i], entertainment_descriptions[i], entertainment_authors[i], entertainment_imgs[i], entertainment_sources[i], entertainment_dates[i], entertainment_paywalls[i]]
            # if sports is selected, get all information for the sports articles related to the keywords
            if 'sports' in tags:
                sports_raw_json = news.search('sports', keywords)
                sports_titles = news.list_article_titles(sports_raw_json)
                sports_urls = news.list_article_urls(sports_raw_json)
                sports_descriptions = news.list_article_desc(sports_raw_json)
                sports_authors = news.list_article_authors(sports_raw_json)
                sports_imgs = news.list_article_imgs(sports_raw_json)
                sports_sources = news.list_article_sources(sports_raw_json)
                sports_paywalls = [True if source in PAYWALLS else False for source in sports_sources]
                sports_dates = news.convert_dates(news.list_article_dates(sports_raw_json))
                for i in range(len(sports_titles)):
                    sports[sports_titles[i]] = [sports_urls[i], sports_descriptions[i], sports_authors[i], sports_imgs[i], sports_sources[i], sports_dates[i], sports_paywalls[i]]
            # if technology is selected, get all information for the technology articles related to the keywords
            if 'technology' in tags:
                technology_raw_json = news.search('technology', keywords)
                technology_titles = news.list_article_titles(technology_raw_json)
                technology_urls = news.list_article_urls(technology_raw_json)
                technology_descriptions = news.list_article_desc(technology_raw_json)
                technology_authors = news.list_article_authors(technology_raw_json)
                technology_imgs = news.list_article_imgs(technology_raw_json)
                technology_sources = news.list_article_sources(technology_raw_json)
                technology_paywalls = [True if source in PAYWALLS else False for source in technology_sources]
                technology_dates = news.convert_dates(news.list_article_dates(technology_raw_json))
                for i in range(len(technology_titles)):
                    technology[technology_titles[i]] = [technology_urls[i], technology_descriptions[i], technology_authors[i], technology_imgs[i], technology_sources[i], technology_dates[i], technology_paywalls[i]]

            # error validation for no results from News API
            if entertainment == {} and sports == {} and technology == {}:
                flash("No results found. Please select a category/categories or try different keyword(s).", "danger")
            else:
                flash("Search is successful!", "success")
    except:
        # News API call failed
        flash("Unable to retrieve articles.", "danger")
    return render_template("search.html", entertainment=entertainment, sports=sports, technology=technology)

@app.route('/sports', methods=['GET'])
def sports():
    headlines = {}
    pagination_headlines = {}
    page = None
    per_page = None
    pagination = None
    # try-except block added in case the API calls fail
    try:
        headlines_raw_json = news.top_headlines_by_topic('sports')
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

        if headlines == {}:
            flash("No articles found.", "danger")

        # handle pagination
        page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
        total = len(headlines) # get number of articles to display
        # keep track of current index of dictionary to display 10 different articles per page
        pagination_headlines = dict(itertools.islice(headlines.items(), offset, offset+per_page))
        pagination = Pagination(page=page, per_page=per_page, total=total,
                                css_framework='bootstrap4')
    except:
        # News API call failed
        flash("Unable to retrieve articles.", "danger")

    return render_template('sports.html',
                           headlines=pagination_headlines,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )

@app.route('/entertainment', methods=['GET'])
def entertainment():
    headlines = {}
    pagination_headlines = {}
    page = None
    per_page = None
    pagination = None
    # try-except block added in case the API calls fail
    try:
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

        if headlines == {}:
            flash("No articles found.", "danger")

        # handle pagination
        page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
        total = len(headlines) # get number of articles to display
        # keep track of current index of dictionary to display 10 different articles per page
        pagination_headlines = dict(itertools.islice(headlines.items(), offset, offset+per_page))
        pagination = Pagination(page=page, per_page=per_page, total=total,
                                css_framework='bootstrap4')
    except:
        # News API call failed
        flash("Unable to retrieve articles.", "danger")
    return render_template('entertainment.html',
                           headlines=pagination_headlines,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )

@app.route('/technology', methods=['GET'])
def technology():
    headlines = {}
    pagination_headlines = {}
    page = None
    per_page = None
    pagination = None
    # try-except block added in case the API calls fail
    try:
        headlines_raw_json = news.top_headlines_by_topic('technology')
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

        if headlines == {}:
            flash("No articles found.", "danger")

        # handle pagination
        page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')
        total = len(headlines) # get number of articles to display
        # keep track of current index of dictionary to display 10 different articles per page
        pagination_headlines = dict(itertools.islice(headlines.items(), offset, offset+per_page))
        pagination = Pagination(page=page, per_page=per_page, total=total,
                                css_framework='bootstrap4')
    except:
        # News API call failed
        flash("Unable to retrieve articles.", "danger")

    return render_template('technology.html',
                           headlines=pagination_headlines,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )

@app.errorhandler(404)
def page_not_found(e):
    # address return code
    return render_template('404.html'), 404
