from src.logger import logging

import pandas as pd

file_path="notebook/data/processed_data.csv"
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        data['text']=data['subject']+" "+data["message"]
        data=data[["label","text"]]
        logging.info("data ingestion is done")
        return data
    except Exception as e:
        logging.info("Error loading data: {e}")
        return None



