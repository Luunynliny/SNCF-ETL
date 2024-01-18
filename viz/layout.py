import dash_daq as daq
from components import (
    network_A,
    network_B,
    network_C,
    network_D,
    train_stations_density_map,
    train_stations_scatter_map,
)
from dash import Input, Output, callback, dcc, html
from network_type import NetworkType

from viz import viz

viz.layout = html.Div(
    [
        dcc.Dropdown(
            id="dropdown",
            options=[
                {"label": "Scatter Mapbox", "value": "scatter_map"},
                {"label": "Density Mapbox", "value": "density_map"},
            ],
            clearable=False,
            searchable=False,
            value="scatter_map",
            style={
                "position": "absolute",
                "width": "300px",
                "left": "10px",
                "top": "10px",
                "zIndex": 1,
            },
        ),
        dcc.Graph(
            id="train_stations_map",
            figure=train_stations_scatter_map,
            style={"width": "100vw", "height": "100vh", "zIndex": 0},
        )
        # dcc.RadioItems(
        #     id="radio_network_map",
        #     options=[
        #         {"label": nt.value, "value": nt.name} for nt in NetworkType
        #     ],
        #     value=NetworkType.A.name,
        # ),
        # dcc.Graph(id="network_map", figure=network_A),
    ]
)

#############
# Callbacks #
#############


@callback(
    Output("train_stations_map", "figure"),
    [
        Input("dropdown", "value"),
        Input("train_stations_map", "relayoutData"),
    ],
)
def dropdown(selected, relayout_data):
    match selected:
        case "scatter_map":
            fig = train_stations_scatter_map
        case "density_map":
            fig = train_stations_density_map

    if relayout_data:
        prev_zoom = relayout_data.get("mapbox.zoom", 10)
        prev_center = relayout_data.get("mapbox.center", {"lat": 0, "lon": 0})

        fig["layout"]["mapbox"]["zoom"] = prev_zoom
        fig["layout"]["mapbox"]["center"] = prev_center

    return fig


# @callback(
#     Output("network_map", "figure"),
#     [
#         Input("radio_network_map", "value"),
#         Input("network_map", "relayoutData"),
#     ],
# )
# def switch_network_map(radio_value, relayout_data):
#     match radio_value:
#         case NetworkType.A.name:
#             fig = network_A
#         case NetworkType.B.name:
#             fig = network_B
#         case NetworkType.C.name:
#             fig = network_C
#         case NetworkType.D.name:
#             fig = network_D

#     if relayout_data:
#         prev_zoom = relayout_data.get("mapbox.zoom", 10)
#         prev_center = relayout_data.get("mapbox.center", {"lat": 0, "lon": 0})

#         fig["layout"]["mapbox"]["zoom"] = prev_zoom
#         fig["layout"]["mapbox"]["center"] = prev_center

#     return fig
