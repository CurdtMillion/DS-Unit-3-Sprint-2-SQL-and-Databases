import pandas as pd
import os
import sqlite3

buddy = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv')

connection = sqlite3.connect('buddy')
buddy.to_sql('buddy', con=connection, if_exists='replace')
print("CONNECTION: ", connection)

cursor = connection.cursor()
print("CURSOR: ", cursor)

query = "SELECT count(*) as TotalUsers FROM buddy"
result = cursor.execute(query).fetchall()
print("RESULT: ", result)


query2 = "SELECT count(*) as NatureShopping FROM buddy WHERE Nature >= 100 & Shopping >= 100"
result2 = cursor.execute(query2).fetchall()
print("RESULT: ", result2)
