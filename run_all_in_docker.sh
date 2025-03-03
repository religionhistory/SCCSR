set -e

# Usage:
#   1) Place postgres.dump.tar in the same folder as this script
#   2) Run: ./run_all_in_docker.sh
#
# This script will:
#   - docker-compose build the worker
#   - docker-compose up the db (in background)
#   - run generate_clean_data.sh /app/postgres.dump.tar in the worker
#   - stop and delete containers, images and volumes afterward
#
# Prerequisites:
#   - A docker-compose.yml with 'db' and 'worker' services
#   - The worker has generate_clean_data.sh script + Python/R libs installed

# Name of database dump file:
DUMPFILE="postgres.dump.tar"

# 1) Build images (ensures Dockerfile changes are up to date)
echo "=== Building Docker images ==="
docker compose build

# 2) Start only the 'db' service in the background
echo "=== Starting the DB service ==="
docker compose up -d db

# Wait a few seconds for the DB to finish starting 
sleep 5

# 3) Run the worker, calling generate_clean_data.sh with the .tar
#    We mount .:/app, so inside the container the file is /app/postgres.dump.tar
echo "=== Running generate_clean_data.sh in the 'worker' container ==="
docker compose run --rm worker bash -c "./generate_clean_data.sh /app/$DUMPFILE"

# 4) Stop all containers
echo "=== Shutting down containers and removing local images and volumes ==="
docker compose down --rmi local --volumes

echo "=== Done! Check data_clean/drh_tables.zip on your host machine. ==="
