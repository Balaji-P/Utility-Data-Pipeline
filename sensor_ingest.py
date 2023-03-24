# create a Python script to ingest the sensor data and publish it to a message broker.
# use the paho-mqtt library to interact with the message broker.

import paho.mqtt.client as mqtt
import json

# Define the MQTT broker settings
broker_address = "localhost"
broker_port = 1883
client_id = "sensor-ingest"

# Define the sensor data
sensor_data = {
  "timestamp": "2022-04-01T12:00:00Z",
  "sensor_id": "1234567890",
  "temperature": 25.0,
  "humidity": 50.0
}

# Connect to the MQTT broker and publish the sensor data
client = mqtt.Client(client_id=client_id)
client.connect(broker_address, broker_port)
client.publish("sensor-data", json.dumps(sensor_data))
client.disconnect()
