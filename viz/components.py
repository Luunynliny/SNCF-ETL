from data import network_df
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

##################
# Train stations #
##################

# train_stations_scatter_map = px.scatter_mapbox(
#     train_stations_df,
#     lat="lat",
#     lon="lon",
#     hover_name="libelle",
#     hover_data=["code_uic", "code_ligne"],
#     zoom=ZOOM_LEVEL,
#     center=FRANCE_CENTER,
# )

# train_stations_density_map = px.density_mapbox(
#     train_stations_df,
#     lat="lat",
#     lon="lon",
#     hover_name="libelle",
#     hover_data=["code_uic", "code_ligne"],
#     zoom=ZOOM_LEVEL,
#     center=FRANCE_CENTER,
#     radius=10,
# )

# train_stations_density_map.update_coloraxes(showscale=False)

###########
# Network #
###########

network_domestic = px.line_mapbox(
    network_df[network_df["type"] == "Ligne proprement dite"],
    lat="lat",
    lon="lon",
    hover_name="name",
    hover_data=["code"],
    color="code",
    line_group="id",
    zoom=ZOOM_LEVEL,
    center=FRANCE_CENTER,
)

network_railroad = px.line_mapbox(
    network_df[
        network_df["type"] == "Voie de desserte de voies ferrées de port"
    ],
    lat="lat",
    lon="lon",
    hover_name="name",
    hover_data=["code"],
    color="code",
    zoom=ZOOM_LEVEL,
    center=FRANCE_CENTER,
)

network_connection = px.line_mapbox(
    network_df[network_df["type"] == "Raccordement"],
    lat="lat",
    lon="lon",
    hover_name="name",
    hover_data=["code"],
    color="code",
    zoom=ZOOM_LEVEL,
    center=FRANCE_CENTER,
)

network_domestic.update_layout(showlegend=False)
network_railroad.update_layout(showlegend=False)
network_connection.update_layout(showlegend=False)
