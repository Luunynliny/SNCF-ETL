import pandas as pd
from pymongo import MongoClient

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

################################
# Retrieve train stations data #
################################

cursor = db["train_stations"].find({})

train_stations_df = pd.DataFrame(list(cursor))

####################
# Close connection #
####################

client.close()
