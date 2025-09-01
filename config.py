# config.py

BASELINE = 100

SECTOR_COLORS = {
    "Leading": "green",
    "Weakening": "orange",
    "Lagging": "red",
    "Improving": "blue",
}

SECTOR_PRESETS = {
    "Technology": ["AAPL", "MSFT", "NVDA", "GOOG", "META"],
    "Financials": ["JPM", "BAC", "WFC", "C", "GS"],
    "Healthcare": ["JNJ", "PFE", "MRK", "ABBV", "TMO"],
    "Cross Asset": {
        "Equities": ["SPY", "QQQ"],
        "Bonds": ["TLT", "IEF"],
        "Commodities": ["GLD", "USO"],
        "Real Estate": ["VNQ"],
    }
}
