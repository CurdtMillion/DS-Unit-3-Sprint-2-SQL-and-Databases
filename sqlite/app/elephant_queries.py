import os
import psycopg2
import sqlite3
from psycopg2.extras import DictCursor
from dotenv import load_dotenv

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg.db")
connection = sqlite3.connect(DB_FILEPATH)

load_dotenv()

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

connection_pg = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION_PG: ", type(connection_pg))
print("CONNECTION: ", type(connection))

cursor = connection.cursor()
cursor_pg = connection_pg.cursor()
print("CURSOR: ", type(cursor))
print("CURSOR_PG: ", type(cursor_pg))

## Connecting to SQLite3 DB for RPG data ##

characters = cursor.execute('SELECT * FROM charactercreator_character LIMIT 10').fetchall()
print(characters)


## Create Character Table in Postgres ##

create_character_table_query = '''
CREATE TABLE IF NOT EXISTS rpg_characters (
    character_id SERIAL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    level INT,
    exp INT,
    hp INT,
    strength INT,
    intelligence INT,
    dexterity INT,
    wisdom INT
)
'''

add_data_query = '''
INSERT INTO rpg_characters (name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES
(
  'Mr. Wizard', 45, 55, 76, 100, 1000, 50, 1000
),
(
   'Honey-Boo-Boo', 15, 2, 3, 5, 1, 1, 1
), 
(
   'Igor', 10, 43, 54, 123, 345, 66, 100 
)
'''

cursor_pg.execute(create_character_table_query)
cursor_pg.execute(add_data_query)


connection.commit()
connection.close()
connection_pg.commit()
connection_pg.close()
