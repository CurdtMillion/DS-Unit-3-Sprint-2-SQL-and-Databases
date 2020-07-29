import pandas as pd
import os
import psycopg2
import sqlite3
from psycopg2.extras import DictCursor
from dotenv import load_dotenv

titanic = pd.read_csv('sqlite\data\titanic.csv')
connection = sqlite3.connect('titanic')
titanic.to_sql('titanic', con=connection, if_exists='replace')

load_dotenv()

DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")
DB_HOST = os.getenv("DB_HOST", default="OOPS")

print("CONNECTION: ", type(connection))
cursor = connection.cursor()

create_character_table_query = '''
CREATE TABLE IF NOT EXISTS titanic (
    Survived INT,
    Pclass INT,
    Name VARCHAR (30) NOT NULL,
    Sex VARCHAR (30) NOT NULL,
    Age INT,
    Siblings/Spouses Aboard INT,
    Parents/Children Aboard INT,
    Fare FLOAT
)
'''


