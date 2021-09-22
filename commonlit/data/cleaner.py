
import os
import os
import pandas as pd
from zipfile import ZipFile
import spacy
nlp = spacy.load("en_core_web_sm")
# from data_loader import load_to_df

class Cleaner:
    def __init__(self, filename, path):
        self.filename = filename
        self.path = path
    

    def unzip_folder(self):
        # opening the zip file in READ mode
        with ZipFile(self.filename, 'r') as zip:
            # printing all the contents of the zip file
            zip.printdir()

            # extracting all the files
            print('Extracting all the files now...')
            zip.extractall(self.path)
            print('Done!')

    def load_to_df(self):
        data_path = os.path.join(self.path,'train.csv')
        data = pd.read_csv(data_path, usecols=['id','excerpt','target','standard_error'],  index_col = 'id')
        return data

    

    def clean_data(self):
        self.unzip_folder()
        df = self.load_to_df()
        print(df.head())

    

    
    

if __name__=='__main__':
    path =  os.path.join(os.getcwd(), "data")
    # specifying the zip file name
    filename = os.path.join(path,"commonlitreadabilityprize.zip")
    cleaned = Cleaner(filename, path).clean_data()