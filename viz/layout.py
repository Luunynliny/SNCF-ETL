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
    Input("switch_map", "value"),
)
def switch_map(is_density_selected):
    return (
        train_stop_density_map
        if is_density_selected
        else train_stop_scatter_map
    )
