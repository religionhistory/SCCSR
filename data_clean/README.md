# Standard Cross-Cultural Sample of Religion 

To access the curated data tables unzip the file `drh_tables.zip`. See documentation below.

## <a name="table-valuescsv"></a>Table [answerset.csv](./answerset.csv)

This table lists the complete answerset for published entries in the Database of Religious History (DRH). It is connected to other tables through the `question_id`, `entry_id` and `region_id` columns. 

This table has no primary key since the answerset is across both questions (`question_id`) and entries (`entry_id`); additionally, distinct answers can be given for particular date ranges (`year_from`, `year_to`), regions (`region_id`), and `branching_questions`. Different experts (`expert_id`) can provide different answers to the same (`entry_id`, `question_id`) combination, or the same expert might provide different answers. Some questions ask the expert to select all that apply or to list all sources (which can result in multiple answers for the same `entry_id`, `question_id` combination).

### Variables

Name/Property | Datatype | Description
 --- | --- | --- 
`question_id` | `int` | Standardised question ID
`question_name` | `string` | Standardised question name
`answer` | `string` | Answer to the question. The majority of questions are categorical, with the possible answers `Yes`, `No`, `Field doesn't know` and `I don't know`.     
`answer_value` | `int` | Answer value to the question. For the majority of answers the coding is `1` = `Yes`, `0` = `No`, `-1` = (`I don't know`) or (`Field doesn't know`), and for most other freetext, numeric, `specify` or answers the coding is `-1`. Other answer value coding can be found [here](other_answer_value).
`notes` | `string` | Extra descriptive information about the answer
`parent_question_id` | `float` | Standardised parent question ID. This is missing if `question_id` has no parent.
`parent_question` | `string` | Standardised parent question name. This is missing if `question_id` has no parent.
`parent_answer` | `string` | Answer to the parent question.
`parent_answer_value` | `int` | Answer value to the parent question `1` = `Yes`, `0` = `No`, `-1` = (`I don't know`) or (`Field doesn't know`)
`entry_id` | `int` | Entry ID
`entry_name` | `string` | Name of the entry
`poll_id` | `poll_id` | Poll ID of the poll the entry answers
`poll_name` | `poll_name` | Name of the poll the entry answers
`year_from` | `int` | Year from which the answer applies from
`year_to` | `int` | Year from which the answer applies to 
`branching_question` | `string` | Segment of people to which the answer applies. Either `Non-elite (common populace)`, `Elite` or `Religious Specialists`
`region_id` | `int` | Region ID of the region corresponding to the answer
`expert_id` | `int` | Expert ID of the Expert who authored the answer
`expert_name` | `string` | Name of the Expert who authored the answer
`editor_id` | `int` | Editor ID of the Editor who oversaw the answer creation
`editor_name` | `string` | Name of the Editor who oversaw the answer creation
`date_published` | `string` | Date answer was published in the format YYYY-MM-DD HH:MM:SS.mmm &plusmn;HHMM
`date_created` | `string` | Date answer was created in the format YYYY-MM-DD HH:MM:SS.mmm &plusmn;HHMM
`date_modified` | `string` | Date answer was last modified in the format YYYYY-MM-DD HH:MM:SS.mmm &plusmn;HHMM

## <a name="table-entry_datacsv"></a>Table [entry_data.csv](./entry_data.csv)

This table lists metadata for entries published in the Database of Religious History (DRH). This is connected to other tables through the `entry_id` and `region_id` columns.

### Variables

Name/Property | Datatype | Description
 --- | --- | --- 
entry_id | `int` | Entry ID. This is the Primary key
entry_name | `string` | Name of the entry
poll_id | `int` | Poll ID of the poll the entry answers
poll_name | `string` | Name of the poll the entry answers
description | `string` | Description of the entry
year_from | `int` | Start year of the entry
year_to | `int` | End year of the entry
region_id | `int` | Region ID of the region corresponding to the entry
expert_id | `int` | Expert ID of the Expert who authored the entry
expert_name | `string` | Name of the Expert who authored the entry
editor_id | `int` | Editor ID of the Editor who oversaw the entry creation
editor_name | `string` | Name of the Editor who oversaw the entry creation
date_created | `string` | Date entry was created in the format YYYY-MM-DD HH:MM:SS.mmm &plusmn;HHMM
date_modified | `string` | Date entry was last modified in the format YYYY-MM-DD HH:MM:SS.mmm &plusmn;HHMM
data_source | `string` | Source of the Data. This is either `Database of Religious History (DRH)` for entries that were created only for the DRH or the source database such as `eHRAF` or `Pulotu — Database of Pacific Religions`.

## <a name="table-region_datacsv"></a>Table [region_data.csv](./region_data.csv)

This table lists region information. The `gis_region` column contains the raw multipolyogons. Regions are assigned a unique `world_region` based on the closest world region by country overlap.

### Variables

Name/Property | Datatype | Description
 --- | --- | --- 
`region_id` | `int` | Region ID. This is the Primary key
`region_name` | `string` | Region name
`region_description` | `string` | Description of the Region
`region_tag_id` | `float` | ID of the associated region tag 
`region_tag_name` | `string` | Name of the associated region tag
`parent_tag_id` | `float` |ID of the parent of the region tag. This is missing if `region_tag_id` has no parent. 
`path` | `string` | Full path of the tag in the tagging hierarchy, in the format of `entrytag_name`[`entrytag_id`]->`entrytag_name`
`world_region` | `string` | The world regions associated with the region. These 11 world regions were selected from UNESCO World Hertigage Sites (https://worldmapper.org/maps/unesco-total-sites-2017/)
`gis_region` | `string` | MULTIPOLYGON of the region

## <a name="table-entity_tagscsv"></a>Table [entity_tags.csv](./entity_tags.csv)

This table lists entity tags. Tags are hierarchically structured (see the `entrytag_level` and `entrytag_path` columns). An entry (`entry_id`) can have multiple tags. 

### Variables

Name/Property | Datatype | Description
 --- | --- | --- 
`entry_id` | `int` | Entry ID. This is the Primary key
`entrytag_id` | `int` | ID of the associated entry tag 
`entrytag_name` | `string` | Name of the associated entry tag
`entrytag_level` | `int` | The level in the tagging hierarchy of the `entrytag_id` 
`entrytag_path` | `string` | Full path of the tag in the tagging hierarchy, in the format of `entrytag_name`[`entrytag_id`]->`entrytag_name`[`entrytag_id`]
`parent_entrytag_id` | `float` | ID of the parent of the entry tag. This is missing if `entrytag_id` has no parent

## <a name="table-questionrelationcsv"></a>Table [questionrelation.csv](./questionrelation.csv)

This table lists the relationships between questions. The Database of Religious History (DRH) employs multiple polls, and some questions are related across polls, (either as a question with exactly the same wording or a similar question). 

### Variables

Name/Property | Datatype | Description
 --- | --- | --- 
`question_id` | `int` | Question ID. This is the Primary key
`related_question_id` | `int` | The standardised related question, with the lowest `question_id` of all possible related questions
`poll_name` | `string` | Poll name of the poll associated with the `question_id`


## <a name="table-literacy_recode.csv"></a>Table [literacy_recode.csv](./questionrelation.csv)

Editorially recoded values for **Written Language** answers for the **Religious Group (v5)** and **Religious Group (v6)** polls. Specifically, the table codes cases where we believe that either a *No* answer, or a *missing answer* should be *Yes* for the following questions: 
* Is a non-religion-specific written language available to the group's adherents through an institution(s) other than the religious group in question?
* Is a non-religion-specific written language used by the group's adherents through an institution(s) other than the religious group in question?

### Variables

Name/Property | Datatype | Description
 --- | --- | --- 
`entry_id` | `int` | Entry ID. This is the Primary key
`entry_name` | `string` | Name of the entry
`question_id` | `int` | Standardised question ID
`question_name` | `string` | Standardised question name
`answer` | `string` | Recoded answer `Yes`
`answer_value` | `int` | Recoded answer value `1`

## <a name="table-social_complexity_recode.csv"></a>Table [social_complexity_recode.csv](./questionrelation.csv)

Editorially recoded values for **Social Complexity** answers for the **Religious Group** and **Religious Text** polls. 
* Society of religious group that produced the text is best characterized as 
* The society to which the religious group belongs is best characterized as (please choose one) 

### Variables

Name/Property | Datatype | Description
 --- | --- | --- 
`entry_id` | `int` | Entry ID. This is the Primary key
`entry_name` | `string` | Name of the entry
`question_id` | `int` | Standardised question ID
`question_name` | `string` | Standardised question name
`answer` | `string` | Recoded answer with the possible values `An empire`, `A state`, `A chiefdom` or `A tribe`
`notes` | `string` | Who verified the recoding decision, either `expert confirmed` or `editorial decision`

## <a name="other_answer_value"></a>Other Answer Value Coding 

The answer value coding of catergorical questions without `Yes`, `No`, `Field doesn't know` and `I don't know` answers.

**Nature of religious group [please select one]:**

`answer_value` | `answer`
--- | ---
1 | Small religious group (not related to larger religious group)
2 | Small religious group (one of many small religious groups in sample region)
3 | Small religious group (seen as being part of a related larger religious group)
4 | Small religious group (trying to be organized-controlled by larger religious group)
5 | Small religious group (actively discouraged-suppressed by larger religious group(s))
6 | Large religious group (unknown relationship to other religious groups, or presence of other religious groups unknown)
7 | Large religious group (intolerant of other affiliations)
8 | Large religious group (with smaller religious groups not officially allowed but in practice tolerated)
9 | Large official religious group with smaller religious groups also openly allowed

**Moral norms apply to:**
`answer_value` | `answer`
--- | ---
1 | Only specialized religious class
2 | Only one class of society
3 | Only one gender
4 | All individuals within society (excepting slaves, aliens)
5 | All individuals within society
6 | All individuals within contemporary world
7 | All individuals (any time period)

**How strict is pilgrimage:**

`answer_value` | `answer`
--- | ---
0 | Optional (rare)
1 | Optional (common)
2 | Obligatory for some
3 | Obligatory for all

**What is the nature of this distinction:**

`answer_value` | `answer`
--- | ---
1 | Weakly present
2 | Present (but not emphasized)
3 | Present and clear
4 | Strongly present and highlighted

**The society to which the religious group belongs is best characterized as (please choose one):**

`answer_value` | `answer`
--- | ---
0 | Other [specify in comments]
1 | A band 
2 | A tribe
3 | A chiefdom
4 | A state
5 | An empire

**Please characterize the forms/level of food production [choose all that apply]: / Please characterize the forms/levels of food production [choose all that apply]:**

`answer_value` | `answer`
--- | ---
0 | Other [specify in comments]
1 | Gathering
2 | Hunting (including marine animals)
3 | Fishing
4 | Pastoralism
4 | Patoralism
4 | Small-scale agriculture
5 | Cannibalism
5 | Small-scale agriculture
5 | Large-scale agriculture [organized irrigation systems, etc.]
6 | Small-scale agriculture / horticultural gardens or orchards
6 | Large-scale agriculture [organized irrigation systems, etc.]
7 | Large-scale agriculture (e.g., monocropping, organized irrigation systems)
