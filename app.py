# app.py

import streamlit as st
from data import download_ticker_data
from rrg_math import calculate_rs_ratio, calculate_rs_momentum
from plotting import create_animated_rrg
from ui_components import input_tickers, select_period, select_interval, tail_length_slider
from config import BASELINE

st.set_page_config(page_title="RRG Tool", layout="wide")

st.title("Relative Rotation Graph (RRG) Tool")

# Input controls
tickers = input_tickers()
benchmark = st.text_input("Benchmark:", value="SPY").upper()
period = select_period()
interval = select_interval()
tail_length = tail_length_slider()

if st.button("Generate RRG"):
    if not tickers:
        st.error("Please enter at least one ticker.")
    elif not benchmark:
        st.error("Please enter a benchmark.")
    else:
        with st.spinner("Downloading data..."):
            data, available, ok = download_ticker_data(tickers, benchmark, period, interval)
        
        if not ok:
            st.error(f"No data for benchmark {benchmark}")
        elif not available:
            st.warning("No valid ticker data found")
        else:
            rs_ratio = calculate_rs_ratio(data, available, benchmark)
            rs_momentum = calculate_rs_momentum(rs_ratio)

            fig = create_animated_rrg(rs_ratio, rs_momentum, available, tail_length=tail_length, baseline=BASELINE)
            st.plotly_chart(fig, use_container_width=True)
