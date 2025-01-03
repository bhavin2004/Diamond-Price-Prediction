import os,sys
from src.exception import CustomException
from src.logger import logging
from src.utils import load_pkl
from sklearn.linear_model import LinearRegression,Lasso,ElasticNet,Ridge
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from dataclasses import dataclass
import pandas as pd
import os,sys


#Creating a config class for Prediction pipeline
@dataclass
class Config:
    preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
    model_path=os.path.join('artifacts','model.pkl')
    
#Defining class for Prediction Pipeline
class PridictionPipeline:
    def __init__(self):
        self.config=Config()
    
    def load_data(self):
        try:
            logging.info("Loading pickle files")
            self.preprocessor=load_pkl(self.config.preprocessor_path)
            self.model=load_pkl(self.config.model_path)
            logging.info("Successfully loaded pkl files")
        except Exception as e:
            logging.error("Error occured in Prediction Pipeline due to loadind pkl files : {}".format(e))
            raise CustomException(e,sys)
        
    def predict(self,input_data:pd.DataFrame):
        try:
            logging.info("Predict method is initiated")
            self.load_data()
            input_data=self.preprocessor.transform(input_data)
            # input_data=pd.DataFrame(self.preprocessor.transform(input_data),columns=self.preprocessor.get_feature_names_out())
            prediction=self.model.predict(input_data)
            logging.info("Prediction is done")
            return prediction
        except Exception as e:
            logging.error("Error occured in Prediction Pipeline due to prediction : {}".format(e))
            raise CustomException(e,sys)
        
class InputConverter:
    def __init__(self,carat,depth,table,cut,color,clarity):
        self.carat=carat
        self.depth=depth
        self.table=table
        self.cut=cut
        self.color=color
        self.clarity=clarity
    
    def convert_to_Datafram(self):
        try:
            #Converting the input data into a dataframe
            input_dict={
                'carat':self.carat,
                'depth':self.depth,
                'table':self.table,
                'cut':self.cut,
                'color':self.color,
                'clarity':self.clarity
            }
            df = pd.DataFrame(input_dict,index=[0])
            print(df)
            logging.info("Successfully Converted")
            return df
        except Exception as e:
            logging.error("Error occured in InputConverter due to converting to dataframe : {}".format(e))
            raise CustomException(e,sys)
if __name__=='__main__':
    obj=InputConverter(0.5,62.1,57.0,'Ideal','D','SI1')
    prediction_obj=PridictionPipeline()
    res=prediction_obj.predict(obj.convert_to_Datafram())    
    print(str(res)+'$')