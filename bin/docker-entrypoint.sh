#!/bin/sh
set -e

if [[ !$PORT ]]; then PORT=5000; fi

gunicorn --bind 0.0.0.0:$PORT "$1"
