# Overview
Extract and preprocess data for Standard Cross-Cultural Sample of Religion (SCCSR v1). 
* Scripts to extract data in `data_dump` (extracted to `data_raw`).
* Preprocessing done in `process_data` (writing to `data_clean`). 
* Based on data-dump from 2024-06-20 (question relations extracted through API on 2024-06-24).

# Outcome
* data_clean/drh_tables.zip containing: 
	* answerset.csv 
	* entry_data.csv
	* entity_tags.csv 
	* questionrelation.csv 
	* region_data.csv 
	* literacy_recode.csv
	* social_complexity_recode.csv
