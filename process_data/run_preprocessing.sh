#!/bin/bash

python3 1_answerset.py
python3 2_entry_data.py
Rscript 3_extract_world_regions.R
python3 4_entry_region.py
python3 5_questionrelation.py
python3 6_entity_tags.py
python3 7_literacy.py
python3 8_social_complexity.py