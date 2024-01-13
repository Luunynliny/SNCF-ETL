import requests
from pymongo import MongoClient

#########
# PATHS #
#########

API_SECRET_TOKEN_PATH = "./SECRET_TOKEN.txt"

#####################
# API configuration #
#####################

API_BASE_URL = "https://api.sncf.com/v1/"
API_REQUEST_ITEM_LIMIT = 1000

#############################
# Retrieve API secret token #
#############################

with open(API_SECRET_TOKEN_PATH) as f:
    API_SECRET_TOKEN = f.read()

########################################
# Retrieve total number of stop points #
########################################

res = requests.get(
    f"{API_BASE_URL}/coverage/fr-idf/stop_points",
    auth=(API_SECRET_TOKEN, ""),
    params={"count": 1},
)

data = res.json()

TOTAL_RESULTS = data["pagination"]["total_result"]
TOTAL_PAGE_COUNT = TOTAL_RESULTS // API_REQUEST_ITEM_LIMIT

##########################
# Database configuration #
##########################

DB_HOST = "db"
DB_PORT = 27017
DB_NAME = "sncf"

###################
# Access database #
###################

client = MongoClient(host=DB_HOST, port=DB_PORT)

db = client[DB_NAME]

###########################
# Retrieve and store data #
###########################

stop_point_collection = db["stop_points"]

for page_count in range(0, TOTAL_PAGE_COUNT + 1):
    res = requests.get(
        f"{API_BASE_URL}/coverage/fr-idf/stop_points",
        auth=(API_SECRET_TOKEN, ""),
        params={"count": API_REQUEST_ITEM_LIMIT, "start_page": page_count},
    )

    data = res.json()

    for stop_point in data["stop_points"]:
        stop_point_collection.insert_one(
            {
                "id": stop_point["id"],
                "name": stop_point["name"],
                "label": stop_point["label"],
                "lat": stop_point["coord"]["lat"],
                "lon": stop_point["coord"]["lon"],
            }
        )
        break

    break
