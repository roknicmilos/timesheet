#!/bin/sh

wait_for_postgres() {
  # Adapted from https://docs.docker.com/compose/startup-order/

  echo 'Waiting for PostgreSQL...'
  until PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOSTNAME" -U "$DB_USERNAME" -d "$DB_NAME" -c '\q'; do
    echo >&2 "Postgres is unavailable - sleeping"
    sleep 1
  done
}

wait_for_postgres

echo "Starting Django project..."

echo "Running development web server"
python3 manage.py runserver 0.0.0.0:8000
