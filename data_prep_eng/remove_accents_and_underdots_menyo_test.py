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

def remove_accents_and_underdots():
    """
    Apply all rules to dataset
    """
    absolute_path = Path('.').resolve() / f'data_prep_eng/output_data/test.txt'
    output_path = Path('.').resolve() / f"data_prep_eng/output_data/test_with_no_diacritics.txt"
    
    yoruba_sentences = _extract_yoruba_sentences(absolute_path)
    
    statistics_file_path= Path('.').resolve() / f"data_prep_eng/output_data/test_with_no_diacritics_stats.txt"
    
    # we do this because the dev.tsv file has the first line as English Yoruba
    only_yoruba_sentences = yoruba_sentences[:]
    remove_accents_and_underdots_from_menyo_test(output_path, only_yoruba_sentences, statistics_file_path=statistics_file_path)
    
    
def remove_accents_and_underdots_for_YAD_test():
    """
    Apply all rules to dataset
    """
    absolute_path = Path('.').resolve() / f'data_prep_eng/output_data/test.txt'
    output_path = Path('.').resolve() / f"data_prep_eng/output_data/test_with_no_diacritics.tsv"
    
    yoruba_sentences = _extract_yoruba_sentences(absolute_path)
    
    statistics_file_path= Path('.').resolve() / f"data_prep_eng/output_data/test_with_no_diacritics_tsv_stats.txt"
    
    # we do this because the dev.tsv file has the first line as English Yoruba
    only_yoruba_sentences = yoruba_sentences[:]
    remove_accents_and_underdots_from_menyo_test(output_path, only_yoruba_sentences, statistics_file_path=statistics_file_path)
    
def remove_accents_only_for_YAD_test():
    """
    Apply all rules to dataset
    """
    absolute_path = Path('.').resolve() / f'data_prep_eng/output_data/test.txt'
    output_path = Path('.').resolve() / f"data_prep_eng/output_data/yad_test_with_no_accents_only.tsv"
    
    yoruba_sentences = _extract_yoruba_sentences(absolute_path)
    
    statistics_file_path= Path('.').resolve() / f"data_prep_eng/output_data/yad_test_with_no_accents_only.txt"
    
    # we do this because the dev.tsv file has the first line as English Yoruba
    only_yoruba_sentences = yoruba_sentences[:]
    remove_accents_only_from_menyo_test(output_path, only_yoruba_sentences, statistics_file_path=statistics_file_path)