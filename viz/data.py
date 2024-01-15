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

#############################
# Retrieve stop points data #
#############################

cursor = db["stop_points"].find({})

stop_points_df = pd.DataFrame(list(cursor))

####################
# Close connection #
####################

client.close()
