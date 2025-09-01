# ui_components.py

import streamlit as st
from config import SECTOR_PRESETS

def input_tickers(default="AAPL, MSFT, NVDA"):
    raw = st.text_input("Enter tickers (comma-separated):", default)
    tickers = [t.strip().upper() for t in raw.split(",") if t.strip()]
    return tickers

def select_sector():
    sectors = list(SECTOR_PRESETS.keys())
    selected = st.selectbox("Select Sector Preset:", sectors)
    tickers = SECTOR_PRESETS[selected] if selected != "Cross Asset" else []
    return selected, tickers

def select_period(default="6mo"):
    return st.selectbox("Select Period:", ["1mo", "3mo", "6mo", "1y", "2y", "5y"], index=3, key="period")

def select_interval(default="1d"):
    return st.selectbox("Select Interval:", ["1d", "1wk", "1mo"], index=0, key="interval")

def tail_length_slider(default=10):
    return st.slider("Tail Length", 2, 20, default)
