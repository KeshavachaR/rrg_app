# plotting.py

import plotly.graph_objects as go
from config import BASELINE, SECTOR_COLORS
from rrg_math import get_quadrant
import pandas as pd

def create_animated_rrg(rs_ratio, rs_momentum, tickers, tail_length=10, baseline=BASELINE):
    dates = rs_ratio.index.dropna().tolist()
    if len(dates) > 60:  # Limit animation length for performance
        dates = dates[-60:]
    
    # Prepare frames data
    frames = []
    for date in dates:
        data_traces = []
        for t in tickers:
            if t in rs_ratio.columns and t in rs_momentum.columns:
                x_val = rs_ratio.at[date, t]
                y_val = rs_momentum.at[date, t]
                if pd.isna(x_val) or pd.isna(y_val):
                    continue
                quadrant = get_quadrant(x_val, y_val, baseline)
                color = SECTOR_COLORS.get(quadrant, "gray")
                
                # Tail history for ticker up to current date
                tail_dates = rs_ratio.index[rs_ratio.index.get_loc(date) - tail_length + 1 : rs_ratio.index.get_loc(date) + 1]
                tail_x = rs_ratio.loc[tail_dates, t].dropna()
                tail_y = rs_momentum.loc[tail_dates, t].dropna()
                
                # Line + markers for tail
                trace = go.Scatter(
                    x=tail_x,
                    y=tail_y,
                    mode="lines+markers+text",
                    line=dict(color=color, width=2),
                    marker=dict(size=8, color=color, line=dict(width=1, color="black")),
                    text=[t] * len(tail_x),
                    textposition="top center",
                    name=t,
                    showlegend=False,
                )
                data_traces.append(trace)

        frame = go.Frame(data=data_traces, name=str(date.date()))
        frames.append(frame)
    
    # Base figure with first frame data
    fig = go.Figure(
        data=frames[0].data if frames else [],
        layout=go.Layout(
            title=f"Animated Relative Rotation Graph",
            xaxis=dict(title="RS-Ratio", range=[baseline - 20, baseline + 20]),
            yaxis=dict(title="RS-Momentum", range=[baseline - 20, baseline + 20]),
            updatemenus=[dict(
                type="buttons",
                buttons=[
                    dict(label="Play", method="animate", args=[None, {"frame": {"duration": 500, "redraw": True}, "fromcurrent": True}]),
                    dict(label="Pause", method="animate", args=[[None], {"frame": {"duration": 0}, "mode": "immediate"}]),
                ],
                showactive=False,
                y=1,
                x=1.12,
                xanchor="right",
                yanchor="top"
            )],
            sliders=[dict(
                steps=[dict(method="animate", args=[[f.name], {"mode": "immediate"}], label=f.name) for f in frames],
                transition={"duration": 0},
                x=0,
                y=0,
                currentvalue=dict(font=dict(size=12), prefix="Date: ", visible=True, xanchor="center"),
                len=1.0
            )]
        ),
        frames=frames
    )
    
    # Draw quadrants as rectangles
    fig.add_shape(type="rect", x0=baseline, y0=baseline, x1=baseline + 20, y1=baseline + 20,
                  fillcolor=SECTOR_COLORS["Leading"], opacity=0.1, line_width=0)
    fig.add_shape(type="rect", x0=baseline, y0=baseline - 20, x1=baseline + 20, y1=baseline,
                  fillcolor=SECTOR_COLORS["Weakening"], opacity=0.1, line_width=0)
    fig.add_shape(type="rect", x0=baseline - 20, y0=baseline - 20, x1=baseline, y1=baseline,
                  fillcolor=SECTOR_COLORS["Lagging"], opacity=0.1, line_width=0)
    fig.add_shape(type="rect", x0=baseline - 20, y0=baseline, x1=baseline, y1=baseline + 20,
                  fillcolor=SECTOR_COLORS["Improving"], opacity=0.1, line_width=0)
    
    # Add baseline lines
    fig.add_shape(type="line", x0=baseline, x1=baseline, y0=baseline - 20, y1=baseline + 20,
                  line=dict(color="gray", dash="dash"))
    fig.add_shape(type="line", y0=baseline, y1=baseline, x0=baseline - 20, x1=baseline + 20,
                  line=dict(color="gray", dash="dash"))
    
    return fig
