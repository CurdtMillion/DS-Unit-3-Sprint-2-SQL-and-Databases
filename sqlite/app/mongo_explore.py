import pymongo
import os
import json
from dotenv import load_dotenv
from pdb import set_trace as breakpoint
import sqlite3
from sql_to_mongo import put_sqltable_in_dict


load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/rpg_db?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)
print(client.list_database_names())

# get the data in a format to add it to mongoDB
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg.db")
connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)
cursor = connection.cursor()
print("CURSOR", cursor)

rpg_dbase = client.rpg_data

with open('test_data_json.txt') as json_file:
    rpg_data = json.load(json_file)

character_table = rpg_dbase.characters
character_table.insert_many(rpg_data)
print(character_table.count_documents({}))

#rpg_query = 'SELECT * FROM charactercreator_character FOR JSON PATH;'
#rpg_data = cursor.execute(rpg_query).fetchall()

print(rpg_data)
exit()



