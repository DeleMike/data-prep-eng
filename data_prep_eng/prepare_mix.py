from pathlib import Path

import os
import random

"""
We will combine train.tsv[menyo], processed_yoruba_bible.tsv[NIV Bible] and jw300.tsv into one file called, mix.tsv.
Then, we will run `csv_to_json.py` from lafand-mt repository to get our mix.json training file
"""


def prepare_mix_train_data():
    """Get mix file by combining train.tsv[menyo], processed_yoruba_bible.tsv[NIV Bible]
    and jw300.tsv into one file called, mix.tsv.
    We will run `csv_to_json.py` from lafand-mt repository to get our mix.json training file
    """
    # define the path to the training files
    files_to_combine = [
        Path('.').resolve() / 'data_prep_eng/output_data/train.tsv',
        Path('.').resolve(
        ) / 'data_prep_eng/output_data/yoruba_bible_data/processed_yoruba_bible.tsv',
        Path('.').resolve() / 'data_prep_eng/output_data/jw300.tsv'
    ]
    seed_value = 28
    random.seed(seed_value)

    # define path to store mixed file
    mix_file_contents = []

    # read each file and dump them to `output_path`
    for file_path in files_to_combine:
        print(f'For file = {file_path.name}...')
        try:
            with open(file_path, 'r', encoding='utf-8') as file_:
                
                # Read the content of the file
                content = file_.read()
                # we start reading each file from the second line to avoid
                # "Original Sentence	Modified Sentence	Case Rule Applied	Source of Data"
                mix_file_contents.append(content[1:])
        except FileNotFoundError:
            print(
                f'{file_path} does not exist. Ensure your {type_of_dataset} exist before running this.')
            
    print(f'Mix File Contents Length = {len(mix_file_contents)}')
    
    # Combine contents of all files
    combined_content = ''.join(mix_file_contents)

    # Split the combined content into lines
    lines = combined_content.strip().split('\n')

    # Shuffle the lines to randomize
    random.shuffle(lines)   
    
    try:
        output_path = Path('.').resolve() / 'data_prep_eng/output_data/mix.tsv'
        for content in mix_file_contents:
            with open(output_path, 'w', encoding='utf-8') as new_file:
                new_file.write(content.strip())
    except:
            print(f'Something happened. We could not write to {file_path}.tsv file')
            
    # after we shuffle the data with our normal seed of 28 to add some randomization
            
   
   
