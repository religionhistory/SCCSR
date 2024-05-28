import numpy as np
import pandas as pd

# load data
region_data = pd.read_csv("../data_raw/region_data.csv")
entry_data = pd.read_csv("../data_raw/entry_data.csv")

# only worry about the regions that are in the data
entry_regions = entry_data[["entry_id", "entry_name", "region_id"]].drop_duplicates()
region_data = region_data.merge(entry_data, on="region_id", how="inner")

# non-completed regions
not_completed = region_data[
    (region_data["completed"] == False) | (region_data["gis_region"].isna())
]
not_completed = not_completed.rename(columns={"completed": "region_completed"})
not_completed["region_missing"] = not_completed["gis_region"].isna()

not_completed = not_completed[
    [
        "entry_id",
        "entry_name",
        "region_id",
        "region_name",
        "region_completed",
        "region_missing",
    ]
]
not_completed = not_completed.sort_values("entry_id")
not_completed.to_csv("../data_clean/region_not_completed.csv", index=False)
