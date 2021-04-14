import yfinance as yf
import pandas as pd

# get stock context
stock = yf.Ticker("AAPL")

# get stock info as a dictionary
stock_info=stock.info
stock_info

# get value from a key of the stock info dictionary
stock_info['country']

# extracting the share price of the last 5 days
stock_share_price_data = stock.history(period="max")
stock_share_price_data.head()

# plot the open prices
stock_share_price_data.reset_index(inplace=True)
stock_share_price_data.plot(x="Date", y="Open")

# extracting the dividends 
stock.dividends

# plot th dividends
apple.dividends.plot()
