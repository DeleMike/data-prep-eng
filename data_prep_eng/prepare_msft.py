from pathlib import Path
from .helpers import *

import os
import random

"""
We will prepare the msft data
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

def prepare_msft_data():
    """
    """
    absolute_path = Path('.').resolve() / f'data_prep_eng/msft/newstest2019-ref.yor.txt'
    
    output_path_1 = Path('.').resolve() / f'data_prep_eng/output_data/newstest2019_ref_no_diacritics.tsv'
    statistics_file_path_1 = Path('.').resolve() / f"data_prep_eng/output_data/newstest2019_ref_no_diacritics_stats.txt"
    
    output_path_2 = Path('.').resolve() / f'data_prep_eng/output_data/newstest2019_ref_no_accents_only.tsv'
    statistics_file_path_2 = Path('.').resolve() / f"data_prep_eng/output_data/newstest2019_ref_no_accents_only_stats.txt"
    
    yoruba_sentences = _extract_yoruba_sentences(absolute_path)

    print('Yoruba sentences length : ', len(yoruba_sentences))
    
    process_and_save_msft_data_with_no_diacritics(output_path_1, yoruba_sentences, statistics_file_path=statistics_file_path_1)
    process_and_save_msft_data_with_no_accents_only(output_path_2, yoruba_sentences, statistics_file_path=statistics_file_path_2)
    