from pathlib import Path
from .helpers import *

def _extract_yoruba_sentences(file_path:str):
    """
    Extract only the Yoruba sentences from the jw300 text
    """
    yoruba_sentences = []

    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        content = file.read()
        yoruba_sentences = content.strip().split('\n') # remove whitespaces, then break per line

    return yoruba_sentences

def create_jw300_train_dataset():
    """Process JW300 data and produce our dataset
    """
    absolute_path = Path('.').resolve() / f'data_prep_eng/jw300/jw300.yo' 
    output_path = Path('.').resolve() / f'data_prep_eng/output_data/jw300.tsv'
    statistics_file_path= Path('.').resolve() / f"data_prep_eng/output_data/jw300_stats.txt"
    
    yoruba_sentences = _extract_yoruba_sentences(absolute_path)
    
    process_and_save_jw300_data(output_path, yoruba_sentences, statistics_file_path=statistics_file_path)