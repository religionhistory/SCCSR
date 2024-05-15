import numpy as np
import pandas as pd

# data to merge with to test
answerset = pd.read_csv("../data_clean/answerset.csv")
entry_data = pd.read_csv("../data_clean/entry_data.csv")
answerset_sub = answerset[
    ["question_id", "question_name", "entry_id"]
].drop_duplicates()
entry_data_sub = entry_data[["entry_id", "poll_name"]].drop_duplicates()
answerentry = pd.merge(answerset_sub, entry_data_sub, on="entry_id", how="inner")
answerentry = answerentry[
    ["question_id", "question_name", "poll_name"]
].drop_duplicates()

answerset["question_id"].nunique()  # 3389
answerentry["question_id"].nunique()  # 3389

# merge with questionrelation
questionrelation = pd.read_csv("../data_clean/questionrelation.csv")
questionrelation["question_id"].nunique()  # 2972

questionrelation_merge = pd.merge(
    answerentry, questionrelation, on="question_id", how="inner"
)
questionrelation_merge["question_id"].nunique()  # 2972

# check the ones that we are missing now
no_relation = answerentry[
    ~answerentry["question_id"].isin(questionrelation["question_id"])
]

no_relation.groupby("poll_name").size()  # mostly Text (v1.0) and some text (v0.1)

# go through some of this data manually
## Religious Group (v5) -- has everything related to something
## Religious Group (v6) -- only "other:" is not related
no_relation[no_relation["poll_name"] == "Religious Group (v6)"]
## Religious Place (v1)
# Function:
# Body present:
# Part of Body Present:
no_relation[no_relation["poll_name"] == "Religious Place (v1)"]
## Religious Place (v)
no_relation[no_relation["poll_name"] == "Religious Place (v1.2)"]
# hard for me to tell whether any of these should be related
## Religious Text (v1.0)
no_relation[no_relation["poll_name"] == "Religious Text (v1.0)"].head(20)
no_relation[no_relation["poll_name"] == "Religious Text (v0.1)"].head(20)
# seems like a bug for Religious Text...

# Try to just map by question name
relation_names = (
    no_relation.groupby("question_name")
    .size()
    .reset_index(name="count")
    .sort_values("count", ascending=False)
)
relation_names.head(10)
no_relation[no_relation["question_name"].str.contains("Are there multiple versions")]
entry_data[entry_data["entry_id"] == 2282]
answerset[answerset["question_name"] == "Ritual purpose of text?"]

entry_x = entry_data[entry_data["poll_name"] == "Religious Text (v0.1)"]
answerset_x = answerset.merge(entry_x, on="entry_id", how="inner")
answerset_x[answerset_x["question_name"] == "Ritual purpose of text?"]

"""
okay so 2282 (v1.0) has "Ritual purpose of text?" which is a sub-question of 
"If multiple versions are proper, is there a differentiation among versions by any means?
which is itself a sub-question of:
"Are multiple versions viewed as proper?"
"""

# a lot of questions here that are not in questionrelations
# where are they then?
qid = 7823
ro = pd.read_csv("data_raw/questionrelation.csv")
ro[ro["question_id"] == qid]
ro[ro["related_question_id"] == qid]

# we seem to have some extra questions here
# what are they?
questionrelation_merge = questionrelation_merge.sort_values("related_question_id")
questionrelation_merge.iloc[2900:2910]
questionrelation_merge["question_id"].nunique()  # ahh so not enough...

# what are they?
questionrelation[
    ~questionrelation["question_id"].isin(questionrelation_merge["question_id"])
]

# any opposite cases?
questionrelation_merge[
    ~questionrelation_merge["question_id"].isin(answerset["question_id"])
]

# check with a case that we know;
answerentry[answerentry["question_name"].str.contains("")]
