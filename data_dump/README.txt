1. Download the database dump
2. Make sure that the name of the database dump (postgres.dump_2024_04_07.tar) matches the variable DB_NAME in restore.sh
3. Install docker and start docker daemon 
4. run: (sudo) bash restore.sh 
5. run: (sudo) docker compose up 
6. open DBeaver and connect to database using config in restore.sh comments 
7. run the extract_answers.sql file in DBeaver to extract raw.csv 
8. run extract_entities.sql file in DBeaver to extract entry_tags.csv 
9. run extract_region.sql file in DBeaver to extract region_tags.csv 


Data dump from 2024-04-07.
Data extracted on 2024-05-12.