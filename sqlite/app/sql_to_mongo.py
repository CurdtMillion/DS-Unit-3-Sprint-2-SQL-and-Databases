import sqlite3
import os

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg.db")
connection = sqlite3.connect(DB_FILEPATH)
cursor = connection.cursor()

query = 'SELECT * FROM charactercreator_character'

def put_sqltable_in_dict(insert_query):
    armory_it = sl_cursor.execute(insert_query)
    desc = armory_it.description
    column_names = [col[0] for col in desc]
    data = [dict(zip(column_names, row))  
        for row in armory_it.fetchall()]
    return data

cursor.execute(query)
result = cursor.execute(query).fetchall()
print(result)
