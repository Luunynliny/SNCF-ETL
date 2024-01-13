import pandas as pd
from dash import Dash, dcc, html
from plotly import express as px

#########
# PATHS #
#########

MAPBOX_TOKEN_PATH = "./MAPBOX_TOKEN.txt"

#########################
# Retrieve Mapbox token #
#########################

with open(MAPBOX_TOKEN_PATH) as f:
    MAPBOX_TOKEN = f.read()

############################
# Initialize visualization #
############################

viz = Dash(__name__)

####################
# Set Mapbox token #
####################

px.set_mapbox_access_token(MAPBOX_TOKEN)

######################
# Map of train stops #
######################

cities_df = pd.DataFrame(
    [
        {"name": "Paris", "lat": 48.864716, "lon": 2.349014},
        {"name": "Lyon", "lat": 45.763420, "lon": 4.834277},
    ]
)

FRANCE_CENTER = {"lat": 46.71109, "lon": 1.7191036}
ZOOM_LEVEL = 4

fig = px.scatter_mapbox(
    cities_df,
    lat="lat",
    lon="lon",
    hover_name="name",
    zoom=ZOOM_LEVEL,
    center=FRANCE_CENTER,
)

##########
# Layout #
##########

viz.layout = html.Div([dcc.Graph(figure=fig)])
