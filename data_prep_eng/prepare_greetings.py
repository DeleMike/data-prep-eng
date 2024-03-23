from pathlib import Path
from .helpers import *

import os
import random

"""
We will prepare the greetings data
"""

def _extract_yoruba_sentences(file_path:str):
    """
    Extract only the Yoruba sentences from the jw300 text
    """
    yoruba_sentences = []

    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        lines = file.readlines()
        for line in lines:
            yoruba_text = line.split('\t')[0].strip()  # Extract Yoruba text before the tab delimiter
            yoruba_sentences.append(yoruba_text)

    return yoruba_sentences

def create_greetings_test_dataset():
    """
    """
    absolute_path = Path('.').resolve() / f'data_prep_eng/greetings/greeting_test.tsv' 
    output_path = Path('.').resolve() / f'data_prep_eng/output_data/greeting_test_output.tsv'
    statistics_file_path= Path('.').resolve() / f"data_prep_eng/output_data/greeting_test_output_stats.txt"
    
    yoruba_sentences = _extract_yoruba_sentences(absolute_path)
    # print('Yoruba sentences are : ', yoruba_sentences[1:])
    
    remove_accents_and_underdots_from_greetings(output_path, yoruba_sentences[1:], statistics_file_path=statistics_file_path)
    
def create_merge_yoruba_greetings():
    """
    """
    absolute_path_1 = Path('.').resolve() / f'data_prep_eng/greetings/greet_dev.tsv' 
    absolute_path_2 = Path('.').resolve() / f'data_prep_eng/greetings/greet_train.tsv' 
    output_path = Path('.').resolve() / f'data_prep_eng/output_data/greeting_merge.tsv'
    
    yoruba_sentences = _extract_yoruba_sentences(absolute_path_1)
    yoruba_sentences_2 = _extract_yoruba_sentences(absolute_path_2)
    merged_yoruba_sentences = []
   
    merged_yoruba_sentences.extend(yoruba_sentences[1:])
    merged_yoruba_sentences.extend(yoruba_sentences_2[1:])
    
    print('Yoruba sentences are : ', merged_yoruba_sentences)
    print('Yoruba sentences length : ', len(merged_yoruba_sentences))
    
    with open(output_path, 'w', encoding='utf-8', newline='') as output_file:
        tsv_writer = csv.writer(output_file, delimiter='\t')
        tsv_writer.writerow(['Yoruba'])
        for sentence in merged_yoruba_sentences:
            tsv_writer.writerow([sentence])
            

def prepare_merge_greetings():
    """
    """
    absolute_path = Path('.').resolve() / f'data_prep_eng/output_data/greeting_merge.tsv'
    output_path = Path('.').resolve() / f'data_prep_eng/output_data/greeting_merge_processed.tsv'
    statistics_file_path= Path('.').resolve() / f"data_prep_eng/output_data/greeting_merge_processed_stats.txt"
    
    yoruba_sentences = _extract_yoruba_sentences(absolute_path)[1:]

    print('Yoruba sentences length : ', len(yoruba_sentences))
    
    process_and_save_greetings_merge_data(output_path, yoruba_sentences, statistics_file_path=statistics_file_path)
 
def create_greetings_test_dataset_no_accent():
    """
    """
    absolute_path = Path('.').resolve() / f'data_prep_eng/greetings/greeting_test.tsv' 
    output_path = Path('.').resolve() / f'data_prep_eng/output_data/greeting_test_output_no_accents_only.tsv'
    statistics_file_path= Path('.').resolve() / f"data_prep_eng/output_data/greeting_test_output_no_accents_only_stats.txt"
    
    yoruba_sentences = _extract_yoruba_sentences(absolute_path)
    # print('Yoruba sentences are : ', yoruba_sentences[1:])
    
    remove_only_accents_from_greetings(output_path, yoruba_sentences[1:], statistics_file_path=statistics_file_path)