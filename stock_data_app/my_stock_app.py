"""
This is a simple stock price scrapper web app.
It takes in stock name and interval and returns historic stock price, volume as well as today's price.
"""

import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# header of the web page
st.write("# Simple Stock Price Scrapper")

# enter the stock symbol
stock_symbol = st.text_input("Please enter Stock name here:", "AAPL")

# enter the interval in days
interval = st.text_input("Please enter the nuumber of days you want to see historic data of: ", "365")
interval = int(interval)

def stock_scrapper(stock_symbol, interval):
    """
    Takes in stock name and interval in days and returns historic stock price
    stock_symbol: name of the stock
    interval: number of days from today
    """

    # get data for stock 
    stock_data = yf.Ticker(stock_symbol)

    #get the historical prices for stock
    # today's date as end date
    end_date = datetime.now().date()

    # to avoid overflow error, if interval is greater than 50 years, then the value is truncated
    if interval > 365*50:
        interval = 365*50

    # start date (from time interval) from when data will be scrapped
    start_date = end_date - timedelta(interval)
    return stock_data.history(period='1d', start=start_date, end=end_date)

# saving historic data in a dataframe
stock_df = stock_scrapper(stock_symbol, interval)

# show today's stock price (closing)
st.write("Today's price of {stock} stock: {price} USD".format(
    stock=stock_symbol, price=round(stock_df['Close'][0],2)
    ))

# show closing price for given time interval
st.write("Closing price of {stock} for past {days} days from today: {date}".format(
    stock=stock_symbol, days=interval, date=datetime.now().date()
    ))

st.line_chart(stock_df['Close'])

# show volume of stock traded for given time interval
st.write("Volume of {stock} traded during past {days} days from today: {date}".format(
    stock=stock_symbol, days=interval, date=datetime.now().date()
    ))

st.line_chart(stock_df['Volume'])

# show the data source
st.write("Source: yahoo! finance")

# developer name:
st.write("Developed by: Galib Hassan Khan")