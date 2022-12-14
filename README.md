# YahooBets
Python project for sentiment analysis for r/WallStreetBets and Yahoo Finance, creating a stock chart with volume, and parsing for relevant news and posts

## Description:
This Python application uses yfinance, Python Reddit API Wrapper (PRAW), Plotly, and Pandas to parse and utilize data from [Yahoo Finance](https://finance.yahoo.com/) as well as [r/WallStreetBets](https://www.reddit.com/r/wallstreetbets/). 

User is prompted for a stock ticker, which is then validated. The valid ticker is then used to parse through r/WallStreetBets relevant posts as well as Yahoo Finance's data to determine sentiment of a stock based on a scale from 1.0-5.0 (as seen below). Keywords are used to indicate attitude towards user-input stock.

<p align="center">
  <img alt="Gif of sentiment analysis" src="https://media4.giphy.com/media/UsfytGNnxWbXo00y7a/giphy.gif">
  </br>
  <img height="250px" alt="Stock Recommendation Chart from Investopedia" src="./images/stock_recommendation_chart.png">
</p>

PRAW and yfinance libraries are used to find and select relevant posts on r/WallStreetBets as well as news from Yahoo Finance. Lastly, yfinance and plotly libraries are used to visualize stock opening, closing, high, low, as well as volume on a candlestick chart (which opens on localhost).

<p align="center">
  <img alt="Gif of news and post pulling from program" src="https://media3.giphy.com/media/SPjv5kiJDoLh8uP1CJ/giphy.gif">
  </br>
  <img height="300px" alt="Image of stock chart from plotly" src="./images/sample_stock_chart.png">
</p>

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

Make sure to update the code at the top of the program to include your credentials.

## Future Ideas:
I hope to implement this Python program into a web app, possibly through Django or Flask.

## Credits:
Here are some resources I used to create this project.
### Documentation:
* https://pypi.org/project/yfinance/
* https://praw.readthedocs.io/en/latest/getting_started/quick_start.html
* https://praw.readthedocs.io/en/stable/code_overview/models/subreddit.html

### Sentiment analysis:
* https://www.investopedia.com/financial-edge/0512/understanding-analyst-ratings.aspx
* https://www.stash.com/learn/stashs-guide-to-reddits-wallstreetbets-can-help-you-understand-the-lingo/#:~:text=Redditors%20use%20the%20rocket%20emoji,their%20investments%20and%20avoid%20selling.

### Stock Chart
* https://plotly.com/python/candlestick-charts/
