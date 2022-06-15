import mysql.connector
import os
mydb = mysql.connector.connect(user=os.getenv('MYSQL_USER'),
                             password=os.getenv('MYSQL_PASSWORD'),
                             host=os.getenv('MYSQL_HOST'))
cur = mydb.cursor(dictionary=True)
with open('killbill-ddl.sql', 'r') as f:
    res = cur.execute(f.read(), multi=True)
    for r in res:
        print("Running query: ", r)  # Will print out a short representation of the query
        print(f"Affected {r.rowcount} rows" )
    mydb.commit()

with open('kaui-ddl.sql', 'r') as f:
    res1 = cur.execute(f.read(), multi=True)
    for r in res1:
        print("Running query: ", r)  # Will print out a short representation of the query
        print(f"Affected {r.rowcount} rows" )
    mydb.commit()