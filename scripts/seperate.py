import json
import os
import pandas as pd

# Define the directory containing JSONL files
jsonl_dir = 'dataset/data_files/data/1/data'

# Create the "outputs" folder if it doesn't exist
output_folder = 'outputs'
os.makedirs(output_folder, exist_ok=True)

# Load data from multiple JSONL files into a single DataFrame
all_data = pd.DataFrame()
for filename in os.listdir(jsonl_dir):
    if filename.endswith('.jsonl'):
        file_path = os.path.join(jsonl_dir, filename)
        data = pd.read_json(file_path, lines=True)
        all_data = pd.concat([all_data, data], ignore_index=True)

# Define the languages of interest (English, Swahili, German)
languages = ['en', 'sw', 'de']

# Create separate JSONL files for each language and set (test, train, dev)
for language in languages:
    for set_name in ['test', 'train', 'dev']:
        # Filter data for the current language and set
        filtered_data = all_data[(all_data['locale'].str.split('-').str[0] == language) & (all_data['partition'] == set_name)]
        
        # Determine the output filename
        output_filename = f'{language}_{set_name}.jsonl'
        output_file = os.path.join(output_folder, output_filename)

        # Save the filtered data to a JSONL file
        filtered_data.to_json(output_file, orient='records', lines=True)

print("JSONL files generated and stored in the 'outputs' folder.")
