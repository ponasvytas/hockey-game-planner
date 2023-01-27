from dash import html, dcc
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

# navbar = dmc.Navbar(
#     children = ["Link", "link2"],
#     p="md",
#     fixed=False,
#     withBorder=True,
#     position="top",
#     height=60
# )

navbar = dbc.Navbar(
    children=["Link", "link2"],
    fixed=False,
)

game_dropdown = dcc.Dropdown(
    options=[
        {"label": "3v3", "value": "3v3"},
        {"label": "4v4", "value": "4v4"},
        {"label": "5v5", "value": "5v5"},
    ],
    id="game-selection-dropdown",
    value="4v4",
)

run_button = dbc.Button("Run")

main_component = html.Div([game_dropdown, run_button], id="main-component")
main_component = dbc.Container([game_dropdown, run_button], id="main-component")
