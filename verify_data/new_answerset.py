import pandas as pd

answerset = pd.read_csv("../data_raw/answerset_en.csv")
answerset = answerset[
    [
        "entry_id",
        "entry_name",
        "question_id",
        "question_name",
        "answer",
        "answer_en",
        "value",
    ]
]


pd.set_option("display.max_colwidth", None)
discrepancy = answerset[answerset["answer"] != answerset["answer_en"]]
discrepancy
"""
Entry_ID, Question_ID, Correct
23, 3136, answer_en
491, 3018, answer_en

Some cases where we have nan for name_en
2308, 5228, 
"""
