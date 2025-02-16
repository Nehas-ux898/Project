import yfinance as yf
import pandas as pd
import numpy as np
import sys

def calculate_rsi(data, window=14):
    """Calculate Relative Strength Index (RSI)"""
    delta = data["Close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def moving_average(data, window):
    """Calculate Moving Average"""
    return data["Close"].rolling(window=window).mean()

def fetch_and_process_stock(stock_symbol):
    """Fetch stock data and compute indicators"""
    print(f"Fetching data for {stock_symbol}...")
    stock = yf.download(stock_symbol, period="6mo")  # Fetch last 6 months' data
    stock["50_MA"] = moving_average(stock, 50)
    stock["200_MA"] = moving_average(stock, 200)
    stock["RSI"] = calculate_rsi(stock)
    
    stock.to_csv(f"{stock_symbol}_processed.csv")
    print(f"Data saved for {stock_symbol}")

if __name__ == "__main__":
    stock_symbol = sys.argv[1]  # Get stock symbol from SLURM job argument
    fetch_and_process_stock(stock_symbol)
