from data_prep_eng.prepare_menyo20k import create_new_menyo_dataset, create_menyo_train_dataset_without_processing ,split_test_data, create_menyo_train_dataset, create_menyo_train_with_no_accents_only, create_menyo_train_with_no_accents_and_underdots,create_menyo_dev_with_no_accents_only,create_menyo_dev_with_no_accents_and_underdots
from data_prep_eng.prepare_jw300  import create_jw300_train_dataset
from data_prep_eng.prepare_mix  import prepare_mix_train_data
from data_prep_eng.prepare_global_vo  import create_global_voices_train_dataset,create_global_voices_only_accents_dataset
from data_prep_eng.prepare_greetings  import create_greetings_test_dataset, create_greetings_test_dataset_no_accent


from data_prep_eng.prepare_bible import split_bible_combined_data, combine_all_bible_data, create_new_yoruba_dataset, create_no_accents_and_no_underdots_yoruba_dataset
from data_prep_eng.prepare import combine_data
from data_prep_eng.remove_accents_and_underdots_menyo_test import remove_accents_and_underdots, remove_accents_and_underdots_for_YAD_test, remove_accents_only_for_YAD_test

import random

# Set a fixed seed for reproducibility


def main():

    seed_value = 28
    random.seed(seed_value)

    # split_test_data()
    # create_new_menyo_dataset() # create dev menyo dataset based on our 4 rules
    # create_new_menyo_dataset(type_of_dataset='test') # create train menyo dataset based on our 4 rules

    # # test_prepare()

    # combined_yor_file_path = combine_all_bible_data() # combine yor bible texts into one file
    # create_new_yoruba_dataset(combined_file_path=combined_yor_file_path) # create yoruba dataset based on our 4 rules

    # process yoruba bible by removing only all accents and underdots
    # create_no_accents_and_no_underdots_yoruba_dataset(combined_file_path=combined_yor_file_path)

    # combine_data() # create dev dataset based on our 4 rules
    # combine_data(type_of_dataset='test') # create test dataset based on our 4 rules

    # prepare menyo 20k data
    # create_menyo_train_dataset()
    
    # create_menyo_train_dataset_without_processing()
    
    
    # prepare JW300 data
    # create_jw300_train_dataset()
    
    # prepare mix
    # prepare_mix_train_data()
    
    # prepare menyo train and dev without accents but leave underdots
    # create_menyo_train_with_no_accents_only()
    # create_menyo_dev_with_no_accents_only()
    
    # prepare menyo train and dev without accents and underdots
    # create_menyo_train_with_no_accents_and_underdots()
    # create_menyo_dev_with_no_accents_and_underdots()
    
    # create_global_voices_train_dataset()
    # create_global_voices_only_accents_dataset()
    # remove_accents_and_underdots()
    
    split_bible_combined_data()
    
    # remove_accents_and_underdots_for_YAD_test()
    # remove_accents_only_for_YAD_test()
    
    
    # create_greetings_test_dataset()
    # create_greetings_test_dataset_no_accent()


if __name__ == "__main__":
    main()
