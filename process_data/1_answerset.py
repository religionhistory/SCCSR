import pandas as pd

# load data
answerset = pd.read_csv("../data_raw/answerset.csv")


# fix branching question duplication
def remove_branching_duplication(input_str):
    # List of possible values
    possible_values = [
        "Non-elite (common people, general populace)",
        "Religious Specialists",
        "Elite",
    ]

    # Check for nan cases and return an empty string
    if pd.isna(input_str):
        return ""

    # Extract the part after the colon
    if ":" in input_str:
        suffix = input_str.split(":")[1]
    # If missing return input
    else:
        return input_str

    # Initialize seen set and unique values list
    seen = set()
    unique_values = []

    # Check each possible value in the suffix
    for value in possible_values:
        if value in suffix and value not in seen:
            seen.add(value)
            unique_values.append(value)

    # Join the unique values with a comma and return the result
    result = ", ".join(unique_values)
    return result


branching_questions = answerset["branching_question"].unique()
branching_question_mapping = {}
for branching_question in branching_questions:
    branching_question_mapping[branching_question] = remove_branching_duplication(
        branching_question
    )
answerset["branching_question"] = answerset["branching_question"].map(
    branching_question_mapping
)

# rename columns
answerset = answerset.rename(columns={"value": "answer_value"})

# ensure that no duplicates exist
answerset = answerset.drop_duplicates()
answerset.to_csv("../data_clean/answerset.csv", index=False)
