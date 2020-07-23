import os
import psycopg2
from psycopg2.extras import DictCursor
from dotenv import load_dotenv

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg.db")

load_dotenv()

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION: ", type(connection))

cursor = connection.cursor()
print("CURSOR: ", type(cursor))


#cursor.execute('SELECT * from test_table;')
#result = cursor.fetchone()
