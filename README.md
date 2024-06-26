# Overview
Data curation for Standard Cross-Cultural Sample of Religion (SCCSR.v1) provided under CC-BY-4.0 license. 

This consists of seven `.csv` files of different elements of the database. The variables of each table are documented in the [README file](https://github.com/religionhistory/drh-data-dump/blob/main/data_clean/README.md) in `data_clean`. 


Name | Description
 --- | --- 
[answerset.csv](./data_clean/answerset.csv) | The complete answerset for published entries in the Database of Religious History (DRH). It is connected to other tables through the `question_id`, `entry_id` and `region_id` columns. 
[entry_data.csv](./data_clean/entry_data.csv) | Metadata for entries published in the Database of Religious History (DRH). This is connected to other tables through the `entry_id` and `region_id` columns.
[region_data.csv](./data_clean/region_data.csv) | Region information. The `gis_region` column contains the raw multipolyogons. Regions are assigned a unique `world_region` based on the closest world region by country overlap.
[entity_tags.csv](./data_clean/entity_tags.csv) | Entity tags. Tags are hierarchically structured (see the `entrytag_level` and `entrytag_path` columns). An entry (`entry_id`) can have multiple tags. 
[questionrelation.csv](./data_clean/questionrelation.csv) | The relationships between questions. The Database of Religious History (DRH) employs multiple polls, and some questions are related across polls, (either as a question with exactly the same wording or a similar question). 
[literacy_recode.csv](./data_clean/questionrelation.csv) | Editorially recoded values for **Written Language** answers for the **Religious Group (v5)** and **Religious Group (v6)** polls. 
[social_complexity_recode.csv](./data_clean/questionrelation.csv) | Editorially recoded values for **Social Complexity** answers for the **Religious Group** and **Religious Text** polls. 

## How to cite
When using DRH data, please reference both: 

* the DRH site ([religiondatabase.org](https://religiondatabase.org))
* Slingerland, E., M. W. Monroe and M. Muthukrishna (2023). "The Database of Religious History (DRH): ontology, coding strategies and the future of cultural evolutionary analyses." Religion, Brain & Behavior 14(2): 131-160. Available at https://eprints.lse.ac.uk/119500/.

### Data Curation
* Scripts to extract data in `data_dump` (extracted to `data_raw`). The database backup is too large the include, so analysis can be reproduced from the extracted tables in `data_raw`. 
* Data curation done in `process_data` (writing to `data_clean`). 
* The preprocessed tables are documented in the [README file](data_clean/README.md) in `data_clean`. 

## Affiliation and Funding
The DRH is housed at the University of British Columbia, and has been funded by generous grants from Canada’s Social Sciences and Humanities Research Council (SSHRC), The John Templeton Foundation, and Templeton Religion Trust.

## Version 1
Based on database backup from 2024-06-23
