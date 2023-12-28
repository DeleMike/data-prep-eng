from pathlib import Path
from .helpers import *

import unicodedata
import random
import csv

def _swap_distinct_words(word_list):
    # Get distinct words in the list
    distinct_words = list(set(word_list))

    # Check if there are at least two distinct words
    if len(distinct_words) < 2:
        return word_list  # No need to swap if there are not enough distinct words

    # Randomly select two distinct words to swap
    word1, word2 = random.sample(distinct_words, 2)

    # Swap the positions of the two selected distinct words
    index1 = word_list.index(word1)
    index2 = word_list.index(word2)
    word_list[index1], word_list[index2] = word_list[index2], word_list[index1]

    return word_list

def test_prepare():
    """
    For a data domain, apply these cases:
    (i) Remove accents and underdots
    (ii) Remove accents only. Leave the underdots
    Prepare data for case (i) and (ii).
    """
    # text = 'Àlàmú ti wá ń gbádùn àdáwà, dídáwà yìí ń fún un ní àǹfààní láti rán ọkàn rẹ̀ níṣẹ́.'
    # we want 60% of the text to apply rule (i) and 40% apply rule (ii)
    # print(_remove_accents_and_underdots(text))
    # print(_remove_only_accents(text))
    # print(_remove_only_accents_and_any_random_word(text))

    # english_text = "ha ha ha, I am going to the market... ha ha ha"
    # print(_remove_only_accents_and_swap_word(english_text))

    # print('/mnt/disk/makindele/data_prep_eng/data_prep_eng/menyo20k_data/dev_book.tsv')
    # absolute_path = Path('.').resolve() / "data_prep_eng/menyo20k_data/dev_book.tsv"
    # print(f'Absolute Path = {absolute_path}')

    # read file
    # with open(str(absolute_path), 'r') as html_file:
    #     content = html_file.read()

    # print(content)

    # Example usage:
    word_list1 = ['ha', 'ha', 'ha', 'I', 'am', 'good!', 'ha', 'ha', 'ha']
    result1 = _swap_distinct_words(word_list1)
    print(result1)

    word_list2 = ['hello']
    result2 = _swap_distinct_words(word_list2)
    print(result2)

    word_list3 = ['hello', 'hello', 'hello']
    result3 = _swap_distinct_words(word_list3)
    print(result3)

def _extract_yoruba_sentences(file_path:str):
    """
    Extract only the Yoruba sentences from the text
    """
    yoruba_sentences = []

    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        tsv_reader = csv.reader(file, delimiter='\t')

        # Assuming Yoruba sentences are in the second column (index 1)
        for row in tsv_reader:
            if len(row) >= 2:
                yoruba_sentence = row[1].strip()
                # print(yoruba_sentence)
                yoruba_sentences.append(yoruba_sentence)

    return yoruba_sentences

def _create_output_folders(base_folder, type_of_dataset, domain):
    # Define the paths
    base_path = Path(base_folder).resolve()
    data_path = base_path / 'data_prep_eng'
    output_path_folders = [
        data_path / 'output_data',
        data_path / 'output_data' / 'menyo20k_data',
        data_path / 'output_data' / 'menyo20k_data' / f'{type_of_dataset}_prep_data'
    ]

    # Create output folders if they don't exist
    for folder in output_path_folders:
        if not folder.exists():
            folder.mkdir()

    # Construct the final output path
    output_path = output_path_folders[-1] / f'yor_{type_of_dataset}_{domain}.tsv'
    absolute_path = data_path / f'menyo20k_data/new_dev_test_files/{type_of_dataset}_{domain}.tsv'

    return output_path, absolute_path

def _create_new_development_file_folders(base_folder, type_of_dataset, domain):
    # Define the paths
    base_path = Path(base_folder).resolve()
    data_path = base_path / 'data_prep_eng'
    output_path_folders = [
        data_path / 'output_data',
        data_path / 'menyo20k_data' / 'new_dev_test_files' ,
    ]

    # Create output folders if they don't exist
    for folder in output_path_folders:
        if not folder.exists():
            folder.mkdir()

    # Construct the final output path
    output_path = output_path_folders[-1]
    absolute_path = data_path / f'menyo20k_data/{type_of_dataset}_{domain}.tsv'

    return output_path, absolute_path

def create_new_menyo_dataset(type_of_dataset='dev'):
    """
    Apply all rules to dataset
    """
    for domain in domains:
       # Define the paths
        output_path, absolute_path = _create_output_folders(
            base_folder='.',
            type_of_dataset=type_of_dataset,
            domain=domain
        )
        
        print(f'Absolute Path = {absolute_path}')
        yoruba_sentences = _extract_yoruba_sentences(absolute_path)
        statistics_file_path= Path('.').resolve() / f"data_prep_eng/output_data/menyo20k_data/{type_of_dataset}_prep_data/yor_{type_of_dataset}_{domain}_stats.txt"
        process_and_save_menyo_data(output_path, yoruba_sentences, statistics_file_path=statistics_file_path)

def create_menyo_train_dataset():
    """Process Menyo20k data and produce our dataset
    """
    absolute_path = Path('.').resolve() / f'data_prep_eng/menyo20k_data/train.tsv'
    output_path = Path('.').resolve() / f"data_prep_eng/output_data/train.tsv"
    
    yoruba_sentences = _extract_yoruba_sentences(absolute_path)
    
    statistics_file_path= Path('.').resolve() / f"data_prep_eng/output_data/train_stats.txt"
    
    # we do this because the train.tsv file has the first line as English Yoruba
    only_yoruba_sentences = yoruba_sentences[1:]
    process_and_save_menyo_data(output_path, only_yoruba_sentences, statistics_file_path=statistics_file_path)

def split_test_data(type_of_dataset='test'):
    for domain in domains:
        # Construct the final output path
        output_path, absolute_path = _create_new_development_file_folders(
            base_folder='.',
            type_of_dataset=type_of_dataset,
            domain=domain
        )

        print(f'Output = ${output_path}')
        print(f'Absolute Path = {absolute_path}')
    
        # Read the data from the absolute path
        with open(absolute_path, 'r') as file:
            lines = file.readlines()

        # Calculate the split index to divide the data into equal halves
        split_index = len(lines) // 2

        # Split the lines into test and dev sets
        dev_lines, test_lines = lines[:split_index], lines[split_index:]

        # Save the test and dev data to the output paths
        test_output_path = output_path.parent / 'new_dev_test_files' / f'test_{domain}.tsv'
        dev_output_path = output_path.parent / 'new_dev_test_files' / f'dev_{domain}.tsv'

        with open(test_output_path, 'w') as test_file:
            test_file.writelines(test_lines)

        with open(dev_output_path, 'w') as dev_file:
            dev_file.writelines(dev_lines)

        print(f"Split data for domain {domain}. Test data saved to {test_output_path}, Dev data saved to {dev_output_path}")