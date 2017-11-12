#!/bin/sh
set -e

port=${PORT:-"5000"}

gunicorn --bind 0.0.0.0:$port "$1"
