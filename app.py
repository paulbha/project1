from src.project1.logger import logging
from src.project1.exception import CustomException
from src.project1.components.data_ingestion import DataIngestion
import sys
import pandas as pd

if __name__=="__main__":
    logging.info("The execution has started")

    try:
        # 1. Initialize and run ingestion
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        
        # 2. Read the created file to show the output in terminal
        # This matches the visual output from the tutorial video
        df = pd.read_csv(train_data_path)
        
        print("\n" + "="*50)
        print("DATABASE EXTRACTION SUCCESSFUL")
        print("="*50)
        print(df.head())  # This displays the table you saw in the screenshot
        print("="*50 + "\n")

    except Exception as e:
        logging.info("Custom Exception occurred")
        raise CustomException(e, sys)