import numpy as np
import pandas as pd

new_regions = pd.read_csv("../data_raw/new_regions.csv")
new_regions["region_id"].nunique()

old_regions = pd.read_csv("../data_raw/region_data.csv")
old_regions["region_id"].nunique()

# check the top-level regions
toplevel_tags = new_regions[new_regions["parent_tag_id"].isnull()]
toplevel_tags["region_tag_name"].unique()
toplevel_tags.head(10)

# cleaned regions
cleaned_regions = pd.read_csv("../data_clean/region_data.csv")
cleaned_regions = cleaned_regions[["region_id", "world_region"]]
cleaned_regions = cleaned_regions.merge(toplevel_tags, on="region_id", how="inner")

# find the entry ids
entry_data = pd.read_csv("../data_clean/entry_data.csv")
entry_data = entry_data[["entry_id", "region_id"]]
entry_data = entry_data.merge(cleaned_regions, on="region_id", how="inner")

"""
Pauline Christianity 2 (Entry ID 182)
World region: Europe
Original tag: Middle east.

Fiji (Entry ID 192, Region ID 32) cannot be Africa (has to be Oceania).


"""
