"""
social_complexity_recoded.csv downloaded from Kelly's Google Drive on 2023-05-30
"""

import numpy as np
import pandas as pd

social_complexity_recoded = pd.read_csv("../data_raw/social_complexity_recoded.csv")
social_complexity_recoded = social_complexity_recoded.rename(
    columns={
        "Entry ID": "entry_id",
        "Entry Name": "entry_name",
        "Notes": "expert_confirmed",
        "Original Code": "original_code",
        "Suggested Code": "suggested_code",
    }
)

# get the relevant questions (ID and formulation differ by poll)
question_ids = [3492, 5174, 7547, 8387]
answerset = pd.read_csv("../data_clean/answerset.csv")
answerset = answerset[
    answerset["question_name"].str.contains(
        "Society of religious group that produced the text"
    )
]
answerset.groupby(["question_name", "question_id", "poll_name"]).size()
answerset_social_complexity = answerset[answerset["question_id"].isin(question_ids)]
answerset_social_complexity_subset = answerset_social_complexity[
    [
        "question_id",
        "question_name",
        "entry_id",
        "entry_name",
        "poll_name",
        "answer",
    ]
].drop_duplicates()

# now merge on entry_id, entry_name
answerset_social_complexity = social_complexity_recoded.merge(
    answerset_social_complexity_subset, on=["entry_id", "entry_name"], how="left"
)

# find the cases where experts are having problems
modify_problems = answerset_social_complexity[
    answerset_social_complexity["entry_id"].isin([185, 1542])
]
modify_problems = modify_problems[
    ["entry_id", "entry_name", "suggested_code"]
].drop_duplicates()
entry_data = pd.read_csv("../data_clean/entry_data.csv")
entry_data = entry_data[["entry_id", "expert_name", "editor_name"]].drop_duplicates()
modify_problems = modify_problems.merge(entry_data, on="entry_id", how="inner")


# okay find the cases where we messed up
text_poll_problems = answerset_social_complexity[
    (~answerset_social_complexity["answer"].isnull())
]
text_poll_problems = text_poll_problems[
    ~text_poll_problems["answer"].str.contains("Other")
]
text_poll_problems = text_poll_problems[
    [
        "entry_id",
        "entry_name",
        "original_code",
        "answer",
        "suggested_code",
        "expert_confirmed",
        "poll_name",
    ]
]

# things that we should change in answerset instead

"""
the ones with weird signs.
these look correct on the website...
so perhaps there is a "answer_en" variable??
"""
