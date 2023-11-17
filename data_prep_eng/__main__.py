from data_prep_eng.prepare_menyo20k import create_new_menyo_dataset
from data_prep_eng.prepare_bible import combine_all_bible_data, create_new_yoruba_dataset
from data_prep_eng.prepare import combine_data

import random

# Set a fixed seed for reproducibility
seed_value = 28
random.seed(seed_value)

def main():
   # create_new_menyo_dataset()
   # create_new_menyo_dataset(type_of_dataset='test')
   # # test_prepare()
   # combined_yor_file_path = combine_all_bible_data()
   # create_new_yoruba_dataset(combined_file_path=combined_yor_file_path)
   # Usage
   combine_data()
   combine_data(type_of_dataset='test')


if __name__ == "__main__":
    main()