# create a shell script to run the data processing pipeline.
# call the ingest script to load the input data into Postgres, then call the processing script to perform data processing on the ingested data.

#!/bin/bash

# Run the ingest script
python3 ingest.py

# Run the processing script
python3 process.py
