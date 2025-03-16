# Data Visualization
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.2/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

app = Dash(external_stylesheets=stylesheets)

app.layout = html.Div(
    # html.H1("Corona Dashboard"),
    # 위와 같이 사용해도 되지만 알아보기 힘듦.
    # children을 명시해주고 배열 리스트로 넣어주는 것이 좋음.
    style={
        "minHeight": "100vh",
        "backgroundColor": "#111111",
        "color": "white",
        "fontFamily": "Open Sans, sans-serif",
    },
    children=[
        html.Header(
            style={
                "textAlign": "center",
                "paddingTop": "50px",
            },
            children=[
                html.H1("Corona Dashboard", style={"fontSize": 40}),
            ],
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
