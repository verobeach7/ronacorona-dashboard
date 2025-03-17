# Data Visualization
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from data import countries_df
from table_builders import make_table

# .columns를 이용하여 DataFrame의 헤더 제목을 가져올 수 있음
# print(countries_df.columns)

# .values를 이용하여 DataFrame의 데이터셀을 가져올 수 있음
print(countries_df.values)

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
            style={"textAlign": "center", "paddingTop": "50px", "marginBottom": 100},
            children=[
                html.H1("Corona Dashboard", style={"fontSize": 40}),
            ],
        ),
        html.Div(children=[html.Div(children=[make_table(countries_df)])]),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
