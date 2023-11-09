import unicodedata

def remove_accents_but_not_dots(input_text):
    # Step 1: Decompose input_text into base letters and combinining characters
    decomposed_text = unicodedata.normalize('NFD', input_text)

    # Step 2: Filter out the combining characters we don't want
    filtered_text = ''
    for c in decomposed_text:
        if ord(c) <= 0x7f or c == '\N{COMBINING DOT BELOW}':
            # Only keep ASCII or "COMBINING DOT BELOW"
            filtered_text += c

    # Step 3: Re-compose the string into precomposed characters
    return unicodedata.normalize('NFC', filtered_text)

print(remove_accents_but_not_dots('ọkàn'))

# import unicodedata

# def remove_under_dots(input_str):
#     # Normalize the string to decomposed form (NFD)
#     normalized_str = unicodedata.normalize('NFD', input_str)
    
#     # Filter out characters that are not combining diacritical marks
#     result_str = ''.join(char for char in normalized_str if unicodedata.category(char) != 'Mn')
    
#     return result_str

# # Example usage:
# original_str = "kožušček"
# modified_str = remove_under_dots(original_str)

# print(modified_str)

# # print('Àlàmú ti wá ń gbádùn àdáwà, dídáwà yìí ń fún un ní àǹfààní láti rán ọkàn rẹ̀ níṣẹ́.')