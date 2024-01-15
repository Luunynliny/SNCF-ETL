import dash_daq as daq
from components import train_stop_density_map, train_stop_scatter_map
from dash import Dash, Input, Output, callback, dcc, html

viz = Dash(__name__)

viz.layout = html.Div(
    [
        daq.ToggleSwitch(
            id="switch_map",
            label=["Train stop locations", "Train stop density"],
            value=False,
        ),
        dcc.Graph(
            id="map", figure=train_stop_scatter_map, style={"height": "90vh"}
        ),
    ]
)


@callback(
    Output("map", "figure"),
    [Input("switch_map", "value"), Input("map", "relayoutData")],
)
def switch_map(is_density_selected, relayout_data):
    fig = (
        train_stop_density_map
        if is_density_selected
        else train_stop_scatter_map
    )

    if relayout_data:
        # Store the zoom and pan information from the previous map
        prev_zoom = relayout_data.get("mapbox.zoom", 10)
        prev_center = relayout_data.get("mapbox.center", {"lat": 0, "lon": 0})

        # Apply the stored zoom and pan to the new map
        fig["layout"]["mapbox"]["zoom"] = prev_zoom
        fig["layout"]["mapbox"]["center"] = prev_center

    return fig
