# 📊 Stock Analysis Web Application

An interactive web app built with Streamlit to visualize historical stock data (closing prices and trading volume) of leading tech stocks using the yfinance API. Users can dynamically select a stock, time period, and data interval to explore price trends over time.

## 🔧 Tech Stack

- **Python**
- **Streamlit**
- **yFinance**
- **Plotly Express**

## 🌟 Features

- Sidebar controls to select:
  - Stock ticker
  - Time period (e.g., 1 week, 1 month)
  - Interval (e.g., daily, hourly)
- Dynamic chart titles based on selected stock
- Hoverable tooltips showing:
  - Date
  - Price
  - Volume
- Custom validation logic to:
  - Ensure interval is always shorter than the selected period
  - Restrict maximum interval to 1 month
- Exception handling for robust error messaging
- Hosted on **Streamlit Community Cloud**

## 📸 Screenshots

*(Add screenshots of your app UI here)*

## 🚀 Deployment

The app is deployed on Streamlit and can be accessed here:  
**[Live App Link](https://your-app-link.streamlit.app/)**

## 📁 Setup Locally

```bash
pip install streamlit yfinance plotly
streamlit run app.py

This project demonstrates practical knowledge of interactive data visualization, API-based data retrieval, UI/UX design using Streamlit, and deployment of Python applications to the cloud. It provides a robust foundation for building financial analytics dashboards and showcases effective use of modern Python tools in real-world projects.
