from data_prep_eng.prepare_menyo20k import create_new_menyo_dataset, split_test_data
from data_prep_eng.prepare_bible import combine_all_bible_data, create_new_yoruba_dataset, create_no_accents_and_no_underdots_yoruba_dataset
from data_prep_eng.prepare import combine_data

import random

# Set a fixed seed for reproducibility


def main():
   
   seed_value = 28
   random.seed(seed_value)
   
   # split_test_data()
   create_new_menyo_dataset() # create dev menyo dataset based on our 4 rules
   create_new_menyo_dataset(type_of_dataset='test') # create train menyo dataset based on our 4 rules

   # # test_prepare()
   
   combined_yor_file_path = combine_all_bible_data() # combine yor bible texts into one file
   create_new_yoruba_dataset(combined_file_path=combined_yor_file_path) # create yoruba dataset based on our 4 rules
   
   # process yoruba bible by removing only all accents and underdots
   create_no_accents_and_no_underdots_yoruba_dataset(combined_file_path=combined_yor_file_path)
   
   # combine_data() # create dev dataset based on our 4 rules
   # combine_data(type_of_dataset='test') # create test dataset based on our 4 rules

if __name__ == "__main__":
    main()