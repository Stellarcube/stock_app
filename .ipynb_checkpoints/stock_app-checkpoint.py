import yfinance as yf
import streamlit as st
import plotly.express as px

duration_dict = {'1 Day': '1d', '5 Days':'5d', '1 Month':'1mo', 
                '3 Months':'3mo', '6 Months':'6mo', '1 Year':'1y', 
                '5 Years':'5y', '10 Years':'10y',
                'Year To Date':'ytd'}

duration = st.sidebar.selectbox(
    """
    Select Time Period:
    """,
    options = list(duration_dict.keys()), # the dict is converted to a list and the 'keys' are extracted as options
    index = 2 # default is 1 month
)

# Writing a 'validation logic' to ensure interval is never greater than or equal to period:

# time_period_interval needs to be shorter than time_period_duration.

time_period_duration = {'1 Day': 0, '5 Days': 1, '1 Week': 2, '1 Month': 3, 
                '3 Months': 4, '6 Months': 5, '1 Year': 6, 
                '5 Years': 7, '10 Years': 8, 
                'Year To Date': 9} 

time_period_interval = {'1 Day': 0, '5 Days': 1, '1 Week': 2, '1 Month': 3} 
# Created two different dictionaries (time_period_duration and time_period_interval) to avoid the problem of invalid interval options and restrict the interval options to what's available in interval_dict.

# the 'values' corresponding to the 'keys' in time_period_interval and  are numbers which can be compared.
valid_interval = [k for k, v in time_period_interval.items() if v < time_period_duration[duration]] # Using list comprehension to enable filtering of 'interval' options

interval_dict = {'1 Day': '1d', '5 Days':'5d', '1 Week':'1wk', '1 Month': '1mo'} 
# The entries in (time_period_duration and time_period_interval) and interval_dict have to be in correlated order because they are connected.

interval = st.sidebar.selectbox(
    """
    Select Time Interval:
    """,
    options = valid_interval, # Instead of inserting a list of keys from interval_dict using list(interval_dict.keys()) for interval options, we create a var-'valid_interval' using list comprehension to filter out and only display the interval options less than duration options.
    index = 0
)

stock_dict = {'Microsoft':'MSFT', 'Apple':'AAPL', 'Nvidia':'NVDA',
'Google':'GOOGL', 'Amazon':'AMZN', 'Meta':'META'}

select_stock = st.sidebar.selectbox(
    """
    Select Stock: 
    """,
    options = list(stock_dict.keys()), #Converts dict to a list #stock_dict.keys() means the 'keys' are the listed options
    index = 0 # Default is Microsoft
)

st.write("""
## Stock Price App

Shown are the stock **closing price** and **volume** of {}!

""".format(select_stock)) # Dynamic ticker symbol based on user selection.

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = stock_dict[select_stock]
# stock_dict is a dict and 'stock_dict[select_stock]' passes the value of the selected key listed as an option.
# The 'key:value' pair has to be organized in such a way that the 'value' has to be the ticker for this to work.
# The 'key' has to be used as a label to indicate to the 'value'.


# the 'values' corresponding to the 'keys' are numbers, which can be compared.
#if time_period[interval] >= time_period[duration]: 
    # st.error("Time Period must be longer than Time Interval.") # Error msg (now defunct because of interval option filtering)

#else:
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
try:
    tickerDf = tickerData.history(period = duration_dict[duration], interval = interval_dict[interval]) #get the historical prices for this ticker
    
    fig_close = px.line(tickerDf, x = tickerDf.index, y = 'Close', title = "Closing prices for {}".format(tickerSymbol))
    # Generating a line chart with tooltip feature using Plotly. px.line() generates a line chart.
    st.plotly_chart(fig_close) # Closing prices
    # This tells Streamlit to render the Plotly figure in the web app.
    
    fig_volume = px.line(tickerDf, x = tickerDf.index, y = 'Volume', title = "Trading volume for {}".format(tickerSymbol))
    st.plotly_chart(fig_volume) # Trading volume 
except Exception as e:
    st.error("Failed to fetch data for {}".format(select_stock))






