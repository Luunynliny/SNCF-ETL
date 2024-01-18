import dash_daq as daq
from components import (
    network_domestic,
)  # train_stations_density_map,; train_stations_scatter_map,; network_connection,; network_railroad,
from dash import Input, Output, callback, dcc, html

from viz import viz

viz.layout = html.Div(
    [
        # daq.ToggleSwitch(
        #     id="switch_station_map",
        #     label=["Locations", "Density"],
        #     value=False,
        # ),
        # dcc.Graph(id="train_stations_map", figure=train_stations_density_map),
        # dcc.RadioItems(
        #     id="radio_network_map",
        #     options=[
        #         "Lignes proprement dite",
        #         "Voies de desserte de voies ferrées de port",
        #         "Raccordements",
        #     ],
        #     value="Lignes proprement dite",
        # ),
        dcc.Graph(id="network_map", figure=network_domestic),
    ]
)

#############
# Callbacks #
#############


# @callback(
#     Output("train_stations_map", "figure"),
#     [
#         Input("switch_station_map", "value"),
#         Input("train_stations_map", "relayoutData"),
#     ],
# )
# def switch_station_map(is_density_selected, relayout_data):
#     fig = (
#         train_stations_density_map
#         if is_density_selected
#         else train_stations_scatter_map
#     )

#     if relayout_data:
#         prev_zoom = relayout_data.get("mapbox.zoom", 10)
#         prev_center = relayout_data.get("mapbox.center", {"lat": 0, "lon": 0})

#         fig["layout"]["mapbox"]["zoom"] = prev_zoom
#         fig["layout"]["mapbox"]["center"] = prev_center

#     return fig


# @callback(
#     Output("network_map", "figure"),
#     [
#         Input("radio_network_map", "value"),
#         Input("network_map", "relayoutData"),
#     ],
# )
# def switch_network_map(radio_value, relayout_data):
#     match radio_value:
#         case "Lignes proprement dite":
#             fig = network_domestic
#         case "Voies de desserte de voies ferrées de port":
#             fig = network_railroad
#         case "Raccordements":
#             fig = network_connection

#     if relayout_data:
#         prev_zoom = relayout_data.get("mapbox.zoom", 10)
#         prev_center = relayout_data.get("mapbox.center", {"lat": 0, "lon": 0})

#         fig["layout"]["mapbox"]["zoom"] = prev_zoom
#         fig["layout"]["mapbox"]["center"] = prev_center

#     return fig
