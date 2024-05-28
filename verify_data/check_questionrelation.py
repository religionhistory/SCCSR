import numpy as np
import pandas as pd

# data to merge with to test
answerset = pd.read_csv("../data_clean/answerset.csv")
entry_data = pd.read_csv("../data_clean/entry_data.csv")
answerset_sub = answerset[
    ["question_id", "question_name", "entry_id", "parent_question"]
].drop_duplicates()
entry_data_sub = entry_data[["entry_id", "poll_name"]].drop_duplicates()
answerentry = pd.merge(answerset_sub, entry_data_sub, on="entry_id", how="inner")
answerentry = answerentry[
    ["question_id", "question_name", "parent_question", "poll_name"]
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

no_relation.sort_values(
    ["question_name", "parent_question", "question_id"], ascending=[True, True, True]
).to_csv("missing_questionrelations.csv", index=False)

"""
# Try to just map by question name
no_relation_grouped = (
    no_relation.groupby("question_name")
    .size()
    .reset_index(name="count")
    .sort_values("count", ascending=False)
)
no_relation_grouped_name_match = no_relation_grouped[no_relation_grouped["count"] > 1]

# Okay so these 119 question names have direct mappings but are not related
no_relation_grouped_name_poll = no_relation_grouped_name_match.merge(
    answerentry, on="question_name", how="inner"
)
no_relation_grouped_name_poll
no_relation_grouped_name_poll.to_csv("missing_questionrelations.csv", index=False)
"""
