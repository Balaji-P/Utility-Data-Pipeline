import paho.mqtt.client as mqtt
import psycopg2
import json

# Define the MQTT broker settings
broker_address = "localhost"
broker_port = 1883
client_id = "sensor-processor"

# Connect to the MQTT broker and subscribe to the sensor data topic
def on_connect(client, userdata, flags, rc):
  print("Connected to MQTT broker")
  client.subscribe("sensor-data")

# Process the incoming sensor data and insert it into the Postgres database
def on_message(client, userdata, msg):
  data = json.loads(msg.payload)
  timestamp = data["timestamp"]
  sensor_id = data["sensor_id"]
  temperature = data["temperature"]
  humidity = data["humidity"]
  
  # Perform data processing
  # ...

  # Insert the processed data into the Postgres database
  conn = psycopg2.connect(dbname='mydatabase', user='myusername', password='mypassword', host='localhost', port='5432')
  cur = conn.cursor()
  cur.execute('INSERT INTO processed_sensor_data (timestamp, sensor_id, temperature, humidity) VALUES (%s, %s, %s, %s)', (timestamp, sensor_id, temperature, humidity))
  cur.close()
  conn.commit()
  conn.close()

# Connect to the MQTT broker and start the subscriber
client = mqtt.Client(client_id=client_id)
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, broker_port)
client.loop_forever()
