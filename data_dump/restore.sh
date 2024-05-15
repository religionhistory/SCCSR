DB_CONTAINER=postgress-postgresql
DB_NAME=ubc-drh
DB_USER=postgres
LOCAL_DUMP_PATH="./postgres.dump_2024_04_07.tar"

# Start the database container
docker compose up -d "${DB_CONTAINER}"
sleep 5s

# Create the database
docker compose exec -T "${DB_CONTAINER}" createdb -U "${DB_USER}" "${DB_NAME}" 

# Create the PostGIS extension (if not already in the dump)
docker compose exec -T "${DB_CONTAINER}" psql -U "${DB_USER}" -d "${DB_NAME}" -c "CREATE EXTENSION IF NOT EXISTS postgis;"

# Restore the database from the dump
docker compose exec -T "${DB_CONTAINER}" pg_restore --verbose --create --no-acl --no-owner -U "${DB_USER}" -d "${DB_NAME}" < "${LOCAL_DUMP_PATH}"

# Stop the container
docker compose stop "${DB_CONTAINER}"

# DBeaver instructions
# Host: 0.0.0.0 Port: 5432
# Database: religion
# Username: postgres
# Password: postgres
