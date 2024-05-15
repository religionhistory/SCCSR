import numpy as np
import pandas as pd

entity_tags = pd.read_csv("../data_clean/entity_tags.csv")

# christian tags
christian_tags = [
    18,  # Christian Traditions
    774,  # Early Christianity
    775,  # Early Christianity
    915,  # Evangelicalism
    971,  # Methodism
    984,  # Medieval Christianity
    996,  # Roman Catholic
    999,  # Catholic
    1006,  # Christian Restorationism
    1014,  # Christianity of the Global south
    1015,  # Born Again Christianity
    1030,  # American Christianity
    1031,  # Pentecostal
    1032,  # Protestantism
    1169,  # Early Christian Monasticism in Egypt
    1377,  # Christian monasticism
    1424,  # Christian Theology
    1570,  # Christianity
    1573,  # Christian
    1575,  # Christianity
    43608,  # Celtic Christianity
    43643,  # Orthodox Christianity
]

christian_traditions_broad = entity_tags[
    entity_tags["entrytag_id"].isin(christian_tags)
]

# find entries that have "Christian Traditions" as a tag
christian_traditions_narrow = christian_traditions_broad[
    christian_traditions_broad["entrytag_id"] == 18
]
christian_traditions_narrow_id = christian_traditions_narrow["entry_id"].unique()

# find entries that do not have this tag
non_christian_traditions = christian_traditions_broad[
    ~christian_traditions_broad["entry_id"].isin(christian_traditions_narrow_id)
]
non_christian_traditions["entry_tag"].unique()
