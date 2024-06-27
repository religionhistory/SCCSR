import pandas as pd
import networkx as nx

# Load questionrelation
questionrelation = pd.read_csv("../data_raw/questionrelation.csv")

# Add a missing link between question_id 8002 and 3233
new_row = pd.DataFrame([{"question_id": 8002, "related_question_id": 3233}])
questionrelation = pd.concat([questionrelation, new_row], ignore_index=True)

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

# ensure no duplication
result_df = result_df.drop_duplicates()

# now sort values and save
result_df = result_df.sort_values(by=["related_question_id", "question_id"])

# check if there are missing question ids (this should not actually happen, but we have n=2)
unique_question_ids = result_df["question_id"].unique()
unique_answerset_ids = answerset["question_id"].unique()

# missing question ids
missing_question_ids = list(set(unique_answerset_ids) - set(unique_question_ids))

# find these in the answerset & relate to self
missing_question_ids_df = answerset[answerset["question_id"].isin(missing_question_ids)]
missing_question_ids_df["related_question_id"] = missing_question_ids_df["question_id"]

# merge with the result_df
result_df = pd.concat([result_df, missing_question_ids_df], sort=False)

# now sort values and save
result_df = result_df.sort_values(by=["related_question_id", "question_id"])
result_df.to_csv("../data_clean/questionrelation.csv", index=False)
