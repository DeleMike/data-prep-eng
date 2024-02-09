import json

from pathlib import Path

def extract_labels_to_text_file(type_of_dataset='test'):
    """
    This will extract the data 'dcyo' from test.json or dev.json
    If it does not exist, then we will not extract labels
    """
    file_path = Path('..').resolve() / f"data_prep_eng/output_data/{type_of_dataset}.json"
    file_content = ''

    try:
        with open(file_path, 'r', encoding='utf-8') as file:

            # Read the content of the file
            content = file.read()
            lines = content.strip().split('\n') # remove whitespaces, then break per line

            for line in lines[:]:
                json_data = json.loads(line) # parse it to a json format
                file_content += json_data['translation']['dcyo'] + '\n'
            
    except FileNotFoundError:
        print(f'{type_of_dataset} does not exist. Ensure your {type_of_dataset} exist before running this.')

    try:
        new_path =  file_path = Path('..').resolve() / f"data_prep_eng/output_data/{type_of_dataset}.txt"
        with open(new_path, 'w', encoding='utf-8') as new_file:
            new_file.write(file_content.strip())
    except:
        print(f'Something happened. We could not write to {type_of_dataset}.txt file')
  
  
""" The following lines below were used to generate the text files that n will be used during the bleu score calculation
We have to use .txt files. Hence, for each dev file we wish to perfrom the Sacrebleu calculation on, just do the following:
Your file must be a json file. Simply just pass it pass the  name of the file `file_to_convert` and you will get a generated file 
as `file_to_extract.txt`
""" 
# extract_labels_to_text_file()
# extract_labels_to_text_file(type_of_dataset='dev')
# extract_labels_to_text_file(type_of_dataset='menyo_train')
# extract_labels_to_text_file(type_of_dataset='dev_with_no_accents')
# extract_labels_to_text_file(type_of_dataset='dev_with_no_accents_and_underdots')
extract_labels_to_text_file(type_of_dataset='global_voices')



