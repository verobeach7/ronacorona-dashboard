from dash import Dash, html, dcc


def make_table(df):
    return html.Table(
        children=[
            html.Thead(
                children=[
                    html.Tr(
                        children=[
                            # Python에서만 가능한 형태. for 반복문을 뒤에서 사용하여 한 줄 쓰기가 가능.
                            html.Th(column_name.replace("_", " "))
                            for column_name in df.columns
                        ]
                    )
                ]
            ),
            html.Tbody(
                children=[
                    html.Tr(children=[html.Td(value_column) for value_column in value])
                    for value in df.values
                ]
            ),
        ]
    )
