import yfinance as yf
import streamlit as st
import pandas as pd


st.write(
    """
    # Simple stock price app
    Showing the stock **closing price** and **volume** of selected company
    """
)
user_input_stock_label = st.text_input("Type stock label here", "TSLA")
user_input_start_date = st.date_input('start date')
user_input_end_date = st.date_input('end date')


tickerSymbol = user_input_stock_label
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period ="1d", start=user_input_start_date, end=user_input_end_date)
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
