import pandas as pd

entry_data = pd.read_csv("../data_raw/entry_data.csv")

# manually fix cases where expert is wrong
# this happens when the person creating the entry is not the expert

# (entry_id, new_expert_id, new_expert_name)
updates = [
    (216, 164, "Beate Pongratz-Leisten"),
    (224, 196, "Ben Raffield"),
    (338, 336, "Multiple Sources: Goldman et al."),
]

# loop through updates and apply
for entry_id, editor_id, editor_name in updates:
    entry_data.loc[entry_data["entry_id"] == entry_id, "expert_id"] = editor_id
    entry_data.loc[entry_data["entry_id"] == entry_id, "expert_name"] = editor_name

# check the inconsistencies we have now
answerset = pd.read_csv("../data_clean/answerset.csv")
answerset_expert_id = answerset["expert_id"].drop_duplicates().to_list()
entry_data_expert_id = entry_data["expert_id"].drop_duplicates().to_list()
set(answerset_expert_id) - set(entry_data_expert_id)  # 294, 1049

"""
remaining 2 inconsistencies are okay;
294: same expert has 2 different expert IDs in the answerset. 
1049: the relevant entry has 2 editors in the answerset (we only list one in the entry data)
"""

entry_data.to_csv("../data_clean/entry_data.csv", index=False)
