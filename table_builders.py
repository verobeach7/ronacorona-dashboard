from dash import Dash, html, dcc


def make_table(df):
    return html.Table(
        children=[
            html.Thead(
                style={"display": "block", "marginBottom": 25},
                children=[
                    html.Tr(
                        style={
                            "display": "grid",
                            "gridTemplateColumns": "repeat(4, 1fr)",
                            "fontWeight": "600",
                            "fontSize": 16,
                        },
                        children=[
                            # Python에서만 가능한 형태. for 반복문을 뒤에서 사용하여 한 줄 쓰기가 가능.
                            html.Th(column_name.replace("_", " "))
                            for column_name in df.columns
                        ],
                    )
                ],
            ),
            html.Tbody(
                style={
                    "maxHeight": "50vh",
                    "display": "block",
                    "overflow": "scroll",
                },
                children=[
                    html.Tr(
                        style={
                            "display": "grid",
                            "gridTemplateColumns": "repeat(4, 1fr)",
                            "border-top": "1px solid white",
                            "padding": "30px 0px",
                            "textAlign": "center",
                        },
                        children=[html.Td(value_column) for value_column in value],
                    )
                    for value in df.values
                ],
            ),
        ]
    )
