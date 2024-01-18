from data import network_df, train_stations_df
from network_type import NetworkType
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

WIDTH, HEIGHT = 2000, 2000

FRANCE_CENTER = {"lat": 46.71109, "lon": 1.7191036}
ZOOM_LEVEL = 4

##################
# Train stations #
##################

train_stations_scatter_map = px.scatter_mapbox(
    train_stations_df,
    lat="lat",
    lon="lon",
    hover_name="libelle",
    hover_data=["code_uic", "code_ligne"],
    zoom=ZOOM_LEVEL,
    center=FRANCE_CENTER,
    mapbox_style="carto-positron",
    # width=WIDTH,
    # height=HEIGHT,
)

train_stations_density_map = px.density_mapbox(
    train_stations_df,
    lat="lat",
    lon="lon",
    hover_name="libelle",
    hover_data=["code_uic", "code_ligne"],
    zoom=ZOOM_LEVEL,
    center=FRANCE_CENTER,
    radius=10,
    mapbox_style="carto-positron",
    # width=WIDTH,
    # height=HEIGHT,
)

train_stations_density_map.update_coloraxes(showscale=False)
train_stations_density_map.update_layout(
    margin={"l": 0, "b": 0, "r": 0, "t": 0}
)

###########
# Network #
###########

network_A = px.line_mapbox(
    network_df[network_df["type"] == NetworkType.A.value],
    lat="lat",
    lon="lon",
    hover_name="name",
    hover_data=["code"],
    color="code",
    line_group="id",
    zoom=ZOOM_LEVEL,
    center=FRANCE_CENTER,
)

network_B = px.line_mapbox(
    network_df[network_df["type"] == NetworkType.B.value],
    lat="lat",
    lon="lon",
    hover_name="name",
    hover_data=["code"],
    color="code",
    zoom=ZOOM_LEVEL,
    center=FRANCE_CENTER,
)

network_C = px.line_mapbox(
    network_df[network_df["type"] == NetworkType.C.value],
    lat="lat",
    lon="lon",
    hover_name="name",
    hover_data=["code"],
    color="code",
    zoom=ZOOM_LEVEL,
    center=FRANCE_CENTER,
)

network_D = px.line_mapbox(
    network_df[network_df["type"] == NetworkType.D.value],
    lat="lat",
    lon="lon",
    hover_name="name",
    hover_data=["code"],
    color="code",
    zoom=ZOOM_LEVEL,
    center=FRANCE_CENTER,
)

network_A.update_layout(showlegend=False)
network_B.update_layout(showlegend=False)
network_C.update_layout(showlegend=False)
network_D.update_layout(showlegend=False)
