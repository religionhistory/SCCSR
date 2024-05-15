# Overview
Extract and preprocess data for Database of Religious History (DRH) data dump.
* Scripts to extract data in `data_dump` (extracted to `data_raw`).
* Preprocessing done in `process_data` (writing to `data_clean`). 
* Checking done in `verify_data`. 
* Currently based on data-dump from 2024-04-07 (re-run with updated data)

# Outcome
* data_clean/answerset.csv (linking: entry_id, question_id, region_id)
* data_clean/entry_data.csv (linking: entry_id, region_id)
* data_clean/entity_tags.csv (linking: entry_id)
* data_clean/questionrelation.csv (linking: question_id)
* data_clean/region_data.csv (linking: region_id)

# Notes
## Exclusion criteria
* Entries with  "Polity" not included currently. 
* Only published entries included. 

## Question Relation
* Currently we map groups of related questions to a number without special justification (1, 2, ..., n). 
* 417 question_id are not in questionrelations (but in answerset). Some of these are definitely mistakes. 

## World Regions
* World region assigned based on overlap with countries (that have assigned world region)
* 4 regions lacking geom object (will not have associated world region)
* 27 regions with geoms that are not "completed" (we are using these anyways currently) 

## Answerset
* Filtering out answers that have "history_parent_id" in the database (which remoevs outdated answers)
* We need to document how rows are missing when parent answers are not "Yes". 

## Branching questions
* Some weird values here (e.g., duplications) that we fix (but we should check up on how this happens). 

## Entity tags
* Entity tags are a mess. I am not sure whether this is something we want to fix.