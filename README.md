# The Daily

## Overview
The Daily is my submission for Capital One's 2020 Software Engineering Summit. It is a web application designed to streamline the process of finding top headlines and relevant news articles. You can search specifically for the categories of Entertainment, Sports, and Technology.

## Libraries Used
- **Flask**: Python web microframework
  - `pip install flask`
- **Jinja2**: HTML templating
  - *Included in* `pip install flask`

## Features

#### News API Usage
When you visit the page for Entertainment, Sports, or Technology, you will see Top Headlines at the top of the page. After all the top headlines are displayed, other news related to the category will be displayed.

There are default values

#### Search Functionality

#### Error Validation
If The Daily is unable to access the News API for any reason (an incorrect API key, for example), a message will flash at the top of the page, stating "Unable to retrieve articles."

If you are accessing a page not found on the website, like https://the-daily-ses.herokuapp.com/randompage, you will be sent to the 404 page. The 404 page will explain that the page you are trying to access is not found, and will redirect you back to the home page.
