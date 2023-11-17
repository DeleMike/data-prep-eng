"""
We want to combine all the domains ['book', 'digital', 'news', 'proverbs', 'tedTalks']
Then make them into dev.tsv and test.tsv file
These files will be used during evaluation and testing
"""
import random

from .helpers import domains
from pathlib import Path

def combine_data(type_of_dataset='dev'):
    # List of domains to combine
    domains = ['book', 'digital', 'news', 'proverbs', 'tedTalks']

    # Initialize an empty list to store combined data
    combined_data = []
    header = None  # Initialize header variable
    for domain in domains:
        file_path = Path('.').resolve() / f"data_prep_eng/output_data/menyo20k_data/{type_of_dataset}_prep_data/yor_{type_of_dataset}_{domain}.tsv"
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                # Read the content of the file
                content = file.read()

                # Split the content into lines
                lines = content.split('\n')

                # Skip the header line and store it
                if header is None:
                    header = lines[0]
                    lines = lines[1:]

                # Add a new column for the source of data in each line
                lines = [f"{line}\t{domain}" for line in lines]

                # Append the lines to the combined data list
                combined_data.extend(lines)
        except FileNotFoundError:
            print(f"File not found: {file_path}")

    # Shuffle the combined data
    random.shuffle(combined_data)

    # Combine all data into a single string
    combined_content = '\n'.join(combined_data)

    # Save the combined content to a new file
    output_path = Path('.').resolve() / f"data_prep_eng/output_data/{type_of_dataset}.tsv"
    with open(output_path, 'w', encoding='utf-8') as output_file:
        # Write the header
        output_file.write(f"{header}\tSource of Data\n")

        # Write the combined content
        output_file.write(combined_content)

    print(f"Combined file saved to {output_path}")

