import os
import pandas as pd
from zipfile import ZipFile
import spacy
nlp = spacy.load("en_core_web_sm")

def load_to_df(file_name, path):
    print('Calling function load_to_df')
    # opening the zip file in READ mode
    with ZipFile(file_name, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()

        # extracting all the files
        print('Extracting all the files now...')
        zip.extractall(path)
        print('Done!')

    data_path = os.path.join(path,'train.csv')
    data = pd.read_csv(data_path, usecols=['id','excerpt','target','standard_error'],  index_col = 'id')
    return data

if __name__ == "__main__":
    pass