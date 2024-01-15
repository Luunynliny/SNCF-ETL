from components import train_stop_density_map, train_stop_scatter_map
from dash import Dash, dcc, html

viz = Dash(__name__)

viz.layout = html.Div(
    [
        dcc.Graph(figure=train_stop_scatter_map),
        dcc.Graph(figure=train_stop_density_map),
    ]
)
