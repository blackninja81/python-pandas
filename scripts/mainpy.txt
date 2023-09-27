import argparse
import json
import os
import pandas as pd

def extract_data(input_file, output_file):
    # Create a list to store DataFrames for concatenation
    selected_data_list = []

    # Read the JSONL file and extract relevant attributes
    with open(input_file, 'r') as json_file:
        data = [json.loads(line) for line in json_file]
        for record in data:
            # Extract the attributes
            id_value = record.get('id', '')
            utt_value = record.get('utt', '')
            annot_utt_value = record.get('annot_utt', '')

            # Create a DataFrame for the current record
            selected_data_list.append(pd.DataFrame({
                'id': [id_value],
                'utt': [utt_value],
                'annot_utt': [annot_utt_value]
            }))

    # Concatenate the DataFrames
    selected_data = pd.concat(selected_data_list, ignore_index=True)

    # Write the selected data to an Excel file
    selected_data.to_excel(output_file, index=False)

if __name__ == "__main__":
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='Extract data from a JSONL file and create an Excel file.')

    # Add command-line arguments (flags)
    parser.add_argument('--input', type=str, required=True, help='Path to the input JSONL file')
    parser.add_argument('--output', type=str, required=True, help='Path to the output Excel file')

    # Parse command-line arguments
    args = parser.parse_args()

    # Call the function to extract data and create an Excel file
    extract_data(args.input, args.output)
