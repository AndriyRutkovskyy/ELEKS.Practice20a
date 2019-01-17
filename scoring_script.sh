#!/usr/bin/env bash

RAW_DATA="$(hadoop fs -cat pract15/data.json)"
PREDICTION= curl -H "Content-type: application/json" -d "${RAW_DATA}" 'http://localhost:9999/predict'
