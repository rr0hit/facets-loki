import psycopg2
import os
c = psycopg2.connect(database='test', user=os.getenv('PGSQL_USER'),password=os.getenv('PGSQL_PASSWORD'),host=os.getenv('PGSQL_HOST'),port='5432')
cursor = c.cursor()
autocommit = psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
print ("ISOLATION_LEVEL_AUTOCOMMIT:", psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
c.set_isolation_level( autocommit )
cursor.execute("CREATE ROLE killbilluser WITH LOGIN INHERIT CREATEDB CREATEROLE NOREPLICATION PASSWORD 'killbill';")
cursor.execute("CREATE DATABASE killbill WITH OWNER = killbilluser;")
cursor.execute("CREATE DATABASE kaui WITH OWNER = killbilluser;")
c.close()

c = psycopg2.connect(database='killbill', user=os.getenv('PGSQL_USER'),password=os.getenv('PGSQL_PASSWORD'),host=os.getenv('PGSQL_HOST'),port='5432')
cursor = c.cursor()
autocommit = psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
print ("ISOLATION_LEVEL_AUTOCOMMIT:", psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
c.set_isolation_level( autocommit )
cursor.execute("CREATE SCHEMA killbillschema authorization killbilluser;")
cursor.execute("set schema 'killbillschema';")
cursor.execute(open("postgres-ddl.sql", "r").read())
cursor.execute(open("killbill.sql", "r").read())
cursor.execute("GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA killbillschema TO killbilluser;")
c.close()

c = psycopg2.connect(database='kaui', user=os.getenv('PGSQL_USER'),password=os.getenv('PGSQL_PASSWORD'),host=os.getenv('PGSQL_HOST'),port='5432')
cursor = c.cursor()
autocommit = psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT
print ("ISOLATION_LEVEL_AUTOCOMMIT:", psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
c.set_isolation_level( autocommit )
cursor.execute("CREATE SCHEMA kauischema authorization killbilluser;")
cursor.execute("set schema 'kauischema';")
cursor.execute(open("postgres-ddl.sql", "r").read())
cursor.execute(open("kaui.sql", "r").read())
cursor.execute("GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA kauischema TO killbilluser;")
c.close()
