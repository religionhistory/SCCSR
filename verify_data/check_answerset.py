import numpy as np
import pandas as pd

# load
answerset = pd.read_csv("../data_clean/answerset.csv")

# check number of entries and questions
answerset["entry_id"].nunique()  # 1463
answerset["question_id"].nunique()  # 3389

# check inconsistent answers
inconsistent_answers = (
    answerset.groupby(
        [
            "entry_id",
            "question_id",
            "year_from",
            "year_to",
            "branching_question",
            "region_id",
            "expert_id",
        ]
    )
    .size()
    .reset_index(name="count")
)
inconsistent_answers = inconsistent_answers[inconsistent_answers["count"] > 1]

# merge back to more easily check
inconsistent_answers = pd.merge(
    inconsistent_answers,
    answerset,
    how="inner",
    on=[
        "entry_id",
        "question_id",
        "year_from",
        "year_to",
        "branching_question",
        "region_id",
        "expert_id",
    ],
)

# just go through some as a sanity check
inconsistent_answers = inconsistent_answers[
    ["entry_id", "question_id", "question_name", "answer", "answer_value"]
]

pd.set_option("display.max_colwidth", None)
inconsistent_answers.tail(15)

"""
from the top:
eid 23, qid 2326 (correct)
eid 23, qid 2330 (correct)
eid 173, qid 3022 (correct)
eid 173, qid 3151 (correct)
eid 174, qid 2330 (correct)
eid 174, qid 2841 (correct)

from the bottom:
eid 2318, qid 6340 (correct)
eid 2318, qid 6334 (if "Print Sources" is "General Variables" then we are lacking 1 reference)
eid 2317, qid 6343 (correct)
eid 2317, qid 6334 (same as above)

in sum this looks good to me. 
"""

# check the ones that have weird answers for branching questions
answerset = pd.read_csv("../data_raw/answerset.csv")
answerset["branching_question"].unique()

# find the ones that have impossible values
missing_branches = answerset[answerset["branching_question"] == " "]
missing_branches["entry_id"].unique()
missing_branches[missing_branches["entry_id"] == 2088].head(20)
missing_branches = missing_branches[
    [
        "entry_id",
        "editor_id",
        "editor_name",
        "expert_id",
        "expert_name",
    ]
].drop_duplicates()
missing_branches.to_csv("missing_branches.csv", index=False)

"""
Entry ID 256: the case for 70 answers (e.g. "Previously human spirits are present:")
Entry ID 406: the case for 1 answer ("Assigned at a specific age:")
Entry ID 1102: the case for 5 answers (e.g., "Type of excavation")
Entry ID 2079: the case for 482 answers (e.g., "Methods of Composition")
Entry ID 2080: the case for 46 answers (e.g., "Supernatural beings care about other")
Entry ID 2081: the case for 132 answers (e.g., "Are sacrifices specified by the text")
Entry ID 2088: the case for 563 answers (e.g., "Is the text stored in a specific location?")
"""

# find other impossible values
answers = answerset["branching_question"].unique().tolist()
answers_duplication = answers[15:]
answerset_duplication = answerset[
    answerset["branching_question"].isin(answers_duplication)
]
answerset_duplication = answerset_duplication[
    [
        "entry_id",
        "question_id",
        "question_name",
        "answer",
        "editor_id",
        "editor_name",
        "expert_id",
        "expert_name",
        "branching_question",
    ]
]
answerset_duplication.to_csv("answerset_duplication.csv", index=False)

""" 
We observe the following problem. For some answers there are duplicated answers.
I am not sure how this can happen, and in the database the answers are actually
coded correctly (i.e., "No, No" is coded as "No"). However, this appears to give
us a problem with the branching questions, where we do get duplication, such that 
for instance "Elite" is coded as "Elite, Elite". Would be best if we can fix these
at the source of course. 

Entry ID 1817, Question ID 6354 ("The structure has a definite shape"): 
- The answer below is duplicated: 
"Other [specify]: and the part in front round (as it looks nowadays),
Other [specify]: and the part in front round (as it looks nowadays)"

Entry ID 1817, Question ID 6716 ("Are there orthodoxy checks:"):
- The answer below is duplicated:
"No, No"

Entry ID 1829, Question ID 4662 ("Assigned by personal choice:"):
- The answer below is duplicated:
"Yes, Yes" 

Entry ID 2054, Question ID 4854 ("The supreme high god exhibits negative emotion:")
- The answer below is duplicated: 
"Yes, Yes"

Entry ID 2054, Question ID 5226 ("Does the religious group in question provide food for themselves:")
- The answer below is duplicated:
"No, No"

Entry ID 2061, Question ID 5122 ("Does membership in this religious group require constraints on sexual activity...")
- The answer below is duplicated:
"Yes, Yes"

Entry ID 2071, Question ID 8146 ("Food")
- The answer below is duplicated:
"No, No"

Entry ID 2071, Question ID 8151 ("Supernatural beings care about murder of members of other religions")
- The answer below is (4x) duplicated:
"Field doesn't know, Field doesn't know, Field doesn't know, Field doesn't know"

Entry ID 2071, Question ID 8202 ("Mild sensory displeasure?")
- The answer below is duplicated:
"No, No"
"""
