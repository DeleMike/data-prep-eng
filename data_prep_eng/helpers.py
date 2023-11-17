import unicodedata
import random
import csv

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
    num_words_to_remove = random.randint(1, min(2, len(words)))  # Ensure not to remove more words than available

    # Step 4: Remove the random number of words
    if len(words) > num_words_to_remove:
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
 