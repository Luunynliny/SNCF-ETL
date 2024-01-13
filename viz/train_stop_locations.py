from dash import Dash, dcc, html
from data import stop_points_df
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

FRANCE_CENTER = {"lat": 46.71109, "lon": 1.7191036}
ZOOM_LEVEL = 4

fig = px.scatter_mapbox(
    stop_points_df,
    lat="lat",
    lon="lon",
    hover_name="label",
    hover_data="id",
    zoom=ZOOM_LEVEL,
    center=FRANCE_CENTER,
)

##########
# Layout #
##########

viz.layout = html.Div([dcc.Graph(figure=fig)])
