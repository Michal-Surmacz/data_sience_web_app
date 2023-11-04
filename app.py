import yfinance as yf
import streamlit as st
from datetime import date

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Bitcoin (BTC)!

""")

tickerSymbol = 'BTC-USD'

end_date = date.today()

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end=end_date)

st.write("""
Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
Volume Price
""")
st.line_chart(tickerDf.Volume)
