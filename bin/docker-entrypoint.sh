#!/bin/sh
set -e

gunicorn --bind 0.0.0.0:$PORT "$1"
