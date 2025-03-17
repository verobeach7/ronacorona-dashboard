# Data Visualization
from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
from data import (
    countries_df,
    totals_df,
    dropdown_options,
    make_global_df,
    make_country_df,
)
from table_builders import make_table


stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.2/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

app = Dash(external_stylesheets=stylesheets)

# Plotly
bubble_map = px.scatter_geo(
    countries_df,
    locations="Country_Region",
    locationmode="country names",
    template="plotly_dark",
    projection="natural earth",
    color_continuous_scale=px.colors.sequential.Oryel,
    color="Confirmed",
    title="Confirmed by Country",
    size="Confirmed",
    size_max=30,
    hover_name="Country_Region",
    hover_data={
        # "Confirmed": True,
        "Confirmed": ":,",
        "Recovered": ":,",
        "Deaths": ":,",
        "Country_Region": False,
    },
)
bubble_map.update_layout(margin=dict(l=0, r=0, t=50, b=0))

bars_graph = px.bar(
    totals_df,
    x="condition",
    y="count",
    # color와 update_traces를 둘 다 이용하면 오류 발생
    # color는 시스템이 자동으로 임의로 색을 설정
    # update_traces는 내가 원하는 색으로 설정 가능
    # color=["Confirmed", "Recovered", "Deaths"],
    hover_data={"count": ":,"},
    template="plotly_dark",
    title="Total Global Cases",
    labels={
        "condition": "Condition",
        "count": "Count",
        "color": "Condition",
    },  # 이렇게 labes를 이용해서도 변경 가능
)
# bars_graph.update_layout(xaxis=dict(title="Condition"), yaxis=dict(title="Count"))
bars_graph.update_traces(marker_color=["#e74c3c", "#8e44ad", "#27ae60"])

# Dash!!!
app.layout = html.Div(
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
        html.Div(
            style={
                "display": "grid",
                "gap": 50,
                "gridTemplateColumns": "repeat(4, 1fr)",
            },
            children=[
                html.Div(
                    style={"grid-column": "span 3"},
                    children=[dcc.Graph(figure=bubble_map)],
                ),
                html.Div(children=[make_table(countries_df)]),
            ],
        ),
        html.Div(
            style={
                "display": "grid",
                "gap": 50,
                "gridTemplateColumns": "repeat(4, 1fr)",
            },
            children=[
                html.Div(children=[dcc.Graph(figure=bars_graph)]),
                html.Div(
                    style={"grid-column": "span 3"},
                    children=[
                        dcc.Dropdown(
                            id="country",
                            options=[
                                {"label": country, "value": country}
                                for country in dropdown_options
                            ],
                        ),
                        dcc.Graph(id="country_graph"),
                    ],
                ),
            ],
        ),
    ],
)


# Output(id, 어디에 값을 보낸지), [Input(id, 무엇을 값으로 가져올지)]
@callback(Output("country_graph", "figure"), Input("country", "value"))
def update_hello(value):
    if value:
        df = make_country_df(value)
    else:
        df = make_global_df()

    fig = px.line(
        df,
        x="date",
        y=["confirmed", "deaths", "recovered"],
        template="plotly_dark",
        labels={
            "value": "Cases",
            "variable": "Condition",
            "date": "Date",
        },
        hover_data={
            "value": ":,",
            "variable": False,
            "date": False,
        },
        color_discrete_map={
            "confirmed": "#e74c3c",
            "deaths": "#8e44ad",
            "recovered": "#27ae60",
        },
    )
    fig.update_layout(xaxis=dict(rangeslider=dict(visible=True)))
    # 수작업으로 색을 바꿔줄 수도 있음
    # fig["data"][0]["line"]["color"] = "#e74c3c"
    # fig["data"][1]["line"]["color"] = "#8e44ad"
    # fig["data"][2]["line"]["color"] = "#27ae60"

    return fig


if __name__ == "__main__":
    app.run(debug=True)
