import os
import pandas as pd
from zipfile import ZipFile
import spacy

def load_to_df(file_name, path):
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
    path =  os.path.join(os.getcwd(), "data")
    # specifying the zip file name
    file_name = os.path.join(path,"commonlitreadabilityprize.zip")

    nlp = spacy.load("en_core_web_sm")
    data_pd = load_to_df(file_name, path)
    
