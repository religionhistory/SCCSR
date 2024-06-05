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

# find the valid answers from group poll
answerset = pd.read_csv("../data_clean/answerset.csv")
question_id = [3492, 5174]
answerset = answerset[answerset["question_id"].isin(question_id)]
answerset["answer"].unique()

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

# save
social_complexity.to_csv("../data_clean/social_complexity.csv", index=False)
