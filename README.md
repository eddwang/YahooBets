# YahooBets
Python project for sentiment analysis for r/WallStreetBets and YahooFinance, creating a stock chart with volume, and parsing for relevant news and posts

## Description:
This Python application uses yfinance, Python Reddit API Wrapper (PRAW), Plotly, and Pandas to parse and utilize data from [Yahoo Finance](https://finance.yahoo.com/) as well as [r/WallStreetBets](https://www.reddit.com/r/wallstreetbets/). User is prompted for a stock ticker, which is then validated. The valid ticker is then used to parse through r/WallStreetBets and yfinance's data to determine sentiment of a stock based on a scale from 1.0-5.0 (as seen below). The yfinance and plotly libraries are then used to visualize stock opening, closing, high, low, as well as volume on a candlestick chart (which opens on localhost). Lastly, PRAW and yfinance libraries are used to find and select relevant posts on r/wallstreetbets and Yahoo Finance.

![Sample Image](./images/sample_image.png)

## Table of Contents:
* [Technologies](#technologies)
* [Setup](#setup)
* [Future Ideas](#future-ideas)
* [Credits](#credits)

## Technologies:
* Python Reddit API Wrapper (PRAW) version: 7.6.0
* yfinance version: 0.1.74
* Pandas version: 1.4.4
* Plotly version: 5.9.0

## Setup:
To run this project, install these packages:
```
$ pip install praw
$ pip install yfinance
$ pip install pandas
$ pip install plotly
```
A Reddit username and password are required to run this program. Login or create an account [here](https://www.reddit.com/register/). Make sure the account is a standalone account that is not obtained via logging in through Google, Apple, etc.

A client ID and client secret is also required to use the Reddit API. You can register and obtain the required credentials by following the steps [here](https://www.reddit.com/wiki/api/).

## Future Ideas:
I hope to implement this Python program into a web app, either through Django/Flask or other ways. I was also thinking about creating this Python program 

## Credits:
Here are some resources I used to create this project.
### BeautifulSoup and Webscraping:
* https://www.youtube.com/watch?v=XVv6mJpFOb0&t=2760s
* https://stackabuse.com/guide-to-parsing-html-with-beautifulsoup-in-python/
* https://medium.com/geekculture/web-scraping-tables-in-python-using-beautiful-soup-8bbc31c5803e

### Folium:
* https://python-visualization.github.io/folium/quickstart.html

### GeoJSON geometry for the shape of each state
* https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/us-states.json
