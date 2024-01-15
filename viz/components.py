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

px.set_mapbox_access_token(MAPBOX_TOKEN)

########
# Maps #
########

FRANCE_CENTER = {"lat": 46.71109, "lon": 1.7191036}
ZOOM_LEVEL = 4

train_stop_scatter_map = px.scatter_mapbox(
    stop_points_df,
    lat="lat",
    lon="lon",
    hover_name="label",
    hover_data="id",
    zoom=ZOOM_LEVEL,
    center=FRANCE_CENTER,
)

train_stop_density_map = px.density_mapbox(
    stop_points_df,
    lat="lat",
    lon="lon",
    hover_name="label",
    hover_data="id",
    zoom=ZOOM_LEVEL,
    center=FRANCE_CENTER,
    radius=10,
)

train_stop_density_map.update_coloraxes(showscale=False)
