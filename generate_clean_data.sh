# Usage (inside a container that has Postgres client + Python/R):
#   ./generate_clean_data.sh path/to/postgres.dump.tar
#
# This script:
#   - Connects to the DB service at hostname "db" (as set in docker-compose).
#   - Creates a database named "religion" if it doesn't exist.
#   - Restores the given .tar dump into that DB.
#   - Exports raw CSVs from that DB into data_raw/ using .sql queries in data_dump/.
#   - Runs the cleaning pipeline in process_data/ to create final data_clean/*.csv.
#   - Zips everything into data_clean/drh_tables.zip.
#
# Prerequisites (inside this container):
#   - Postgres client (pg_restore, psql)
#   - Python w/ pandas, numpy, etc.
#   - R + relevant packages (tidyverse, sf, etc.)

set -e  # Exit on error

# 1) Check the dump file argument
DUMPFILE="$1"
if [ -z "$DUMPFILE" ]; then
  echo "Usage: $0 <path_to_postgres_dump_tar>"
  exit 1
fi

# 2) DB connection info (matches docker-compose.yml setup)
DB_HOST="db"
DB_NAME="religion"
DB_USER="postgres"

# 3) Create the database if it doesn't exist
echo "=== Creating database '$DB_NAME' (if needed) ==="
createdb -h "$DB_HOST" -U "$DB_USER" "$DB_NAME" || true

# 4) Enable PostGIS extension
echo "=== Enabling PostGIS extension (if not present) ==="
psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c "CREATE EXTENSION IF NOT EXISTS postgis;"

# 5) Restore from the .tar dump *into* the "religion" DB (no --create)
echo "=== Restoring DB from $DUMPFILE into $DB_NAME ==="
pg_restore --verbose --no-acl --no-owner \
  -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" < "$DUMPFILE"

# 6) Export raw CSVs into data_raw/ using the .sql queries in data_dump/
mkdir -p data_raw

echo "=== Exporting answerset.csv ==="
psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" \
  -c "\copy ($(sed '$ s/;$//' data_dump/answersets.sql)) TO '/tmp/answerset.csv' CSV HEADER"
cp /tmp/answerset.csv data_raw/answerset.csv

echo "=== Exporting entry_data.csv ==="
psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" \
  -c "\copy ($(sed '$ s/;$//' data_dump/entry_data.sql)) TO '/tmp/entry_data.csv' CSV HEADER"
cp /tmp/entry_data.csv data_raw/entry_data.csv

echo "=== Exporting region_data.csv ==="
psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" \
  -c "\copy ($(sed '$ s/;$//' data_dump/region_data.sql)) TO '/tmp/region_data.csv' CSV HEADER"
cp /tmp/region_data.csv data_raw/region_data.csv

echo "=== Exporting entity_tags.csv ==="
psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" \
  -c "\copy ($(sed '$ s/;$//' data_dump/entity_tags.sql)) TO '/tmp/entity_tags.csv' CSV HEADER"
cp /tmp/entity_tags.csv data_raw/entity_tags.csv

echo "=== Exporting questionrelation.csv ==="
psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" \
  -c "\copy ($(sed '$ s/;$//' data_dump/questionrelation.sql)) TO '/tmp/questionrelation.csv' CSV HEADER"
cp /tmp/questionrelation.csv data_raw/questionrelation.csv

# 7) Run the cleaning pipeline
echo "=== Running cleaning scripts in process_data/ ==="
cd process_data
chmod +x run_preprocessing.sh
./run_preprocessing.sh
cd ..

# 8) Zip the final CSVs
echo "=== Zipping final CSVs to data_clean/drh_tables.zip ==="
cd data_clean
chmod +x zip_files.sh
./zip_files.sh
cd ..

# 9) Delete the generated CSVs in data_raw
echo "=== Deleting generated raw CSV files ==="
rm -f data_raw/answerset.csv \
      data_raw/entry_data.csv \
      data_raw/region_data.csv \
      data_raw/entity_tags.csv \
      data_raw/questionrelation.csv

# 10) Delete the cleaned CSVs (but not the zip)
echo "=== Deleting final CSVs now that they're zipped ==="
rm -f data_clean/answerset.csv \
      data_clean/entity_tags.csv \
      data_clean/entry_data.csv \
      data_clean/literacy_recode.csv \
      data_clean/questionrelation.csv \
      data_clean/social_complexity_recode.csv

echo "=== Done! Your clean data is in data_clean/drh_tables.zip ==="
