import pandas as pd
import networkx as nx

# Load questionrelation
questionrelation = pd.read_csv("../data_raw/questionrelation.csv")

""" potential edits 
add_rows = [
    (5258, 6361),  # Place v1 to v1.2
    (6759, 4652),  # Text v0.1 to v1.0
    (6860, 7700),  # Text v0.1 to v1.0
    (7560, 8400),  # Text v0.1 to v1.0
    (7561, 8401),  # Text v0.1 to v1.0
    (7562, 8402),  # Text v0.1 to v1.0
    (7563, 8403),  # Text v0.1 to v1.0
    (6943, 7783),  # Text v0.1 to v1.0
    (7889, 6674),  # Text v1.0 to Place v1.2
    (6869, 5168),  # Text v0.1 to Group v6
    (7709, 5168),  # Text v1.0 to Group v6
]

rows_remove = [5257, 6923, 6924, 6925, 6928, 6931, 6932]

values_rename = {
    6925: 7772,
    6932: 7765,
}
"""

# Build the graph
G = nx.Graph()
for _, row in questionrelation.iterrows():
    G.add_edge(row["question_id"], row["related_question_id"])

# Find connected components
connected_components = list(nx.connected_components(G))

# Create a new DataFrame for the output with the smallest question_id in each component as the related_question_id
new_labels = []
for component in connected_components:
    min_question_id = min(
        component
    )  # Find the minimum question_id in the current component
    for question_id in component:
        new_labels.append(
            {"question_id": question_id, "related_question_id": min_question_id}
        )

result_df = pd.DataFrame(new_labels)

# now add the poll name and filter out cases that are not in our dataset
answerset = pd.read_csv("../data_clean/answerset.csv")
answerset = answerset[["question_id", "poll_name"]].drop_duplicates()
result_df = result_df.merge(answerset, on="question_id", how="inner")

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

# now sort values and save
result_df = result_df.sort_values(by=["related_question_id", "question_id"])
result_df.to_csv("../data_clean/questionrelation.csv", index=False)
