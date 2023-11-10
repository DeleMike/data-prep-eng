from pathlib import Path

import unicodedata
import random
import csv

def prepare():
    """
    For a data domain, apply these cases:
    (i) Remove accents and underdots
    (ii) Remove accents only. Leave the underdots
    Prepare data for case (i) and (ii).
    """
    text = 'Àlàmú ti wá ń gbádùn àdáwà, dídáwà yìí ń fún un ní àǹfààní láti rán ọkàn rẹ̀ níṣẹ́.'
    # we want 60% of the text to apply rule (i) and 40% apply rule (ii)
    print(_remove_accents_and_underdots(text))
    print(_remove_only_accents(text))

    # print('/mnt/disk/makindele/data_prep_eng/data_prep_eng/data/dev_book.tsv')
    absolute_path = Path('.').resolve() / "data_prep_eng/data/dev_book.tsv"
    print(f'Absolute Path = {absolute_path}')

    # read file
    # with open(str(absolute_path), 'r') as html_file:
    #     content = html_file.read()

    # print(content)



def extract_yoruba_sentences(file_path):
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

def _remove_accents_and_underdots(text):
    """
    We will remove all accents and underdots from the text
    """
    # Normalize the string to decomposed form (NFD)
    normalized_str = unicodedata.normalize('NFD', text)
    
    # Filter out characters that are not combining diacritical marks
    result_str = ''.join(char for char in normalized_str if unicodedata.category(char) != 'Mn')
    
    return result_str

def _remove_only_accents(text):
    """
    We will remove all accents only. So underdots will still appear in text
    """
    # Step 1: Decompose input_text into base letters and combinining characters
    decomposed_text = unicodedata.normalize('NFD', text)

    # Step 2: Filter out the combining characters we don't want
    filtered_text = ''
    for c in decomposed_text:
        if ord(c) <= 0x7f or c == '\N{COMBINING DOT BELOW}':
            # Only keep ASCII or "COMBINING DOT BELOW"
            filtered_text += c

    # Step 3: Re-compose the string into precomposed characters
    return unicodedata.normalize('NFC', filtered_text)

def apply_mixed_removal(sentence):
    # Determine whether to apply _remove_accents_and_underdots or _remove_only_accents
    if random.random() < 0.6:  # 60% chance for _remove_accents_and_underdots
        return _remove_accents_and_underdots(sentence), 'accents_and_underdots'
    else:  # 40% chance for _remove_only_accents
        return _remove_only_accents(sentence), 'only_accents'

def train():
    # Set a fixed seed for reproducibility
    seed_value = 30
    random.seed(seed_value)

    absolute_path = Path('.').resolve() / "data_prep_eng/data/dev_book.tsv"
    output_path_folder = Path('.').resolve() / "data_prep_eng/data/prep_data"
    if(not output_path_folder.exists()): output_path_folder.mkdir()
    output_path= Path('.').resolve() / "data_prep_eng/data/prep_data/yor_dev_book.tsv"


    print(f'Absolute Path = {absolute_path}')
    yoruba_sentences = extract_yoruba_sentences(absolute_path)
    # Counters for verification
    counters = {'total_sentences': 0, 'accents_and_underdots': 0, 'only_accents': 0}

    with open(output_path, 'w', encoding='utf-8', newline='') as output_file:
        tsv_writer = csv.writer(output_file, delimiter='\t')
        tsv_writer.writerow(['Original Sentence', 'Modified Sentence', 'Case Rule Applied'])

        for sentence in yoruba_sentences:
            modified_sentence, removal_type = apply_mixed_removal(sentence)
            counters['total_sentences'] += 1
            counters[removal_type] += 1
            tsv_writer.writerow([sentence, modified_sentence, removal_type])

    # Calculate percentages
    counters['accents_and_underdots_percentage'] = (counters['accents_and_underdots'] / counters['total_sentences']) * 100
    counters['only_accents_percentage'] = (counters['only_accents'] / counters['total_sentences']) * 100

    # Print the counters
    print("\nCounters:")
    for key, value in counters.items():
        print(f"{key}: {value}")

    print(f"\nOutput file created at: {output_path}")

    # Output file path for statistics
    statistics_file_path= Path('.').resolve() / "data_prep_eng/data/prep_data/yor_dev_book_stats.txt"

    # Write counters to the statistics file
    with open(statistics_file_path, 'w', encoding='utf-8') as statistics_file:
        statistics_file.write("Counters:\n")
        for key, value in counters.items():
            statistics_file.write(f"{key}: {value}\n")

    print(f"\nStatistics file created at: {statistics_file_path}")