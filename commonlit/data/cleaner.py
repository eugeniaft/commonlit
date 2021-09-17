
import os
import os
import pandas as pd
from zipfile import ZipFile
import spacy
nlp = spacy.load("en_core_web_sm")
# from data_loader import load_to_df

class Cleaner:
    def __init__(self, file_name, path):
        self.filename = file_name
        self.path = path
    

    # def load_to_df(self):
    #     # print('Calling function load_to_df')
    #     # opening the zip file in READ mode
    #     with ZipFile(self.filename, 'r') as zip:
    #         # printing all the contents of the zip file
    #         zip.printdir()

    #         # extracting all the files
    #         print('Extracting all the files now...')
    #         zip.extractall(path)
    #         print('Done!')

    def clean_data(self):
        print('cleaned_data called...')
        # self.load_to_df()

    # data_path = os.path.join(path,'train.csv')
    # data = pd.read_csv(data_path, usecols=['id','excerpt','target','standard_error'],  index_col = 'id')
    # return data

    
    

if __name__=='main':
    path =  os.path.join(os.getcwd(), "data")
    # specifying the zip file name
    file_name = os.path.join(path,"commonlitreadabilityprize.zip")

    cleaned = Cleaner(file_name, path).clean_data()