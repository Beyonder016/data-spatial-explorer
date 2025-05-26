# app/ui_utils1.py

import plotly.graph_objects as go
from app.config import COLOR_MAP

def generate_plot(devices, connections):
    fig = go.Figure()
    status_map = {device.id: "isolated" for device in devices}

    for d1, d2, status in connections:
        for dev in [d1, d2]:
            if status == "interfering":
                status_map[dev] = "interfering"
            elif status == "connected" and status_map[dev] != "interfering":
                status_map[dev] = "connected"
            elif status == "overlapping" and status_map[dev] not in ("connected", "interfering"):
                status_map[dev] = "overlapping"

    for device in devices:
        fill_color = {
            "connected": "rgba(0,255,0,0.15)",
            "overlapping": "rgba(255,255,0,0.15)",
            "interfering": "rgba(255,0,0,0.2)",
            "isolated": "rgba(128,128,128,0.1)"
        }.get(status_map[device.id], "rgba(128,128,128,0.1)")

        fig.add_shape(
            type="circle",
            x0=device.x - device.signal_radius,
            y0=device.y - device.signal_radius,
            x1=device.x + device.signal_radius,
            y1=device.y + device.signal_radius,
            fillcolor=fill_color,
            line=dict(color="lightblue", width=1)
        )

        fig.add_trace(go.Scatter(
            x=[device.x],
            y=[device.y],
            mode='markers+text',
            marker=dict(size=10, color="blue"),
            text=[device.id],
            textposition="top center"
        ))

    for d1, d2, status in connections:
        dev1 = next(d for d in devices if d.id == d1)
        dev2 = next(d for d in devices if d.id == d2)
        fig.add_trace(go.Scatter(
            x=[dev1.x, dev2.x],
            y=[dev1.y, dev2.y],
            mode='lines',
            line=dict(color=COLOR_MAP[status], width=2),
            hoverinfo='skip'
        ))

    fig.update_layout(
        title="📡 Signal Mesh Grid",
        xaxis=dict(range=[0, 100], showgrid=False),
        yaxis=dict(range=[0, 100], showgrid=False),
        height=700,
        showlegend=False
    )
    return fig
