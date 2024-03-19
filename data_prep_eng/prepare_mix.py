from pathlib import Path

import os
import random

"""
We will combine train.tsv[menyo], processed_yoruba_bible.tsv[NIV Bible] and jw300.tsv into one file called, mix.tsv.
Then, we will run `csv_to_json.py` from lafand-mt repository to get our mix.json training file
"""

def prepare_mix_train_data():
    """Get mix file by combining new_train.tsv[menyo], processed_yoruba_bible.tsv[NIV Bible]
    and jw300.tsv into one file called, mix.tsv.
    We will run `csv_to_json.py` from lafand-mt repository to get our mix.json training file
    """
    # define the path to the training files
    files_to_combine = [
        Path('.').resolve() / 'data_prep_eng/output_data/yad_train.tsv',
        Path('.').resolve(
        ) / 'data_prep_eng/output_data/yoruba_bible_data/new_yoruba_bible_train_2.tsv',
        Path('.').resolve() / 'data_prep_eng/output_data/jw300.tsv'
    ]
    seed_value = 28
    random.seed(seed_value)

    # define path to store mixed file
    mix_file_contents = []

    # read each file and dump them to `output_path`
    for file_path in files_to_combine:
        print(f'For file = {file_path.name}...')
        with open(file_path, 'r', encoding='utf-8') as file:
            # Skip the first line in the TSV file
            lines = file.readlines()[1:]
            
            mix_file_contents.extend(lines)
     
    print('Total number of sentences: ', len(mix_file_contents))       
    mix_output_path = Path('.').resolve() / 'data_prep_eng/output_data/mix.tsv'
    
    # Write the mixed content to mix.tsv
    with open(mix_output_path, 'w', encoding='utf-8') as mix_file:
        # Write header
        header = "Original Sentence\tModified Sentence\tCase Rule Applied\tSource of Data\n"
        mix_file.write(header)
        
        # add a bit of randomness
        random.shuffle(mix_file_contents)
        
        # Write mixed contents
        mix_file.writelines(mix_file_contents)

            
   
   
