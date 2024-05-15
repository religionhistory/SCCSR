import pandas as pd
import networkx as nx

# create the mapping for question relations #
questionrelation = pd.read_csv("../data_raw/questionrelation.csv")

# Build the graph
G = nx.Graph()
for _, row in questionrelation.iterrows():
    G.add_edge(row["question_id"], row["related_question_id"])

# Find connected components
connected_components = list(nx.connected_components(G))

# Create a new DataFrame for the output
new_labels = []
for label, component in enumerate(connected_components):
    for question_id in component:
        new_labels.append(
            {"question_id": question_id, "related_question_id": label + 1}
        )

result_df = pd.DataFrame(new_labels)

# filter out cases that are not in our dataset
answerset = pd.read_csv("../data_clean/answerset.csv")
answerset = answerset[["question_id"]].drop_duplicates()
result_df = result_df[result_df["question_id"].isin(answerset["question_id"])]

# now some of them do not have any relations
# remove if there is no relation to other questions
missing_relation = (
    result_df.groupby("related_question_id").size().reset_index(name="count")
)
missing_relation = missing_relation[missing_relation["count"] == 1]
missing_relation = missing_relation[["related_question_id"]]
result_df = result_df[
    ~result_df["related_question_id"].isin(missing_relation["related_question_id"])
]

result_df.to_csv("../data_clean/questionrelation.csv", index=False)
