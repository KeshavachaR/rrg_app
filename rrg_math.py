# rrg_math.py

import pandas as pd
from config import BASELINE

def calculate_rs_ratio(data, tickers, benchmark, length=14, baseline=BASELINE):
    rs_ratio = pd.DataFrame(index=data.index)
    for t in tickers:
        try:
            rs = (data[t] / data[t].shift(length)) / (data[benchmark] / data[benchmark].shift(length))
            rs_ratio[t] = rs * baseline
        except:
            continue
    return rs_ratio

def calculate_rs_momentum(rs_ratio, momentum_length=13, baseline=BASELINE):
    momentum = pd.DataFrame(index=rs_ratio.index)
    for t in rs_ratio.columns:
        roc = rs_ratio[t].pct_change(periods=momentum_length)
        momentum[t] = baseline + (roc * baseline)
    return momentum

def get_quadrant(x, y, baseline=BASELINE):
    if x >= baseline and y >= baseline:
        return "Leading"
    elif x >= baseline and y < baseline:
        return "Weakening"
    elif x < baseline and y < baseline:
        return "Lagging"
    else:
        return "Improving"
