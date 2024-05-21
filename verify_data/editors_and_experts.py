import numpy as np
import pandas as pd

answerset = pd.read_csv("../data_clean/answerset.csv")
entry_data = pd.read_csv("../data_clean/entry_data.csv")

# editor ids
answerset_editor_id = answerset["editor_id"].drop_duplicates().to_list()
entry_data_editor_id = entry_data["editor_id"].drop_duplicates().to_list()

# true
set(answerset_editor_id) == set(entry_data_editor_id)

# editor names
answerset_editor_name = answerset["editor_name"].drop_duplicates().to_list()
entry_data_editor_name = entry_data["editor_name"].drop_duplicates().to_list()

# true
set(answerset_editor_name) == set(entry_data_editor_name)

# expert ids
answerset_expert_id = answerset["expert_id"].drop_duplicates().to_list()
entry_data_expert_id = entry_data["expert_id"].drop_duplicates().to_list()

# false
set(answerset_expert_id) == set(entry_data_expert_id)
len(answerset_expert_id)
len(entry_data_expert_id)

# there are 4 experts in the answerset that are not in the entry data
# this probably means that we need to include the expert name in the answerset
