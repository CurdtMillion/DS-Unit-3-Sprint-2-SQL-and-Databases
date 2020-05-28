import psycopg2

DB_NAME = "krkxxpiu"
DB_USER = "krkxxpiu"
DB_PASSWORD = "ZAgtuG0XZxWhpucWqTBKqiM-6hxexCxA"
DB_HOST = "otto.db.elephantsql.com"





### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname='DB_NAME', user='DB_USER',
                        password='DB_PASSWORD', host='DB_HOST')
### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
### An example query
cur.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
cur.fetchone()



cursor.execute("SELECT * from test_table;")
#print(type(result)) #> <class 'tuple'>
#result = cursor.fetchone()
#> (1, 'A row name', None)

result = cursor.fetchall()
for row in result:
    print("-------")
    print(type(row))
    print(row)