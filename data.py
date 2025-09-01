# data.py

import yfinance as yf
import pandas as pd

def download_ticker_data(tickers, benchmark, period, interval):
    # Download data for all tickers + benchmark
    all_tickers = tickers + [benchmark]
    data = yf.download(all_tickers, period=period, interval=interval)["Close"]
    data = data.dropna(how='all')
    # Filter available tickers with data
    available = [t for t in tickers if t in data.columns]
    benchmark_ok = benchmark in data.columns
    return data, available, benchmark_ok
