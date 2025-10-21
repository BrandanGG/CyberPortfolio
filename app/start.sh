#!/bin/bash
echo "Starting Gunicorn with 4 workers on 0.0.0.0:8000..."
exec gunicorn --bind 0.0.0.0:8000 --workers 4 app:app "$@"