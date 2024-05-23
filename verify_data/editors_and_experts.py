import numpy as np
import pandas as pd

answerset = pd.read_csv("../data_clean/answerset.csv")
entry_data = pd.read_csv("../data_clean/entry_data.csv")

# editor ids
answerset_editor_id = answerset["editor_id"].drop_duplicates().to_list()
entry_data_editor_id = entry_data["editor_id"].drop_duplicates().to_list()

# true
set(answerset_editor_id) == set(entry_data_editor_id)
set(answerset_editor_id) - set(entry_data_editor_id)  # empty
set(entry_data_editor_id) - set(answerset_editor_id)  # empty

# editor names
answerset_editor_name = answerset["editor_name"].drop_duplicates().to_list()
entry_data_editor_name = entry_data["editor_name"].drop_duplicates().to_list()

# true
set(answerset_editor_name) == set(entry_data_editor_name)
set(answerset_editor_name) - set(entry_data_editor_name)  # empty
set(entry_data_editor_name) - set(answerset_editor_name)  # empty

# expert ids
answerset_expert_id = answerset["expert_id"].drop_duplicates().to_list()
entry_data_expert_id = entry_data["expert_id"].drop_duplicates().to_list()

# false
set(answerset_expert_id) == set(entry_data_expert_id)
set(answerset_expert_id) - set(entry_data_expert_id)  # 164, 196, 294, 336, 1049
set(entry_data_expert_id) - set(answerset_expert_id)  # 38

# find these cases
### this one is a problem
answerset[answerset["expert_id"] == 164][
    ["entry_id", "expert_name"]
].drop_duplicates()  # Beate Pongratz-Leisten, 216
entry_data[entry_data["entry_id"] == 216]  # Karen Sonik

### this one is a problem
answerset[answerset["expert_id"] == 196][
    ["entry_id", "expert_name"]
].drop_duplicates()  # Ben Raffield, 224
entry_data[entry_data["entry_id"] == 224]  # Neil Price

### this one is not a problem
answerset[answerset["expert_id"] == 294][
    ["entry_id", "expert_name"]
].drop_duplicates()  # Robert Eno, 299
answerset[answerset["entry_id"] == 299][
    ["expert_id", "expert_name"]
].drop_duplicates()  # Robert Eno is there twice with different expert IDs (perhaps as regional and managing)
entry_data[
    entry_data["entry_id"] == 299
]  # One of the expert IDs match (name is correct)

### Guess this one is a problem although weird.
answerset[answerset["expert_id"] == 336]  # Multiple Sources: Goldman et al.
answerset[answerset["entry_id"] == 338][
    ["expert_id", "expert_name"]
].drop_duplicates()  # Multiple Sources: Goldman et al. is there twice with different expert IDs (perhaps as regional and managing)
entry_data[entry_data["entry_id"] == 338]  # Chris Carleton.

### this one I am not sure about?
answerset[answerset["expert_id"] == 1049]  # Nina Edwards
answerset[answerset["entry_id"] == 1231][
    ["expert_id", "expert_name"]
].drop_duplicates()  # Matthew Hamm and Nina Edwards
entry_data[entry_data["entry_id"] == 1231]  # Matthew Hamm

# going the other way
entry_data[entry_data["expert_id"] == 38]  # Neil Price (this is entry 224 again).

""" errors found: 
in entry_data: Karen Sonik listed as expert for entry ID 216 but the expert should be Beate Pongratz-Leisten.
in entry_data: Neil Price listed as expert for entry ID 224 but the expert should be Ben Raffield.
in entry_data: looks like "Multiple Sources" is the expert? but we have Chris Carleton. 
for entry 1231 we have both Nina Edwards and Matthew Hamm as experts but we only list Matthew Hamm in entry_data.
"""


# check something (are cases with )
editors = answerset[["entry_id", "editor_id"]].drop_duplicates()
editors.groupby(["entry_id"]).size().reset_index(name="count").sort_values(by="count")
