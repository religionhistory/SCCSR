"""
vmp 2023-06-04
manually re-coding some literacy answers based on expert coding. 
wait to get green light for some of the questions 
"""

import pandas as pd

# recodings
recoding = [
    # entry id, question code, value
    [182, "available", 1],
    [210, "available", 1],
    [378, "used", 1],
    [378, "available", 1],
    [387, "used", 1],
    [387, "available", 1],
    [390, "used", 1],
    [390, "available", 1],
    [423, "used", 1],
    [423, "available", 1],
    [441, "used", 1],
    [441, "available", 1],
    [493, "used", 1],
    [493, "available", 1],
    [563, "used", 1],
    [563, "available", 1],
    [570, "used", 1],
    [570, "available", 1],
    [590, "used", 1],
    [590, "available", 1],
    [607, "used", 1],
    [607, "available", 1],
    [633, "used", 1],
    [633, "available", 1],
    [770, "used", 1],
    [770, "available", 1],
    [802, "used", 1],
    [802, "available", 1],
    [812, "used", 1],
    [812, "available", 1],
    [824, "used", 1],
    [824, "available", 1],
    [826, "used", 1],
    [826, "available", 1],
    [846, "used", 1],
    [846, "available", 1],
    [855, "used", 1],
    [855, "available", 1],
    [857, "used", 1],
    [857, "available", 1],
    [866, "used", 1],
    [866, "available", 1],
    [908, "used", 1],
    [908, "available", 1],
    [928, "used", 1],
    [928, "available", 1],
    [935, "used", 1],
    [935, "available", 1],
    [976, "used", 1],
    [976, "available", 1],
    [980, "used", 1],
    [980, "available", 1],
    [941, "used", 1],
    [941, "available", 1],
    [988, "used", 1],
    [988, "available", 1],
    [991, "used", 1],
    [991, "available", 1],
    [1109, "used", 1],
    [1109, "available", 1],
    [1136, "used", 1],
    [1136, "available", 1],
    [1156, "used", 1],
    [1156, "available", 1],
    [1218, "used", 1],
    [1218, "available", 1],
    [1334, "used", 1],
    [1334, "available", 1],
    [1340, "used", 1],
    [1340, "available", 1],
    [1456, "used", 1],
    [1456, "available", 1],
    [1529, "used", 1],
    [1529, "available", 1],
    [1619, "used", 1],
    [1619, "available", 1],
    [1740, "used", 1],
    [1740, "available", 1],
    [1872, "used", 1],
    [1872, "available", 1],
    [1903, "used", 1],
    [1903, "available", 1],
    [1918, "used", 1],
    [1918, "available", 1],
    [1938, "used", 1],
    [1938, "available", 1],
    [1958, "used", 1],
    [1958, "available", 1],
    [1962, "used", 1],
    [1962, "available", 1],
    [1972, "used", 1],
    [1972, "available", 1],
    [1978, "used", 1],
    [1978, "available", 1],
    [1983, "used", 1],
    [1983, "available", 1],
    [2003, "used", 1],
    [2003, "available", 1],
    [2084, "used", 1],
    [2084, "available", 1],
    [2233, "used", 1],
    [2233, "available", 1],
    [2266, "used", 1],
    [2266, "available", 1],
    [2273, "used", 1],
    [2273, "available", 1],
]

# comments (do we really want to code this?)
comments = [
    # entry id, question, comment
    [
        928,
        "distinct",
        "Distinct written language for Lakota as a whole, but not distinct for the Ghost Dance movement.",
    ],
    [
        770,
        "distinct",
        "There are arguably specific written languages for Thai Buddhists (Thai-Pali and Khom script) but they are not distinct to this religious group",
    ],
]

# load full data
answerset = pd.read_csv("../data_clean/answerset.csv")

# first do the main recoding
answerset = answerset[
    ["entry_id", "entry_name", "question_id", "question_name", "poll_name"]
].drop_duplicates()

# find the relevant questions
question_ids = [
    3166,  # distinct written language (group v5)
    3173,  # used (v5)
    3175,  # available (v5)
    5220,  # distinct written language (group v6)
    5222,  # available (v6)
    5223,  # used (v6)
]
literacy_questions = answerset[answerset["question_id"].isin(question_ids)]
literacy_questions.groupby(["poll_name", "question_name", "question_id"]).size()

# now we need to create the grid of values
literacy_grid = literacy_questions[
    ["question_id", "question_name", "poll_name"]
].drop_duplicates()
entry_poll = answerset[["entry_id", "entry_name", "poll_name"]].drop_duplicates()
entry_poll = entry_poll[entry_poll["poll_name"].str.contains("Group")]
literacy_grid = literacy_grid.merge(entry_poll, on="poll_name", how="inner")

# verify that this was correct
n_group_entries = len(entry_poll)
n_questions = 3
n_rows = n_group_entries * n_questions
assert len(literacy_grid) == n_rows

# apply temporary mapping
question_mapping = {
    3166: "distinct",
    3173: "used",
    3175: "available",
    5220: "distinct",
    5222: "available",
    5223: "used",
}
literacy_grid["question_code"] = literacy_grid["question_id"].map(question_mapping)

# turn recode into a dataframe
recoding_df = pd.DataFrame(
    recoding, columns=["entry_id", "question_code", "answer_value"]
)
recoding_df["answer"] = "Yes"

# merge (here we get nan in the cases where original answer was nan)
merged_df = recoding_df.merge(
    literacy_grid, on=["entry_id", "question_code"], how="left"
)
assert len(recoding_df) == len(merged_df)
assert recoding_df["entry_id"].nunique() == merged_df["entry_id"].nunique()

# select columns and re-order
merged_df = merged_df[
    ["entry_id", "entry_name", "question_id", "question_name", "answer", "answer_value"]
]
merged_df = merged_df.sort_values(["entry_id", "question_id"])

# save
merged_df.to_csv("../data_clean/literacy_recode.csv", index=False)
