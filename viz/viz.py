import dash_bootstrap_components as dbc
from dash import Dash

viz = Dash(
    __name__, title="SNCF Réseau", external_stylesheets=[dbc.themes.BOOTSTRAP]
)
