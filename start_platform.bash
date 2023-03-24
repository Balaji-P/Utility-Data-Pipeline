#!/bin/bash

# Run the ingest script
python3 sensor_ingest.py &

# Run the processor script
python3 sensor_processor.py
