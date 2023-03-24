# create a Python script to interact with the Postgres database and perform spatial queries.
# use the psycopg2 library to interact with Postgres.

import psycopg2

# Connect to the Postgres database
conn = psycopg2.connect(dbname='mydatabase', user='myusername', password='mypassword', host='localhost', port='5432')

# Define a function to create the table and insert data
def create_table():
  cur = conn.cursor()
  cur.execute('CREATE TABLE spatial_data (id SERIAL PRIMARY KEY, name VARCHAR, location GEOMETRY(Point, 4326))')
  cur.execute("INSERT INTO spatial_data (name, location) VALUES ('San Francisco', ST_PointFromText('POINT(-122.4194 37.7749)', 4326))")
  cur.execute("INSERT INTO spatial_data (name, location) VALUES ('Los Angeles', ST_PointFromText('POINT(-118.2437 34.0522)', 4326))")
  cur.close()
  conn.commit()

# Define a function to perform spatial queries
def query_spatial_data():
  cur = conn.cursor()
  cur.execute("SELECT name FROM spatial_data WHERE ST_DWithin(location, ST_PointFromText('POINT(-122.4194 37.7749)', 4326), 100000)")
  rows = cur.fetchall()
  cur.close()
  return rows

# Create the table and insert data
create_table()

# Perform a spatial query
results = query_spatial_data()
print(results)

# Close the connection
conn.close()
