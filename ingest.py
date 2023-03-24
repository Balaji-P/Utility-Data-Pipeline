import csv
import psycopg2

# Connect to the Postgres database
conn = psycopg2.connect(dbname='mydatabase', user='myusername', password='mypassword', host='localhost', port='5432')
cur = conn.cursor()

# Read the CSV input file
with open('input.csv') as file:
  reader = csv.reader(file)
  next(reader)  # Skip the header row
  for row in reader:
    # Parse the data from the row
    timestamp = row[0]
    component = row[1]
    value = row[2]

    # Insert the data into the Postgres table
    cur.execute('INSERT INTO component_data (timestamp, component, value) VALUES (%s, %s, %s)', (timestamp, component, value))

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()
