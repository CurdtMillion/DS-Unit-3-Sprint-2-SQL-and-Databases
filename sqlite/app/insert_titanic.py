import os
import psycopg2
import sqlite3
from psycopg2.extras import DictCursor
from dotenv import load_dotenv

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "titanic.csv")
connection = sqlite3.connect(DB_FILEPATH)

load_dotenv()

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

print("CONNECTION: ", type(connection))
cursor = connection.cursor()
