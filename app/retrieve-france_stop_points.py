from os import path

import requests
from icecream import ic

########################
# Get secret api token #
########################

with open(
    path.join(path.dirname(path.abspath(__file__)), "../SECRET_TOKEN.txt")
) as f:
    SECRET_TOKEN = f.read()

########################################
# Retrieve total number of stop points #
########################################

# res = requests.get(
#     "https://@api.navitia.io/v1/coverage/fr-idf/stop_points",
#     auth=(SECRET_TOKEN, ""),
#     params={"count": 1},
# )
# data = res.json()

TOTAL_RESULTS = 35397  # data["pagination"]["total_result"]

#############################
# Retrieve stop points data #
#############################

res = requests.get(
    "https://@api.navitia.io/v1/coverage/fr-idf/stop_points",
    auth=(SECRET_TOKEN, ""),
    params={"count": 2},
)
data = res.json()

for stop_point in data.get("stop_points"):
    _id = stop_point["id"]
    name = stop_point["name"]
    label = stop_point["label"]
    lon, lat = stop_point["coord"].values()

    ic(_id, name, label, lon, lat)

    break
