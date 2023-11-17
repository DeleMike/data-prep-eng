from data_prep_eng.prepare import create_new_dataset

def main():
   create_new_dataset()
   create_new_dataset(type_of_dataset='test')
   # test_prepare()

if __name__ == "__main__":
    main()