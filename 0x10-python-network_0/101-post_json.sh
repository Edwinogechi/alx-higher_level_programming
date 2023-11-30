#!/bin/bash
# Send JSON post request to a given JSOn file
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
