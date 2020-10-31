import streamlit as st
import yfinance as yf
import pandas as pd 


st.write("""
# Stock Analysis of **Apple Inc**.

The prices of Apple are shown below. Notice the impact of COVID-19 on the market.
""")


# Creating a ticker object for Apple Inc.
obj = yf.Ticker('AAPL')


# Initialise a dataframe that holds historical data of Apple Inc.
# The start and end dates are given below with an interval of 1 day

obj_historical_df = obj.history(start='2020-01-01', end='2020-10-28', interval='1d')
obj_historical_df


# Adding Newline
st.text("")
st.text("")




st.write("""
    ### **Opening Price**
""")
# Plotting opening price on Line Chart of Apple Inc
st.line_chart(obj_historical_df.Open)
st.write("""
    The variation in opening price of Apple Inc during the period 1/1/2020 - 28/10/2020
""")

# Adding Newline
st.text("")
st.text("")




st.write("""
    ### **Closing Price**
""")
# Plotting closing price on Line Chart of Apple Inc
st.line_chart(obj_historical_df.Close)
st.write("""
    The variation in closing price of Apple Inc during the period 1/1/2020 - 28/10/2020
""")

# Adding Newline
st.text("")
st.text("")



st.write("""
    ### **Volume**
""")
# Plotting volume on Line Chart of Apple Inc
st.line_chart(obj_historical_df.Volume)
st.write("""
    The variation in volume of Apple Inc during the period 1/1/2020 - 28/10/2020
    



    [Click here for more information.](https://finance.yahoo.com/quote/AAPL/)
""")

