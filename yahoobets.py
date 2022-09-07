import yfinance as yf
import praw
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd

# Enter Reddit Username and Password as well as Reddit API Client ID and Secret
reddit_username = "Enter Reddit Username Here"
reddit_password = "Enter Reddit Password Here"
client_id = "Enter Client ID / App ID Here"
client_secret = "Enter Client Secret Here"


class Ticker:
    """
    Valid ticker that can be used for ticker-specific functions
    """
    def __init__(self, ticker):
        self.ticker = ticker
        self.ticker_object = yf.Ticker(ticker)
        # Initializes Python Reddit API Wrapper (PRAW), reddit object, and subreddit object
        self.subreddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            password=reddit_password,
            user_agent="Sentiment Analysis by eddwang @ u/ThirstyPear",
            username=reddit_username,
            ).subreddit("wallstreetbets")

    def generate_chart(self):
        """
        Generates a stock chart and volume chart of user-input ticker that opens on localhost.
        Stock chart contains prices up to a year ago

        Input:
            ticker
                user-given ticker

        Output:
            chart
                stock chart and volume chart via localhost
        """
        data = yf.download(tickers=self.ticker, period='365d', interval='1d', rounding=True)

        # Create stock chart
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1,
                            subplot_titles=('Stock Chart', 'Volume'), row_width=[0.2, 0.7])
        fig.add_trace(
            go.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'],
                           name='Share Price'), row=1, col=1)
        fig.update_layout(title=self.ticker + " Shares", yaxis_title='Share Price (USD)')
        fig.update(layout_xaxis_rangeslider_visible=False)

        # Create volume chart
        fig.add_trace(go.Bar(x=data.index, y=data["Volume"], showlegend=False), row=2, col=1)
        fig.show()

    def find_relevant_posts(self):
        """
        Function that utilizes PRAW (Python Reddit API Wrapper) and yfinance to search for last 5 relevant news / posts

        Input:
            ticker
                user-input ticker
        Output:
            print statements
                5 print statements for relevant YahooFinance news posts with links to each post
                5 print statements for relevant WallStreetBets posts
        """
        print(f"===== YahooFinance News for {self.ticker} =====")
        max_news = 5
        for post in self.ticker_object.news:
            print(f"{post['title']} @ {post['link']}")
            max_news -= 1
            if max_news == 0:
                break

        max_posts = 5
        print(f"\n===== WallStreetBets Posts for {self.ticker} =====")
        for query in ["$" + self.ticker, self.ticker, self.ticker_object.info['longName']]:
            for post in self.subreddit.search(query, sort="top", time_filter="month"):
                print(post.title)
                max_posts -= 1
                if max_posts == 0:
                    break
            if max_posts == 0:
                break
        print()

    def yahoo_analyst_score(self):
        """
        Utilizes yfinance to pull analyst recommendations for each firm. Sets keywords to values from 1-5, with 1 being buy, 3 being hold, and 5 being sell. Then, prints given analyst scores

        Input:
            ticker
                user-input ticker
            ticker_object
                object from yfinance to utilize yfinance API

        Output:
            print statement
                contains analyst recommendation score from 1-5, with 1 being buy and 5 being sell
        """
        # Pulls last 25 analyst recommendations for the stock
        data = pd.DataFrame(self.ticker_object.recommendations, columns=['Firm', 'To Grade']).tail(25)
        firm_list = []
        weight_sum = 0
        weight_counter = 0
        firm_count = 0
        weight_map = dict(Buy=1, Overweight=2, Add=2, Outperform=2, Hold=3, Neutral=3, Underperform=4, Reduce=4,
                          Underweight=4, Sell=5)

        # Iterates over dataframe from most to least recent, skipping over older gradings from the same firm
        for index, row in data[::-1].iterrows():
            if row['Firm'] not in firm_list:
                weight_for_firm = weight_map.get(row['To Grade'])
                if weight_for_firm is not None:
                    firm_count += 1
                    weight_sum += weight_for_firm
                    weight_counter += 1
                    firm_list.append(row['Firm'])
        weight = round(weight_sum / weight_counter, 2)

        print(f"===== YahooFinance and WallStreetBets Scoring for {self.ticker} =====")
        print(f"According {firm_count} analyst firms, {self.ticker} was given a score of {weight}")

    def wsb_sentiment_analysis(self):
        """
        Analyzes sentiment of posts in the last month related to user-given ticker, assigning value from 1.0-5.0, with 1 being buy, 3 being hold, and 5 being sell

        Input:
            ticker
                user-input ticker
            ticker_object
                object from yfinance to utilizes yfinance API

        Output:
            print statement
                contains WallStreetBets sentiment in past month regarding user-given ticker and stock
        """
        # Dictionary word_map with Key as keyword and Value as 1, 3, or 5 as buy/hold/sell score
        word_map = dict.fromkeys(['buy', 'calls', 'call', 'moon', 'bought', 'yolo', 'bullish', 'bull', '🚀', '🐂'], 1)
        word_map.update(dict.fromkeys(['hodl', 'hold', 'diamond hands', '💎🤲'], 3))
        word_map.update(dict.fromkeys(['sell', 'puts', 'put', 'bearish', 'bear', '🧸'], 5))

        stock_sentiment = 0
        total_votes = 0
        # Searches subreddit for keywords of the (ticker), $(ticker), and the full name of the stock
        # i.e. if the ticker were AAPL, then the corresponding keywords are: AAPL, $AAPL, Apple
        for query in ["$" + self.ticker, self.ticker, self.ticker_object.info['longName']]:
            # Checks each post within a month of posting for words in word_map, assigning each post with a post_sentiment_score multiplied by the amount of upvotes
            for post in self.subreddit.search(query, sort="top", time_filter="month"):
                post_sentiment_score = 0
                relevant_word_count = 0
                if post.score > 100:
                    # Lists words in title, then checks each word for a corresponding value in word_map
                    title_word_list = [text for text in post.title.lower().split() if text != " "]
                    for word in title_word_list:
                        if word in word_map:
                            post_sentiment_score += word_map.get(word)
                            relevant_word_count += 1
                if post_sentiment_score != 0:
                    stock_sentiment += (post_sentiment_score / relevant_word_count) * post.score
                    total_votes += post.score
        # Checks if there were any posts with keywords in word_map
        if stock_sentiment != 0:
            print(f"According to {total_votes} votes in the last month, WallStreetBets believes that {self.ticker} is a {round(stock_sentiment / total_votes, 2)}")
        else:
            print("Not enough data in r/wallstreetbets")


def ticker_validity(ticker):
    """
    Utilizes yfinance API to check if the user-input ticker is a valid ticker or not

    Input:
        ticker
            user-input ticker from main function
    Output:
        True
            ticker has a valid corresponding stock
        False
            ticker does not have a valid corresponding stock
    """
    ticker_object = yf.Ticker(ticker)
    if ticker_object.info['regularMarketPrice'] is not None:
        return True
    else:
        print(f"Ticker {ticker} is invalid")
        return False


def main():
    """
    Driver function that checks if the user-input ticker is valid, creates instance of object Ticker, then calls functions
    """
    while True:
        ticker = str(input("What is the ticker of the stock? ")).upper()
        if ticker_validity(ticker):
            break
    stock = Ticker(ticker)
    stock.generate_chart()
    stock.find_relevant_posts()
    stock.yahoo_analyst_score()
    stock.wsb_sentiment_analysis()


if __name__ == "__main__":
    main()
