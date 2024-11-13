import kaggle
import os
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()
api.model_list_cli()

def set_kaggle_file(userInput):
    if userInput != '':    
        dataset = search_kaggle_file(userInput)
        test = download_kaggle_file(dataset)
        return test

def download_kaggle_file(kaggle_files_list):  
    DOWNLOAD_LOCAL = './data' 
    for dataset in kaggle_files_list:
        try:
            kaggle.api.dataset_download_files(
                str(dataset),
                path=DOWNLOAD_LOCAL,
                unzip=True
            )
            print('Download: ', dataset, " | ", dataset.title, " | ", dataset.size)
        except Exception:
            print('Error:    ', dataset, " | ", dataset.title, " | ", dataset.size)
    # Get the name of the file inside the data directory
    downloaded_files = os.listdir(DOWNLOAD_LOCAL)
    return downloaded_files[0]

def search_kaggle_file(search):
    SEARCH = str(search)
    kaggle_list = api.dataset_list(
        search=SEARCH,
        file_type="csv",
        sort_by="published"
    )[0:2]  # Just a test!
    print(kaggle_list)
    return kaggle_list

set_kaggle_file('')