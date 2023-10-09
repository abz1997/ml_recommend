from sqlalchemy import create_engine
import psycopg2
import pandas as pd

DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
ENDPOINT = '' # Change it for your AWS endpoint
USER = 'postgres'
#PASSWORD = str(input('Database Password: '))
PASSWORD = ''
PORT = 5432
DATABASE = 'postgres'
engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")

cur = engine.execute(f"SELECT * FROM products WHERE id='fffbb9f5-423d-470a-a0d5-018177258d8b'")

#print(cur.fetchall())

df = pd.read_sql('products', engine)

print(df.head())


# conn = psycopg2.connect(
#     host="",
#     database="postgres",
#     user="postgres",
#     password='')

# cur = conn.cursor()

# cur.execute("SELECT * FROM products WHERE id='fffbb9f5-423d-470a-a0d5-018177258d8b'")
# print(cur.fetchall())
