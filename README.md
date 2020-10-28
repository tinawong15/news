# The Daily

## Overview
The Daily is my submission for Capital One's 2020 Software Engineering Summit. It is a web application designed to streamline the process of finding top headlines and relevant news articles. You can search specifically for the categories of Entertainment, Sports, and Technology.

## Tools and Libraries Used
- **Flask**: Python web microframework
  - `pip install flask`
- **Jinja2**: HTML templating
  - *Included in* `pip install flask`
- **Bootstrap**: open-source CSS framework
- **Heroku**: platform as a service (PaaS)

## Features

#### News API Usage
When you visit the page for Entertainment, Sports, or Technology, you will see Top Headlines at the top of the page. After all the top headlines are displayed, other news related to the category will be displayed.

For each article, the following information about the article is displayed on the website:
- title
- link to article, which will open in a new tab
- author (if exists. If not, the byline will only show the source.)
- source
- paywall (if exists for the news source)
- date (converted from a format like this: `2018-04-12T13:00:00Z` to a more readable format of `April 12, 2018`)
- description
- image (if exists. More information in next paragraph)

When the articles are listed, the image appears next to the description of the article. If there is no image associated with the article, the Bootstrap column dedicated to the image is eliminated and the description of the article will fill up the entire horizontal space. If there is an image associated with the article but the website does not have the permission to access the image, the Bootstrap column dedicated to the image will still exist, but it will be blank.

#### Search Functionality
You will be able to search specifically within the categories of Entertainment, Sports, and Technology. You can enter one or multiple keywords into the search bar, and all of the keywords will be taken into account in the search. If you would like to search a phrase rather than multiple different words, such as "New York Times" rather than "New", "York", "Times", enter the phrase in quotes.

If the search is successful, a message will flash at the top of the page, stating "Search is successful!"

### Paywalls
If an article is from a news source that has any form of paywall (prevents you from reading the article, limits the number of articles you can read per month, etc.), there will be a tag `✓ Paywall` next to the date of the article.

#### Error Validation
If The Daily is unable to access the News API for any reason (an incorrect API key, for example), a message will flash at the top of the page, stating "Unable to retrieve articles."

If you are accessing a page not found on the website, like https://the-daily-ses.herokuapp.com/randompage, you will be sent to the 404 page. The 404 page will explain that the page you are trying to access is not found, and will redirect you back to the home page.
