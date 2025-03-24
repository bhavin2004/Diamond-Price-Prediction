#Importing neccessary Libraries
import sys,os
from src.logger import logging
from src.exception import CustomException
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.impute import SimpleImputer #Handling Missing Values
from sklearn.preprocessing import StandardScaler #Used to handle feature scaling
from sklearn.preprocessing import OrdinalEncoder #Used to handle categorical data using Ordinal scaling
from sklearn.model_selection import train_test_split #Used to split the dataset into training and testing sets
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from src.utils import *

## Initializing the Data Transformation Config class
@dataclass
class DataTransformationConfig:
    preprocessor_pkl_path=os.path.join('artifacts','preprocessor.pkl')
    processed_train_file_path: str = os.path.join('artifacts','processed_train_data.csv')
    processed_test_file_path: str = os.path.join('artifacts','processed_test_data.csv')
    
    
    
## Class for Data Transformation
class DataTransformation:
    def __init__(self):
        self.config=DataTransformationConfig()
    
    def create_prepocessor(self,x:pd.DataFrame):
        try:
            logging.info("create_preprocessor method is initiated")
            
            #Segregating numerical and categorical features
            categorical_columns = x.select_dtypes(include='object').columns #here ordinal encoding will be used
            numerical_columns = x.select_dtypes(exclude='object').columns #here standard scaling will be used
            
            # Define the custom rankings for ordinal encoding
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            cut_categories = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
            clarity_categories = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']
            
            logging.info("Pipeline is initiated")
            ##Numerical pipeline Building
            ##The numerical pipeline building is a process of creating a series of numerical operations that can be executed in automation
            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy='median')),
                    ("scaler",StandardScaler()),
                ]
            )
            ##Categorical pipeline Building
            ##The categorical pipeline building is a process of creating a series of categorical operations that can be executed in automation
            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy='most_frequent')),
                    ('Ordinal Encoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                    ('StandardScaler',StandardScaler())
                ]
            )

            logging.info('Pipeline are created for both numerical and categorical fetures')
            logging.info("Creating the Preprocessor object")
            
            preprocessor=ColumnTransformer([
                ('numerical',numerical_pipeline,numerical_columns),
                ('categorical',categorical_pipeline,categorical_columns)
            ]) 
            
            ##Returning the preprocessor obj
            return preprocessor           
            
        except Exception as e:
            logging.error("Error occured in data transformation in creating preprocessor object : {0}".format(str(e)))
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            logging.info("Data Transformation is initiated")
            
            train_data=pd.read_csv(train_path)
            test_data=pd.read_csv(test_path)
            
            # train_data.drop(columns=['x','y','z','id'],inplace=True)
            logging.info("Read the Train and test data are loaded")
            logging.info(f"Train Dataframe Head =>\n{train_data.head().to_string()}")
            logging.info(f"Test Dataframe Head =>\n{test_data.head().to_string()}")
            

            traget_col='price'
            drop_cols=[traget_col,'id','x','y','z']
            
            #Segregating the independent features and dependent features
            x_train=train_data.drop(columns=drop_cols,axis=1)
            x_test=test_data.drop(columns=drop_cols,axis=1)
            
            y_train=train_data[traget_col]
            y_test=test_data[traget_col]
            
            logging.info('Obtaining preprocessing object')
            preprocessor=self.create_prepocessor(x_train)
            logging.info('Obtainined preprocessing object')
            
            logging.info("Applying Data transformation with prepoccessor obj")
            x_train=pd.DataFrame(preprocessor.fit_transform(x_train),columns=preprocessor.get_feature_names_out())
            x_test=pd.DataFrame(preprocessor.transform(x_test),columns=preprocessor.get_feature_names_out())
            
            logging.info("Read the Train and test Transformed data")
            logging.info(f"Train Dataframe Head =>\n{x_train.head().to_string()}")
            logging.info(f"Test Dataframe Head =>\n{x_test.head().to_string()}")
            
            # logging.info()
            save_pkl(obj=preprocessor,obj_path=self.config.preprocessor_pkl_path)
            
            logging.info("Preprocessor object is saved")
            train_df=x_train.copy()
            train_df[traget_col]=y_train
            train_df.to_csv(self.config.processed_train_file_path,index=False)
            test_df=x_test.copy()
            test_df[traget_col]=y_test
            test_df.to_csv(self.config.processed_test_file_path,index=False)
            
            return (
                 x_train,
                 y_train,
                 x_test,y_test,
                self.config.preprocessor_pkl_path
                )
            
            
        except Exception as e:
            logging.error("Error occured in data transformation in inititaing the data transformation : {0}".format(str(e)))
            raise CustomException(e,sys)