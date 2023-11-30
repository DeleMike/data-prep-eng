import unicodedata
import random
import csv

domains = ['book', 'digital', 'news', 'proverbs', 'tedTalks']

def remove_accents_and_underdots(text:str):
    """
    We will remove all accents and underdots from the text
    """
    # Normalize the string to decomposed form (NFD)
    normalized_str = unicodedata.normalize('NFD', text)
    
    # Filter out characters that are not combining diacritical marks
    result_str = ''.join(char for char in normalized_str if unicodedata.category(char) != 'Mn')
    
    return result_str

def remove_only_accents(text:str):
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

def remove_only_accents_and_any_random_word(text:str):
    """
    We will do the same as _remove_only_accents but here we will also remove some random words from the text
    """
    # Step 1: Remove accents
    decomposed_text = remove_only_accents(text)

    #  Step 2: Tokenize the text into words
    words = decomposed_text.split()

    # Step 3: Determine the number of words to remove (between 1 and 2)
    num_words_to_remove = min(2, len(words))  # Ensure not to remove more words than available

    # Step 4: Remove the random number of words
    if num_words_to_remove < len(words):
        for _ in range(num_words_to_remove):
            random_index = random.randint(0, len(words) - 1)
            del words[random_index]

    # Step 5: Re-compose the string into precomposed characters
    result_text = ' '.join(words)
    return unicodedata.normalize('NFC', result_text)

def remove_only_accents_and_swap_word(text: str):
    """
    Remove accent and swap two distinct words

    We will do the same as _remove_only_accents but here we will swap a word position
    For example, if we have, in English "ha ha I am going to the market!", 
    a possible result we want to achieve is "ha ha I going am to the market!"
    If say, the first word that was randomly selected was "ha" and the next word that was randomly
    selected was also "ha", then we will have to pick another distinct word to swap with.
    We are only swapping one-word positions. 
    In cases where the words are identical, we ensure they are distinct.  
    """

    # Step 1: Remove accents
    decomposed_text = remove_only_accents(text)

    # Step 2: Tokenize the text into words
    words = decomposed_text.split()

    # Step 3: Make the words DISTINCT
    distinct_words = list(set(words))

    # Check if there are at least two distinct words
    if len(distinct_words) < 2:
        # If not, return the original list without performing the swap
        # Sometimes we might already have it settled
        return unicodedata.normalize('NFC', decomposed_text)

    # Randomly select two distinct words to swap
    word1, word2 = random.sample(distinct_words, 2)

    # Swap the positions of the two selected distinct words
    index1 = words.index(word1)
    index2 = words.index(word2)

    # Swap the positions of the two selected distinct words
    words[index1], words[index2] = words[index2], words[index1]

    # Step 4: Re-compose the string into precomposed characters
    result_text = ' '.join(words)
    return unicodedata.normalize('NFC', result_text)

def apply_mixed_removal(sentence):
    """Determine which case to apply

    This line uses random.choices to randomly select one of the three cases: 
    'remove_accents_and_underdots', 'remove_only_accents', or 'remove_only_accents_and_any_random_word',
    'remove_only_accents_and_swap_word'. 
    The weights [0.6, 0.2, 0.1, 0.1] determine the probability of each case being selected. 
    In this case, 'accents_and_underdots' has a 60% chance, 
    'only_accents' has a 20% chance, and 'only_accents_and_any_random_word' has a 10% chance.
    'remove_only_accents_and_swap_word' also has a 10% chance
    """
    case = random.choices([
        'remove_accents_and_underdots', 
        'remove_only_accents', 
        'remove_only_accents_and_any_random_word',
        'remove_only_accents_and_swap_word'], weights=[0.6, 0.2, 0.1, 0.1])[0]


    if case == 'remove_accents_and_underdots':
        return remove_accents_and_underdots(sentence), case
    elif case == 'remove_only_accents':
        return remove_only_accents(sentence), case
    elif case == 'remove_only_accents_and_any_random_word':
        return remove_only_accents_and_any_random_word(sentence), case
    elif case == 'remove_only_accents_and_swap_word':
        return remove_only_accents_and_swap_word(sentence), case

import csv
from pathlib import Path


def process_and_save_menyo_data(output_path, yoruba_sentences, statistics_file_path):
     # Counters for verification
    counters = {
        'total_sentences': 0, 
        'remove_accents_and_underdots': 0,
        'remove_only_accents': 0,
        'remove_only_accents_and_any_random_word': 0,
        'remove_only_accents_and_swap_word': 0
    }

    # Define the output path
    with open(output_path, 'w', encoding='utf-8', newline='') as output_file:
        tsv_writer = csv.writer(output_file, delimiter='\t')
        tsv_writer.writerow(['Original Sentence', 'Modified Sentence', 'Case Rule Applied'])
        for sentence in yoruba_sentences:
            modified_sentence, removal_type = apply_mixed_removal(sentence)
            counters['total_sentences'] += 1
            counters[removal_type] += 1
            tsv_writer.writerow([sentence, modified_sentence, removal_type])
    
    # Calculate percentages
    counters['accents_and_underdots_percentage'] = (counters['remove_accents_and_underdots'] / counters['total_sentences']) * 100
    counters['only_accents_percentage'] = (counters['remove_only_accents'] / counters['total_sentences']) * 100
    counters['only_accents_and_any_random_word_percentage'] = (counters['remove_only_accents_and_any_random_word'] / counters['total_sentences']) * 100
    counters['only_accents_and_swap_word_word_percentage'] = (counters['remove_only_accents_and_swap_word'] / counters['total_sentences']) * 100
    
    # Print the counters
    print("\nCounters:")
    for key, value in counters.items():
        print(f"{key}: {value}")
    print(f"\nOutput file created at: {output_path}")
    # Output file path for statistics
    
    # Write counters to the statistics file
    with open(statistics_file_path, 'w', encoding='utf-8') as statistics_file:
        statistics_file.write("Counters:\n")
        for key, value in counters.items():
            statistics_file.write(f"{key}: {value}\n")
    print(f"\nStatistics file created at: {statistics_file_path}")


def process_and_save_yoruba_data(yoruba_sentences, statistics_file_path):
    """
    Process the Yoruba dataset, save the modified sentences along with statistics.
    """
    # Counters for verification
    counters = {
        'total_sentences': 0, 
        'remove_accents_and_underdots': 0,
        'remove_only_accents': 0,
        'remove_only_accents_and_any_random_word': 0,
        'remove_only_accents_and_swap_word': 0
    }

    # Define the output path
    output_path = Path('.').resolve() / f"data_prep_eng/output_data/yoruba_bible_data/processed_yoruba_bible.tsv"
    # output_path = Path('.').resolve() / f"data_prep_eng/output_data/train.tsv"


    with open(output_path, 'w', encoding='utf-8', newline='') as output_file:
        tsv_writer = csv.writer(output_file, delimiter='\t')
        tsv_writer.writerow(['Original Sentence', 'Modified Sentence', 'Case Rule Applied', 'Source of Data'])

        for sentence in yoruba_sentences:
            # print(f'Setence = {sentence}')
            modified_sentence, removal_type = apply_mixed_removal(sentence)
            counters['total_sentences'] += 1
            counters[removal_type] += 1
            tsv_writer.writerow([sentence, modified_sentence, removal_type, 'bible'])

    # Calculate percentages
    counters['accents_and_underdots_percentage'] = (counters['remove_accents_and_underdots'] / counters['total_sentences']) * 100
    counters['only_accents_percentage'] = (counters['remove_only_accents'] / counters['total_sentences']) * 100
    counters['only_accents_and_any_random_word_percentage'] = (counters['remove_only_accents_and_any_random_word'] / counters['total_sentences']) * 100
    counters['only_accents_and_swap_word_word_percentage'] = (counters['remove_only_accents_and_swap_word'] / counters['total_sentences']) * 100

    # Print the counters
    print("\nCounters:")
    for key, value in counters.items():
        print(f"{key}: {value}")

    print(f"\nOutput file created at: {output_path}")

    # Output file path for statistics
    # Write counters to the user-provided statistics file
    with open(statistics_file_path, 'w', encoding='utf-8') as statistics_file:
        statistics_file.write("Counters:\n")
        for key, value in counters.items():
            statistics_file.write(f"{key}: {value}\n")

    print(f"\nStatistics file created at: {statistics_file_path}")

# # Usage
# yoruba_sentences = get_yoruba_sentences()  # Replace with your method to get Yoruba sentences
# user_statistics_file_path = input("Enter the statistics file path: ")
# process_and_save_yoruba_data(yoruba_sentences, user_statistics_file_path)

 