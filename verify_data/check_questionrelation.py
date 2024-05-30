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

# there are a couple tricky ones
# need to get parents of parents
question_parents = questionrelation_merge[
    ["question_name", "parent_question"]
].drop_duplicates()
question_parents = question_parents.rename(
    columns={"question_name": "parent_question", "parent_question": "parent_parent"}
)

focus_questions = [6925, 6932, 7765, 7772, 6773, 7612, 7613, 6882, 7722, 6881, 7721]
focus_questions = no_relation[no_relation["question_id"].isin(focus_questions)]
focus_questions.merge(question_parents, on="parent_question", how="left")

# rachel proposed problems
focus_questions = [5257, 5684, 6361, 5258]
questionrelation_merge[questionrelation_merge["question_id"].isin(focus_questions)]
no_relation[no_relation["question_id"] == 5258]


questionrelation_merge[questionrelation_merge["question_id"] == 5257]
questionrelation[questionrelation["question_id"] == 5257]
questionrelation[questionrelation["related_question_id"] == 5257]
questionrelation[questionrelation["question_id"] == 5684]
questionrelation_merge[questionrelation_merge["question_id"] == 5257]
questionrelation_merge[questionrelation_merge["question_id"] == 5684]
