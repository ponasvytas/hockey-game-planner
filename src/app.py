from dash import Dash, dcc, html
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

import dash
import components, graphs

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

server = app.server

layout = html.Div(
    [
        components.navbar,
        components.main_component,
        graphs.summary_graph,
    ]
)

app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")
