def data_preprocessing():
    print("something happened")
    import os
    from sklearn.model_selection import train_test_split
    from dataclasses import dataclass
    import pandas as pd
    from src.logger import logging
    from src.exception import CustomException
    import sys


    logging.info('Data ingestion has been started')

    @dataclass
    class DataIngestionConfig:
        train_data_path: str = os.path.join('artifacts', 'train.csv')
        test_data_path: str = os.path.join('artifacts', 'test.csv')
        raw_data_path: str = os.path.join('artifacts', 'data.csv')

    class DataIngestion:
        def __init__(self):
            self.ingestion_config = DataIngestionConfig()
        
        def initiate_data_ingestion(self):
            logging.info("Entering the ingestion method/component")
            try:
                # Read the dataset
                df = pd.read_csv('notebook/Data/processed_data.csv')
                logging.info("Dataset read successfully")

                # Ensure the directory for saving the files exists
                os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

                # Save the raw data
                df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
                logging.info("Raw data saved successfully")

                # Split the dataset into train and test sets
                logging.info("Initiating train-test split")
                train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
                
                # Save the train and test sets
                train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
                test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
                
                logging.info('Data ingestion completed successfully')
                
                return (
                    self.ingestion_config.train_data_path, 
                    self.ingestion_config.test_data_path
                )
            
            except FileNotFoundError as e:
                logging.error(f"File not found: {e}")
                raise CustomException(f"File not found: {e}", sys)
            except pd.errors.EmptyDataError as e:
                logging.error(f"Empty data: {e}")
                raise CustomException(f"Empty data: {e}", sys)
            except Exception as e:
                logging.error(f"An error occurred: {e}")
                raise CustomException(e, sys)

    if __name__ == "__main__":
        try:
            obj = DataIngestion()
            train_data, test_data = obj.initiate_data_ingestion()

        
            # Continue with model training and evaluation using `train_arr` and `test_arr`

        except CustomException as e:
            logging.error(f"Custom exception: {e}")
        except Exception as e:
            logging.error(f"Unhandled exception: {e}")



