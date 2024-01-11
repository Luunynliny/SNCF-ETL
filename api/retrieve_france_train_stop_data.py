import json
from os import path

import requests

###############
# ENVIRONMENT #
###############

SECRET_TOKEN_PATH = path.join(
    path.dirname(path.abspath(__file__)), "../../../SECRET_TOKEN.txt"
)

STOP_POINTS_DATA_PATH = path.join(
    path.dirname(path.abspath(__file__)), "../stop_points.json"
)

ITEM_LIMIT = 1000

########################
# Get secret api token #
########################

with open(SECRET_TOKEN_PATH) as f:
    SECRET_TOKEN = f.read()

########################################
# Retrieve total number of stop points #
########################################

res = requests.get(
    "https://@api.navitia.io/v1/coverage/fr-idf/stop_points",
    auth=(SECRET_TOKEN, ""),
    params={"count": 1},
)

data = res.json()

TOTAL_RESULTS = data["pagination"]["total_result"]
TOTAL_PAGE_COUNT = TOTAL_RESULTS // ITEM_LIMIT

#############################
# Retrieve stop points data #
#############################

stop_points_data = []

for page_count in range(0, TOTAL_PAGE_COUNT + 1):
    res = requests.get(
        "https://api.sncf.com/v1/coverage/fr-idf/stop_points",
        auth=(SECRET_TOKEN, ""),
        params={"count": ITEM_LIMIT, "start_page": page_count},
    )

    data = res.json()

    for stop_point in data.get("stop_points"):
        stop_points_data.append(
            {
                "id": stop_point["id"],
                "name": stop_point["name"],
                "label": stop_point["label"],
                "coord": stop_point["coord"],
            }
        )

##############
# Store data #
##############

with open(STOP_POINTS_DATA_PATH, "w") as f:
    json.dump(stop_points_data, f, ensure_ascii=False, indent=4)
