import pandas as pd
import networkx as nx

# Load questionrelation
questionrelation = pd.read_csv("../data_raw/questionrelation.csv")

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
result_df.to_csv("../data_clean/questionrelation.csv", index=False)
