import dash_daq as daq
from components import (
    network_line,
    train_stations_density_map,
    train_stations_scatter_map,
)
from dash import Dash, Input, Output, callback, dcc, html

viz = Dash(__name__)

viz.layout = html.Div(
    [
        # daq.ToggleSwitch(
        #     id="switch_map",
        #     label=["Locations", "Density"],
        #     value=False,
        # ),
        # dcc.Graph(id="train_stations", figure=train_stations_density_map),
        dcc.Graph(figure=network_line, style={"width": "50%"}),
    ]
)

#############
# Callbacks #
#############


# @callback(
#     Output("train_stations", "figure"),
#     [Input("switch_map", "value"), Input("train_stations", "relayoutData")],
# )
# def switch_map(is_density_selected, relayout_data):
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
