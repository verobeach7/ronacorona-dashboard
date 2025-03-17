# Data Visualization
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from data import countries_df

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
            style={
                "textAlign": "center",
                "paddingTop": "50px",
            },
            children=[
                html.H1("Corona Dashboard", style={"fontSize": 40}),
            ],
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Table(
                            children=[
                                html.Thead(
                                    children=[
                                        html.Tr(
                                            children=[
                                                # Python에서만 가능한 형태. for 반복문을 뒤에서 사용하여 한 줄 쓰기가 가능.
                                                html.Th(column_name.replace("_", " "))
                                                for column_name in countries_df.columns
                                            ]
                                        )
                                    ]
                                ),
                                html.Tbody(
                                    children=[
                                        html.Tr(
                                            children=[
                                                html.Td(value_column)
                                                for value_column in value
                                            ]
                                        )
                                        for value in countries_df.values
                                    ]
                                ),
                            ]
                        )
                    ]
                )
            ]
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
