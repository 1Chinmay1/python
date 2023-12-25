import pandas as pd
import yfinance as yf


def get_all_nse_stocks():
    nse = yf.Ticker("^NSEI")
    return pd.DataFrame(nse.history(period="1d"))

def get_volume_data(stock):
    stock_data = yf.Ticker(stock)
    return pd.DataFrame(stock_data.history(period="2d"))['Volume']

def calculate_volume_change(stock):
    volume_data = get_volume_data(stock)
    return volume_data.iloc[-1] - volume_data.iloc[-2]

def filter_stocks(stocks):
    filtered_stocks = []
    for stock in stocks:
        volume_change = calculate_volume_change(stock)
        if volume_change > 3 * stocks[stock]['Volume']:
            filtered_stocks.append(stock)
    return filtered_stocks

if __name__ == "__main__":
    nse_stocks = get_all_nse_stocks()
    filtered_stocks = filter_stocks(nse_stocks)
    print(filtered_stocks)
