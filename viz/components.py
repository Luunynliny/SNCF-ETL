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

FRANCE_CENTER = {"lat": 46.71109, "lon": 1.7191036}
ZOOM_LEVEL = 5

OPACITY = 0.5

MAP_BASE_CONFIG = {
    "lat": "lat",
    "lon": "lon",
    "hover_name": "libelle",
    "hover_data": ["code_uic", "code_ligne"],
    "zoom": ZOOM_LEVEL,
    "center": FRANCE_CENTER,
    "opacity": OPACITY,
}

LINE_BASE_CONFIG = {
    "lat": "lat",
    "lon": "lon",
    "hover_name": "name",
    "hover_data": ["code"],
    "color": "code",
    "line_group": "id",
    "zoom": ZOOM_LEVEL,
    "center": FRANCE_CENTER,
}

LAYOUT_BASE_CONFIG = {"margin": {"l": 0, "b": 0, "r": 0, "t": 0}}

##################
# Train stations #
##################

train_stations_scatter_map = px.scatter_mapbox(
    train_stations_df, **MAP_BASE_CONFIG
)

train_stations_density_map = px.density_mapbox(
    train_stations_df,
    **MAP_BASE_CONFIG,
    radius=10,
)

train_stations_scatter_map.update_layout(**LAYOUT_BASE_CONFIG)
train_stations_density_map.update_layout(**LAYOUT_BASE_CONFIG)

train_stations_density_map.update_coloraxes(showscale=False)

###########
# Network #
###########

network_A = px.line_mapbox(
    network_df[network_df["type"] == NetworkType.A.value], **LINE_BASE_CONFIG
)

network_B = px.line_mapbox(
    network_df[network_df["type"] == NetworkType.B.value], **LINE_BASE_CONFIG
)

network_C = px.line_mapbox(
    network_df[network_df["type"] == NetworkType.C.value], **LINE_BASE_CONFIG
)

network_D = px.line_mapbox(
    network_df[network_df["type"] == NetworkType.D.value], **LINE_BASE_CONFIG
)

network_A.update_layout(**LAYOUT_BASE_CONFIG, showlegend=False)
network_B.update_layout(**LAYOUT_BASE_CONFIG, showlegend=False)
network_C.update_layout(**LAYOUT_BASE_CONFIG, showlegend=False)
network_D.update_layout(**LAYOUT_BASE_CONFIG, showlegend=False)
