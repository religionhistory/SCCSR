import pandas as pd
import numpy as np

# load data
social_complexity = pd.read_csv("../data_raw/social_complexity.csv")

# rename columns
social_complexity = social_complexity.rename(
    columns={
        "Entry ID": "entry_id",
        "Entry Name": "entry_name",
        "Simplified Code": "answer_code",
        "Notes": "notes",
    }
)

# drop columns
social_complexity = social_complexity.drop(
    columns=["Original Code", "Suggested Code"]
).reset_index(drop=True)

# recode answers
answer_mapping = {
    "state": "A state",
    "empire": "An empire",
    "chiefdom": "A chiefdom",
    "tribe": "A tribe",
    "band": "A band",
}

social_complexity["answer"] = social_complexity["answer_code"].replace(answer_mapping)
social_complexity = social_complexity.drop(columns=["answer_code"])

# drop rows that are not recoded
valid_keys = answer_mapping.values()
social_complexity = social_complexity[social_complexity["answer"].isin(valid_keys)]

# other cleanup
notes_mapping = {
    "confirmed": "expert confirmed",
    "yes (says he already changed it)": "expert confirmed",
    "says he already changed it": "expert confirmed",
}
social_complexity["notes"] = social_complexity["notes"].replace(notes_mapping)
social_complexity["notes"] = np.where(
    social_complexity["notes"] != "expert confirmed",
    "editorial decision",
    social_complexity["notes"],
)

# need to add the question_id and question_name
# need to map this through poll name
answerset = pd.read_csv("../data_clean/answerset.csv")
question_ids = [3492, 5174, 7547, 8387]
answerset_social_complexity = answerset[answerset["question_id"].isin(question_ids)]
question_poll = answerset_social_complexity[
    ["question_id", "question_name", "poll_name"]
].drop_duplicates()
entry_data = pd.read_csv("../data_clean/entry_data.csv")
entry_data = entry_data[["entry_id", "poll_name"]].drop_duplicates()
grid_values = question_poll.merge(entry_data, on="poll_name", how="inner")

# now we merge inner on entry
social_complexity = social_complexity.merge(grid_values, on="entry_id", how="inner")

# select and order
social_complexity = social_complexity[
    ["entry_id", "entry_name", "question_id", "question_name", "answer", "notes"]
]
social_complexity = social_complexity.sort_values("entry_id")

# save
social_complexity.to_csv("../data_clean/social_complexity_recode.csv", index=False)
