import pandas as pd
import os
from load_data import read_data_file, load_files

def inspect_metadata_files(directory, dir_path, unique_columns):
    # Load metadata files
    metadata_frames = load_files(directory, dir_path, extension=".soft")
    
    # Collect unique column names
    for name, df in metadata_frames.items():
        unique_columns.update(df.columns)

# Set the directory path relative to the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
dir_path = os.path.join(current_dir, 'Datasets')

# Output file
output_file = os.path.join(current_dir, 'unique_column_names.txt')

# Clear the output file before writing
open(output_file, 'w').close()

# Set to collect unique column names
unique_columns = set()

# Inspect metadata files
inspect_metadata_files('Series family [metadata]', dir_path, unique_columns)
inspect_metadata_files('Annotation', dir_path, unique_columns)
inspect_metadata_files('full', dir_path, unique_columns)

# Write unique column names to the output file
with open(output_file, 'w') as file:
    for column in sorted(unique_columns):
        file.write(f"{column}\n")
