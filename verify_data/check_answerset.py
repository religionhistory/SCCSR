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
    ["entry_id", "question_id", "question_name", "answer", "value"]
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
