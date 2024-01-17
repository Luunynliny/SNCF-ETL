import pandas as pd
from pymongo import MongoClient

##########################
# Database configuration #
##########################

DB_HOST = "localhost"  # "db"
DB_PORT = 27017
DB_NAME = "sncf"

###################
# Access database #
###################

client = MongoClient(host=DB_HOST, port=DB_PORT)

db = client[DB_NAME]

################################
# Retrieve train stations data #
################################

cursor = db["train_stations"].find({})

train_stations_df = pd.DataFrame(list(cursor))

#########################
# Retrieve network data #
#########################

cursor = db["network"].find({})

lats, lons, codes, names, types = [], [], [], [], []

for row in list(cursor):
    geom = row["geo_shape"]["geometry"]

    match geom["type"]:
        case "LineString":
            for lon, lat in (coords := geom["coordinates"]):
                lats.append(lat)
                lons.append(lon)

            coords_cnt = len(coords)
        case "MultiLineString":
            coords_cnt = 0

            for coords in geom["coordinates"]:
                for lon, lat in coords:
                    lats.append(lat)
                    lons.append(lon)

                coords_cnt += len(coords)

    codes.extend([row["code_ligne"]] * coords_cnt)
    names.extend([row["lib_ligne"]] * coords_cnt)
    types.extend([row["type_ligne"]] * coords_cnt)

network_df = pd.DataFrame(
    {
        "lat": lats,
        "lon": lons,
        "code": codes,
        "name": names,
        "type": types,
    }
)

####################
# Close connection #
####################

client.close()
