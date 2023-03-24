# create a shell script to start the Microservices-based data processing platform.
# call the ingest script to publish sensor data to the message broker
# call the processor script to subscribe to the message broker
# process the sensor data and publish the processed data to the database

#!/bin/bash

# Run the ingest script
python3 sensor_ingest.py &

# Run the processor script
python3 sensor_processor.py
