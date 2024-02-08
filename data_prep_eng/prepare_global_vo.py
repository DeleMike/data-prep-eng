from pathlib import Path
from .helpers import *

import os
import random

"""
We will prepare the global voices data to be our trainin set
"""

def _extract_yoruba_sentences(file_path:str):
    """
    Extract only the Yoruba sentences from the jw300 text
    """
    yoruba_sentences = []

    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        content = file.read()
        yoruba_sentences = content.strip().split('\n') # remove whitespaces, then break per line

    return yoruba_sentences

def create_global_voices_train_dataset():
    """
    """
    absolute_path = Path('.').resolve() / f'data_prep_eng/global_voices/global_voices.txt' 
    output_path = Path('.').resolve() / f'data_prep_eng/output_data/global_voices.tsv'
    statistics_file_path= Path('.').resolve() / f"data_prep_eng/output_data/global_voices_stats.txt"
    
    yoruba_sentences = _extract_yoruba_sentences(absolute_path)
    
    remove_accents_and_underdots_from_global_voices(output_path, yoruba_sentences, statistics_file_path=statistics_file_path)