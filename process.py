import pandas as pd
import psycopg2

# Connect to the Postgres database
conn = psycopg2.connect(dbname='mydatabase', user='myusername', password='mypassword', host='localhost', port='5432')

# Load the component data into a pandas DataFrame
df = pd.read_sql_query('SELECT * FROM component_data', conn)

# Perform data processing on the DataFrame
df['value'] = pd.to_numeric(df['value'])
df = df.groupby(['component', pd.Grouper(key='timestamp', freq='1D')]).mean()

# Insert the processed data into the Postgres table
cur = conn.cursor()
for index, row in df.iterrows():
  timestamp = index[1].strftime('%Y-%m-%d')
  component = index[0]
  value = row['value']
  cur.execute('INSERT INTO processed_component_data (date, component, value) VALUES (%s, %s, %s)', (timestamp, component, value))
cur.close()

# Commit the changes and close the connection
conn.commit()
conn.close()
