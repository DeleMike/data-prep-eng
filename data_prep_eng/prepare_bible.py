import os

from pathlib import Path

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

