import os
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.logger import logging
import pandas as pd
from src.exception import CustomException
import sys
logging.info('Data ingestion has been started')
@dataclass
class DataIngestiononfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestiononfig()
    def initiate_data_injestion(self):
        logging.info("Enter the injestion method or component")
        try:
            df=pd.read_csv('notebook/Data/processed_data.csv')
            logging.info("read the Dataset ")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train Test split Initiated")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info('Ingestion of data is completed')
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=='__main__':
    obj=DataIngestion()
    obj.initiate_data_injestion()