#!/bin/sh
set -e

# Run migrations
python expense_manager/manage.py migrate --noinput

# Start server
exec "$@"
