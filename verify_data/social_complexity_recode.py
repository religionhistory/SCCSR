import numpy as np
import pandas as pd

# get answersets
answerset = pd.read_csv("../data_clean/answerset.csv")


# search for more questions;
questions = [
    "Society of religious group that produced the text is best characterized as:",
    "Are there specific elements of society involved with the destruction of the text?",
    "Are there specific elements of society that have controlled the reproduction of the text?",
]

# find them
answerset_social_complexity = answerset[answerset["question_name"].isin(questions)]
answerset_social_complexity.groupby(
    ["question_id", "question_name", "poll_name"]
).size()

# the problems are the following
d = pd.read_csv("../data_raw/answerset.csv")
d = d[["entry_id", "entry_name", "branching_question"]].drop_duplicates()
d.head(10)

# find the problem case;
