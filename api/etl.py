import requests
from pymongo import MongoClient

#####################
# API configuration #
#####################

API_BASE_URL = "https://ressources.data.sncf.com/api/explore/v2.1"

###########################
# Retrieve train stations #
###########################

res = requests.get(
    f"{API_BASE_URL}/catalog/datasets/liste-des-gares/exports/json"
)

data = res.json()

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

##############
# Store data #
##############

train_station_collection = db["train_stations"]

for train_station in data:
    train_station_collection.insert_one(
        {
            "code_uic": train_station["code_uic"],
            "libelle": train_station["libelle"],
            "code_ligne": train_station["code_ligne"],
            "lat": train_station["geo_point_2d"]["lat"],
            "lon": train_station["geo_point_2d"]["lon"],
        }
    )

####################
# Close connection #
####################

client.close()
