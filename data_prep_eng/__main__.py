from data_prep_eng.prepare_menyo20k import create_new_menyo_dataset
from data_prep_eng.prepare_bible import combine_all_bible_data

def main():
   create_new_menyo_dataset()
   create_new_menyo_dataset(type_of_dataset='test')
   # test_prepare()
   combine_all_bible_data()

if __name__ == "__main__":
    main()