#Import neccessary libraries
import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


## initialize the Data Ingestion Configuration so that it can be used in the entire application and if any changes are made to the configuration, it will be reflected in the entire application

@dataclass
class DataIngestionConfig:
    """This class contains configuration related to data ingestion"""
    
    #The train file path we have the path to the train data for the model#
    train_file_path: str = os.path.join('artifacts','train_data.csv')
    
    #The test file path we have the path to the test data for the model#
    test_file_path: str = os.path.join('artifacts','test_data.csv')
    
    #The raw file path we have the path to the raw data for the model#
    raw_file_path: str = os.path.join('artifacts','raw_data.csv')
    
    #Original file path we have the path to the original data for the model#
    original_file_path: str = os.path.join('notebooks/data','gemstone.csv')
    
class DataIngestion:
    """This class is used for data ingestion"""
    
    ##Initialize the object with data ingestion config  
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    
    ##Initaiting the data ingestion process
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion is started")
        
        
        #Make try except block to handle the error in data ingestion process
        try:
            #Read the data from the file
            df = pd.read_csv(self.ingestion_config.original_file_path)
            logging.info("Dataset from data folder is loaded as pandas Dataframe") 
            
            #Confirming that the raw data is folder exist
            os.makedirs(os.path.dirname(self.ingestion_config.raw_file_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_file_path,index=False,header=True)
            
            logging.info("Performing Train Test split on the dataset")
            
            train_set,test_set=train_test_split(df,test_size=.20,random_state=42)
            
            #save the train data to the file
            train_set.to_csv(self.ingestion_config.train_file_path,index=False,header=True)
            
            #save the test data to the file
            test_set.to_csv(self.ingestion_config.test_file_path,index=False,header=True)
            
            
            logging.info("Data Ingestion of the Dataset is completed")
            
            return (
                self.ingestion_config.train_file_path,
                self.ingestion_config.test_file_path,
            )
            
        except Exception as e:
            #Raise the custom exception
            logging.error("Error occured during data ingestion : {}".format)
            raise CustomException(e,sys)
