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

## World Regions
* World region assigned based on overlap with countries (that have assigned world region)
* 4 regions lacking geom object (will not have associated world region)
* 27 regions with geoms that are not "completed" (we are using these anyways currently) 

# Known issues
## Question Relation
* Currently mapping to lowest Question ID within group. 
* Working to correct missing relations between questions.

## Answerset
* Filtering out answers that have "history_parent_id" in the database (which remoevs outdated answers)
* We need to document how rows are missing when parent answers are not "Yes". 

## Branching questions
* Some weird values here (e.g., duplications) that we fix (but we should check up on how this happens). 

## Entity tags
* The organization seems weird to me, for instance it is possible to have the "Catholicism" tag without "Christian Traditions". These are at the same level in the hierarchy (which explains how this is possible), but would seem more natural if "Christian Traditions" was at a higher level (level 2 which it is currently) and "Catholicism" was a child tag (i.e., at level 3 in the hierarchy). 

## Data that is missing
* editor_id, editor_name in entry_data.csv (add to SQL extraction script). 

## Column names
* Make sure that we agree on the column names used. 