#Model Training
from src.exception import CustomException
from src.logger import logging
from src.utils import evaluated_model,best_model,save_pkl
from sklearn.linear_model import LinearRegression,Lasso,ElasticNet,Ridge
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from dataclasses import dataclass
import pandas as pd
import os,sys
##Initialing the models trainer config class
@dataclass
class ModelTrainerConfig:
    model_file_path = os.path.join('artifacts','model.pkl')
    
##Implementing the model trainer class
class ModelTrainer:
    def __init__(self):
        self.config=ModelTrainerConfig()
        
    def initiate_model_trainer(self,x_train,x_test,y_train,y_test):
        try:
            logging.info("Initiating the Model Trainer")
            models={
            'LinearRegression':LinearRegression(),
            'Ridge':Ridge(),
            'Lasso':Lasso(),
            'ElasticNet':ElasticNet(),
            'DecisionTreeRegressor':DecisionTreeRegressor(),
            'RandomForestRegressor':RandomForestRegressor(n_estimators=25,criterion="squared_error",max_depth=4,min_samples_split=2),
            # 'SVR':SVR()
            }
            logging.info("Starting the model evaluation")           
            evaluated_models=evaluated_model(models,x_train,x_test,y_train,y_test)
            logging.info("Evaluation of models completed")
            logging.info(evaluated_models)
            # logging.info("\n"+"\n".join([str(i) for i in evaluated_models.items()]))
            logging.info(f"Every model performance=>\n"+"\n".join([str(i) for i in evaluated_models.items()]))
            logging.info("Finding best model using best model function")
            best_model_name,best_model_trained,best_score=best_model(models,evaluated_models)
            print(f'Best Model Name: {best_model_name}')
            print(f'Best Model Score: {best_score}')
            
            logging.info(f"Best Model Name: {best_model_name}")
            logging.info(f"Best Model Score: {best_score}")
            logging.info("Saving the best model")
            save_pkl(obj=best_model_trained,obj_path=self.config.model_file_path)
            logging.info("Model Pickle file is saved")
            print(x_test[:1])
            print(best_model_trained.predict(x_test[:1]))
        except Exception as e:
            logging.error("Error occured during model training: {}".format(e))
            raise CustomException(e,sys)    
        
