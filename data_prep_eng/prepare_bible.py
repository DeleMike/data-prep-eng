from pathlib import Path
from .helpers import *

import os

def _create_combined_file_path(base_folder, data_folder, file_name):
    # Define the paths
    base_path = Path(base_folder).resolve()
    combined_path_folders = [
        base_path / 'data_prep_eng' / 'output_data',
        base_path / 'data_prep_eng' / 'output_data' / data_folder
    ]

    # Create output folders if they don't exist
    for folder in combined_path_folders:
        if not folder.exists():
            folder.mkdir()

    # Construct the final combined file path
    combined_file_path = combined_path_folders[-1] / file_name

    return combined_file_path

def combine_all_bible_data():
    """
    Combine all data from the Yoruba dataset [data_prep_eng/bibeli_mimo_yoruba_NIV]
    """
    # Step 1: Read all the contents in [data_prep_eng/bibeli_mimo_yoruba_NIV]
    # Specify the path to the directory
    directory_path = "/mnt/disk/makindele/data_prep_eng/data_prep_eng/bibeli_mimo_yoruba_NIV"

    # Get the list of folders in the directory
    folder_names = [folder for folder in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, folder))]

    # /mnt/disk/makindele/data_prep_eng/data_prep_eng/bibeli_mimo_yoruba_NIV/1KI.5.BMY/1KI.5.1.txt
    # Initialize an empty list to store file paths
    file_paths = []

    # Iterate through all files in the directory and its subdirectories
    for foldername, subfolders, filenames in os.walk(directory_path):
        # print(f'Foldername = {foldername}, subfolder = {subfolders}, filenames = {filenames}')
        for filename in filenames:
            # Construct the full path to the file
            file_path = os.path.join(foldername, filename)
            # Append the file path to the list
            file_paths.append(file_path)

    # Specify the path for the combined file
    base_folder = '.'
    data_folder = 'yoruba_bible_data'
    file_name = 'yoruba_bible_combined.txt'
    combined_file_path = _create_combined_file_path(base_folder, data_folder, file_name)

    # Open the combined file in write mode
    with open(combined_file_path, 'w', encoding='utf-8') as combined_file:
        # Iterate through each file path
        for file_path in file_paths:
            # Read the contents of the file
            with open(file_path, 'r', encoding='utf-8') as current_file:
                file_contents = current_file.read()
                # Write the contents to the combined file
                combined_file.write(file_contents + '\n')  # Add a newline between each file

    print("Combination completed. Output file:", combined_file_path)
    return combined_file_path

def create_new_yoruba_dataset(combined_file_path):
    """
    Apply the case rules to the Yoruba dataset and save the processed output.
    """
    # open the combined file path and read the contents
    yoruba_sentences = []
    with open(combined_file_path, 'r', encoding='utf-8') as file:
        txt_reader = csv.reader(file)

        for row in txt_reader:
            yoruba_sentences.append(row[0])

    # print(f'Yoruba sentences = {yoruba_sentences[:20]}')

    if(len(yoruba_sentences) != 0):
        # process it using those four rules
        statistics_file_path =  Path('.').resolve() / f"data_prep_eng/output_data/yoruba_bible_data/processed_yoruba_bible.txt"
        process_and_save_yoruba_data(yoruba_sentences, statistics_file_path=statistics_file_path)
        
def create_no_accents_and_no_underdots_yoruba_dataset(combined_file_path):
    """
    Apply the case rule, remove accents and underdots to the Yoruba dataset and save the processed output.
    """
    # open the combined file path and read the contents
    yoruba_sentences = []
    with open(combined_file_path, 'r', encoding='utf-8') as file:
        txt_reader = csv.reader(file)

        for row in txt_reader:
            yoruba_sentences.append(row[0])

    # print(f'Yoruba sentences = {yoruba_sentences[:20]}')

    if(len(yoruba_sentences) != 0):
        # process it using those four rules
        statistics_file_path =  Path('.').resolve() / f"data_prep_eng/output_data/yoruba_bible_data/no_accents_and_underdots_yoruba_bible.txt"
        remove_only_accents_and_underdots_on_yoruba_data(yoruba_sentences, statistics_file_path=statistics_file_path)
        
def split_bible_combined_data():
    """90% for train, 10% for test"""
    # divide file by 90%
    # then test file to have 10% of contents
    file_path = '/mnt/disk/makindele/data_prep_eng/data_prep_eng/output_data/yoruba_bible_data/yoruba_bible_combined.txt'
    
    # Read the contents of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.readlines()
    
    # Shuffle the data randomly
    random.shuffle(data)
    
    print(f'Length of file = {len(data)}')
    # Calculate the index to split the data
    split_index = int(0.9 * len(data))
    
    # Split the data into training and testing sets
    train_data = data[:split_index]
    test_data = data[split_index:]
    
    print(f'Length of train is = {len(train_data)}')
    print(f'Length of train is = {len(test_data)}')
    
    
    # Write the training data to a new file
    with open('data_prep_eng/output_data/yoruba_bible_data/unprocessed_yoruba_bible_train.txt', 'w', encoding='utf-8') as train_file:
        train_file.writelines(train_data)
    
    # # Write the testing data to a new file
    # with open('data_prep_eng/output_data/yoruba_bible_data/yoruba_bible_test.txt', 'w', encoding='utf-8') as test_file:
    #     test_file.writelines(test_data)
        
        
    # for each of the contents in the 
    statistics_file_path =  Path('.').resolve() / f"data_prep_eng/output_data/yoruba_bible_data/yor_bible_train_stats.txt"
    yoruba_sentences = []
    with open('data_prep_eng/output_data/yoruba_bible_data/unprocessed_yoruba_bible_train.txt', 'r', encoding='utf-8') as file:
        txt_reader = csv.reader(file)

        for row in txt_reader:
            yoruba_sentences.append(row[0])
            
    
    print(yoruba_sentences[0:3])
    
    process_and_save_yoruba_data_v2(yoruba_sentences, statistics_file_path=statistics_file_path)
    
    
    #  # for each of the contents in the 
    # statistics_file_path_2 =  Path('.').resolve() / f"data_prep_eng/output_data/yoruba_bible_data/yor_bible_test_stats.txt"
    # output_file_path =  Path('.').resolve() / f"data_prep_eng/output_data/yoruba_bible_data/yoruba_bible_test_on_accents.tsv"
    
    # yoruba_sentences_2 = []
    # with open('data_prep_eng/output_data/yoruba_bible_data/yoruba_bible_test.txt', 'r', encoding='utf-8') as file:
    #     txt_reader = csv.reader(file)

    #     for row in txt_reader:
    #         yoruba_sentences_2.append(row[0])
            
    
    # print(yoruba_sentences_2[0:3])
    
    # remove_accents_only_from_bible(output_path=output_file_path, yoruba_sentences=yoruba_sentences_2, statistics_file_path=statistics_file_path_2)
    
    # remove_accents_and_underdots_from_bible(output_path=output_file_path, yoruba_sentences=yoruba_sentences_2, statistics_file_path=statistics_file_path_2)
