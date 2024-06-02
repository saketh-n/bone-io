import pandas as pd
import os

# Initialize an empty dictionary to store dataframes
data_frames = {}

def read_data_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Find the line number where the table begins
    for i, line in enumerate(lines):
        if line.startswith("!platform_table_begin") or line.startswith("!dataset_table_begin"):
            start_line = i + 1
            break

    # Read the data starting from the line after the table begins
    df = pd.read_csv(file_path, sep='\t', comment='#', skiprows=start_line, low_memory=False)
    return df

def load_files(directory, dir_path, extension=".soft"):
    path = os.path.join(dir_path, directory)
    files = [f for f in os.listdir(path) if f.endswith(extension)]
    for file in files:
        file_path = os.path.join(path, file)
        data_frames[file] = read_data_file(file_path)
    return data_frames

def load_all():
    # Get the current working directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Set the directory path relative to the current directory
    dir_path = os.path.join(current_dir, 'Datasets')
    
    data_frames.update(load_files('Annotation', dir_path, '.annot'))
    data_frames.update(load_files('full', dir_path))
    data_frames.update(load_files('Series family [metadata]', dir_path))
    return data_frames

if __name__ == "__main__":
    # Load all full data files and series family metadata files
    load_all()

    # Print the loaded dataframes' keys to see what has been loaded
    print("Loaded dataframes:", data_frames.keys())
