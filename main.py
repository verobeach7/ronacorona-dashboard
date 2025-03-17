# Data Visualization
from dash import Dash, html, dcc
import plotly.express as px
from data import countries_df, totals_df
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
    hover_data={"count": ":,"},
    template="plotly_dark",
    title="Total Global Cases",
)
bars_graph.update_layout(xaxis=dict(title="Condition"), yaxis=dict(title="Count"))

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
            children=[
                html.Div(children=[dcc.Graph(figure=bubble_map)]),
                html.Div(children=[make_table(countries_df)]),
            ]
        ),
        html.Div(
            children=[
                html.Div(children=[dcc.Graph(figure=bars_graph)]),
            ]
        ),
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
