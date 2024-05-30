"""
vmp 2023-05-29
manually re-coding some literacy answers based on expert coding. 
wait to get green light for some of the questions 
"""

import numpy as np
import pandas as pd

recoding = [
    # entry id, question, new value
    [182, available, 1],
    [210, available, 1],
    [423, available, 1],
    [423, used, 1],
    [607, available, 1],
    [607, used, 1],
    [1456, available, 1],
    [1456, used, 1],
    [2266, available, 1],
    [2266, used, 1],
]

# temporary test
answerset = pd.read_csv("../data_clean/answerset.csv")
test = answerset[answerset["entry_id"] == 2021]
test[test["answer"].str.contains("ARTICLES OF FAITH")]
