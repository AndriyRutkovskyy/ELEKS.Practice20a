#!/usr/bin/env bash

RAW_DATA="$(hadoop fs -cat pract20a_hdfs_data/data.json)"
PREDICTION= curl -H "Content-type: application/json" -d "${RAW_DATA}" 'http://localhost:9999/predict'
