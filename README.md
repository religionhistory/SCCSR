# Overview
The Standard Cross-Cultural Sample of Religion is a product of the [Database of Religious History (DRH)](https://religiondatabase.org). 
The DRH is a qualitative-quantitative encyclopedic database of historical religious data across time and space. 
Data are contributed to the project by academic [experts](https://religiondatabase.org/landing/about/people/experts) and overseen by a panel of [editors](https://religiondatabase.org/landing/about/people/editors).
The data take the form of answers (provided by experts) to a long list of standard questions grounded in time and space.

The Standard Cross-Cultural Sample of Religion is “standard” in a different way than its namesake, The Standard Cross-Cultural Sample (SCCS). 
The SCCS was designed to control for region and cultural relatedness. 
Because of our mostly bottom-up, expert-driven data gathering method, DRH data is heavily overweighted in certain time/space regions. 
We are not aware of any publications that have implemented reweighting in analyses using data from the Database of Religious History (DRH). One possibility is to reweight in time and space. This can be achieved by using the "start_year" and "end_year" columns (available both at answer-level in ``answerset.csv`` and at entry-level in ``entry_data.csv``) and using either the world regions or the raw GIS polygon columns (available in ``region_data.csv``). One natural choice that we have experimented with is to create 100-year bins for each world region, and then assign each bin a total weight of 1. This means that entries that fall in spatiotemporal slices that contain many other entries will be downweighted, while entries that fall in spatiotemporal slices with fewer entries will be upweighted. While this approach does address spatiotemporal overweighting it does not address other types of overweighting that might be present in the database; for instance, some religious traditions might be overweighted in the database (generally or for specific spatiotemporal slices). We are hesitant to provide general recommendations for addressing issues of overweighting in the DRH because reweighting might introduce new biases and the choice of reweighting method (or to not use reweighting) will depend on the specific research questions being pursued.

On the other hand, DRH data is “standard” in the sense that whatever Group, Place of Text is being portrayed, experts are answering a standardized set of questions, allowing a degree of comparison and quantitative analysis that has simply never been possible before. 
As the DRH grows, top-down data-gathering pushes will be targeted at underrepresented regions of the world, with the goal of making future versions of the SCCSR more and more comprehensive. 

The Standard Cross-Cultural Sample of Religion (SCCSR.v1) is provided under CC-BY-4.0 license. 

The primary entry into the data is via the files provided in the `data_clean/` directory.
This consists of seven `.csv` files of different elements of the database. 
The variables of each table are documented in the [README file](https://github.com/religionhistory/drh-data-dump/blob/main/data_clean/README.md) in `data_clean/`. 

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
* Slingerland, E., M. W. Monroe and M. Muthukrishna (2023). "The Database of Religious History (DRH): ontology, coding strategies and the future of cultural evolutionary analyses." Religion, Brain & Behavior 14(2): 131-160. https://doi.org/10.1080/2153599X.2023.2200825 Available at https://eprints.lse.ac.uk/119500/.

### Data Curation
* Scripts to extract data in `data_dump` (extracted to `data_raw`). The database backup is too large the include, so analysis can be reproduced from the extracted tables in `data_raw`. 
* Data curation done in `process_data` (writing to `data_clean`). 
* The preprocessed tables are documented in the [README file](data_clean/README.md) in `data_clean`. 

## Affiliation and Funding
The DRH is housed at the University of British Columbia, and has been funded by generous grants from Canada’s Social Sciences and Humanities Research Council (SSHRC), The John Templeton Foundation, and Templeton Religion Trust.

## Version 1
Based on database backup from 2024-06-23
