import pandas as pd

# not doing anything here
entry_data = pd.read_csv("../data_raw/entry_data.csv")
entry_data.to_csv("../data_clean/entry_data.csv", index=False)
