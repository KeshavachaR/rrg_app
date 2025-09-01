# Relative Rotation Graph (RRG) Tool

A Streamlit-based interactive tool for generating Relative Rotation Graphs (RRG), which help visualize the relative strength and momentum of multiple stocks or assets compared to a benchmark.

## Features

- Input a list of tickers and a benchmark ticker (default: SPY).
- Select the historical period and data interval.
- Configure the tail length for the animated RRG visualization.
- Download price data dynamically.
- Calculate relative strength ratio and momentum.
- Display an animated, interactive RRG chart.

## Installation

1. Clone the repository:

git clone https://github.com/KeshavachaR/rrg_app.git

cd rrg_app

## Set up a virtual environment:

Windows:

python -m venv .venv

.venv\Scripts\activate

macOS/Linux

python3 -m venv .venv

source .venv/bin/activate

## Install required packages:

pip install -r requirements.txt

## Usage

Run the Streamlit app:

streamlit run app.py

## How to use the app interface:

Tickers: Enter one or more stock tickers separated by commas.

Benchmark: Enter the benchmark ticker symbol (default is SPY).

Period: Choose the historical data period (e.g., 1 year, 6 months).

Interval: Select the data interval (e.g., daily, weekly).

Tail Length: Adjust how many past data points are visible in the animation.

Click Generate RRG to fetch data and display the animated Relative Rotation Graph.

## Dependencies

Streamlit
Plotly
pandas, numpy (assumed for data handling and math)
yfinance or equivalent for ticker data download (assumed inside data.py)

Check requirements.txt for full list.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributions

Contributions are welcome! Feel free to fork the repo and submit pull requests.



