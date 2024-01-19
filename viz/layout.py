import dash_bootstrap_components as dbc
from components import (
    MAP_BASE_CONFIG,
    network_A,
    network_B,
    network_C,
    network_D,
    train_stations_density_map,
    train_stations_scatter_map,
)
from dash import Input, Output, callback
from dash import callback_context as ctx
from dash import dcc, html, no_update

from viz import viz

viz.layout = html.Div(
    [
        dbc.DropdownMenu(
            id="layers",
            label="Layers",
            children=[
                dbc.DropdownMenuItem("Gares - Localisation", id="ts-scatter"),
                dbc.DropdownMenuItem("Gares - Densité", id="ts-density"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem(
                    "Réseau - Ligne proprement dite", id="nw-domestic"
                ),
                dbc.DropdownMenuItem(
                    "Réseau - Raccordement", id="nw-connection"
                ),
                dbc.DropdownMenuItem(
                    "Réseau - Voie-mère d'embranchement", id="nw-siding"
                ),
                dbc.DropdownMenuItem(
                    "Réseau - Voie de desserte de voies ferrées de port",
                    id="nw-service",
                ),
            ],
            style={
                "position": "absolute",
                "width": "300px",
                "left": "10px",
                "top": "10px",
                "zIndex": 1,
            },
        ),
        dcc.Graph(
            id="map",
            figure=train_stations_scatter_map,
            style={"width": "100vw", "height": "100vh", "zIndex": 0},
        ),
        html.Div(id="output"),
    ]
)

#############
# Callbacks #
#############


@callback(
    Output("map", "figure"),
    Input("map", "relayoutData"),
    Input("ts-scatter", "n_clicks"),
    Input("ts-density", "n_clicks"),
    Input("nw-domestic", "n_clicks"),
    Input("nw-connection", "n_clicks"),
    Input("nw-siding", "n_clicks"),
    Input("nw-service", "n_clicks"),
)
def update_map(relayout, *args):
    match ctx.triggered_id:
        case "ts-scatter":
            fig = train_stations_scatter_map
        case "ts-density":
            fig = train_stations_density_map
        case "nw-domestic":
            fig = network_A
        case "nw-connection":
            fig = network_B
        case "nw-siding":
            fig = network_C
        case "nw-service":
            fig = network_D
        case _:
            return no_update

    fig["layout"]["mapbox"]["center"] = relayout.get(
        "mapbox.center", MAP_BASE_CONFIG["center"]
    )
    fig["layout"]["mapbox"]["zoom"] = relayout.get(
        "mapbox.zoom", MAP_BASE_CONFIG["zoom"]
    )

    return fig
