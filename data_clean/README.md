# Standard Cross-Cultural Sample of Religion 

To access the curated data tables unzip the file `drh_tables.zip`. See documentation below.

## <a name="table-valuescsv"></a>Table [answerset.csv](./answerset.csv)

This table lists the complete answerset for published entries in the Database of Religious History (DRH). Connected to other tables through `question_id`, `entry_id`, `region_id` columns. 

Table has no primary key since the answerset is across questions (`question_id`) and entries (`entry_id`); additionally, distinct answers can be given for particular date ranges (`year_from`, `year_to`), regions (`region_id`), and `branching_questions`. Different experts (`expert_id`) can provide different answers to the same (`entry_id`, `question_id`) combination, or the same expert might provide different answers. Some questions ask the expert to select all that apply or to list all sources (which can result in multiple answers for the same `entry_id`, `question_id` combination).

### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
`question_id` | `int` | 
`question_name` | `string` | 
`answer` | `string` | 
`answer_value` | `int` | `1` = `Yes`, `0` = `No`, `-1` = (`I don't know`) or (`Field doesn't know`)
`notes` | `string` | 
`parent_question_id` | `float` | missing if `question_id` has no parent
`parent_question` | `string` | missing if `question_id` has no parent
`parent_answer` | `string` | 
`parent_answer_value` | `int` | `1` = `Yes`, `0` = `No`, `-1` = (`I don't know`) or (`Field doesn't know`)
`entry_id` | `int` | 
`entry_name` | `string` |
`poll_id` | `poll_id` |
`poll_name` | `poll_name` |
`year_from` | `int` | 
`year_to` | `int` | 
`branching_question` | `string` | `Non-elite (common populace)`, `Elite`, `Religious Specialists`
`region_id` | `int` | 
`expert_id` | `int` | 
`expert_name` | `string` | 
`editor_id` | `int` | 
`editor_name` | `string` | 
`date_published` | `string` | YYYY-MM-DD HH:MM:SS.mmm &plusmn;HHMM
`date_created` | `string` | YYYY-MM-DD HH:MM:SS.mmm &plusmn;HHMM
`date_modified` | `string` | YYYY-MM-DD HH:MM:SS.mmm &plusmn;HHMM

## <a name="table-entry_datacsv"></a>Table [entry_data.csv](./entry_data.csv)

This table lists metadata for entries published in the Database of Religious History (DRH). Connected to other tables through `entry_id`, `region_id` columns.

Note: should we include editor here as well? We probably should.

### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
entry_id | `int` | Primary key
entry_name | `string` | 
poll_id | `int` | 
poll_name | `string` | 
description | `string` | 
year_from | `int` | 
year_to | `int` | 
region_id | `int` | 
expert_id | `int` | 
expert_name | `string` | 
editor_id | `int` | 
editor_name | `string` |
date_created | `string` | YYYY-MM-DD HH:MM:SS.mmm &plusmn;HHMM
date_modified | `string` | YYYY-MM-DD HH:MM:SS.mmm &plusmn;HHMM
data_source | `string` | 

## <a name="table-region_datacsv"></a>Table [region_data.csv](./region_data.csv)

This table lists region information. The `gis_region` column contains the raw multipolyogons.
Regions have been assigned a unique `world_region` based on country overlap (world regions taken from xxx). 

### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
`region_id` | `int` | Primary key
`region_name` | `string` | 
`region_description` | `string` | 
`region_tag_id` | `float` | 
`region_tag_name` | `string` |
`parent_tag_id` | `float` |
`path` | `string` | path in tagging hierarchy
`world_region` | `string` | 11 world regions (based on overlap: https://worldmapper.org/maps/unesco-total-sites-2017/)
`gis_region` | `string` | MULTIPOLYGON 

## <a name="table-entity_tagscsv"></a>Table [entity_tags.csv](./entity_tags.csv)

This table lists entity tags. Tags are hierarchically structured (see `entrytag_level` and `entrytag_path` columns).
An entry (`entry_id`) can have multiple tags. 

### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
`entry_id` | `int` | 
`entrytag_id` | `int` | 
`entrytag_name` | `string` | 
`entrytag_level` | `int` | `entrytag_id` level in hierarchy
`entrytag_path` | `string` | `entrytag_name`[`entrytag_id`]->`entrytag_name`[`entrytag_id`]
`parent_entrytag_id` | `float` | Missing if `entrytag_id` has no parent

## <a name="table-questionrelationcsv"></a>Table [questionrelation.csv](./questionrelation.csv)

This table lists relations between questions. The Database of Religious History (DRH) employs multiple polls.
Some questions are related across polls (either the exact same question or a similar question). 

### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
`question_id` | `int` | 
`related_question_id` | `int` | lowest `question_id` in group 
`poll_name` | `string` | 


## <a name="table-literacy_recode.csv"></a>Table [literacy_recode.csv](./questionrelation.csv)

Editorially recoded values for "Written Language" answers for the "Religious Group (v5)" and "Religious Group (v6)" polls. Specifically, the table codes cases where we believe that either a "No" answer or a missing answer should be "Yes" for the following questions: 
* Is a non-religion-specific written language available to the group's adherents through an institution(s) other than the religious group in question?
* Is a non-religion-specific written language used by the group's adherents through an institution(s) other than the religious group in question?

### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
`entry_id` | `int` | 
`entry_name` | `string` |
`question_id` | `int` | 
`question_name` | `string` |
`answer` | `string` | 
`answer_value` | `int` |

## <a name="table-social_complexity_recode.csv"></a>Table [social_complexity_recode.csv](./questionrelation.csv)

Editorially recoded values for "Social Complexity" answers for the "Religious Group" and "Religious Text" polls. 
* Society of religious group that produced the text is best characterized as 
* The society to which the religious group belongs is best characterized as (please choose one) 

### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
`entry_id` | `int` | 
`entry_name` | `string` |
`question_id` | `int` | 
`question_name` | `string` |
`answer` | `string` | 
`notes` | `string` |