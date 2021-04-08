#!/bin/bash
# Script that sends a request to a URL passed as an argument, and displays only the status code of the response
curl -sI $1 | head -n 1 | cut -f2 -d " "
