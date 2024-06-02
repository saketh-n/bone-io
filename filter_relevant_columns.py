# Define keywords that are relevant to your study
keywords = ['Tissue', 'Development', 'Stage', 'Treatment', 'Gene', 'Expression', 'Sample']

# Read the unique column names
with open('unique_column_names.txt', 'r') as file:
    unique_columns = file.readlines()

# Filter relevant columns based on keywords
relevant_columns = [col.strip() for col in unique_columns if any(keyword in col for keyword in keywords)]

# Write relevant columns to a new file
with open('relevant_columns.txt', 'w') as file:
    for col in relevant_columns:
        file.write(f"{col}\n")
