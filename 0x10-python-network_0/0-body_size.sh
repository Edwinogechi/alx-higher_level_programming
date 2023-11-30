#!/bin/bash
#Make request and display body of the response
curl -s "$1" | wc -c
