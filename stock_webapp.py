import yfinance as yf
import streamlit as st
import pandas as pd
import datetime as dt

ticker = 'GOOGL'
ticker_data = yf.Ticker(ticker)
com_name = ticker_data.info['longName']
today = dt.datetime.today()

st.write(f"""

# Simple Stock Price App:
{ticker} stock closing price and volume.  

""")

data = ticker_data.history(start='2010-1-1', end=today)


st.line_chart(data.Close)
st.line_chart(data.Volume)