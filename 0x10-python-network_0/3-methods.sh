#!/bin/bash
# makes a URL a display all HTTP methods the server will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
