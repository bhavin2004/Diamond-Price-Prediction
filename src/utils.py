import pickle
import os,sys
from src.logger import logging
from src.exception import CustomException
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.linear_model import LinearRegression,Lasso,ElasticNet,Ridge
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR

def save_pkl(obj,obj_path):
    try:
        folder_dir=os.path.dirname(obj_path)
        os.makedirs(folder_dir,exist_ok=True)
        logging.info(f"Initiating the Saving of Pickle file {obj_path}")
        with open(obj_path,'wb') as f:
            pickle.dump(obj,f)
    except Exception as e:
            logging.error("Error occured in saving the {} pkl file: {}".format(obj_path,str(e)))
            raise CustomException(e,sys)
        
        
def evaluated_model(models:dict,x_train,x_test,y_train,y_test):
    try:
        model_score=dict()
        for model_name,model in models.items():
            model.fit(x_train,y_train)
            y_pred=model.predict(x_test)
            score=calculate_model_score(y_test,y_pred)
            model_score[model_name]=score
        return model_score
    except Exception as e:
        logging.error("Error occured during evaluation all models: {}".format(e))
        raise CustomException(e,sys)
    
import numpy as np
def calculate_model_score(true,predicated):
    # Calculate the mean squared error
    mse = mean_squared_error(true,predicated)
    # Calculate the mean absolute error
    mae = mean_absolute_error(true,predicated)
    # Calculate the root mean squared error
    rmse = float(np.sqrt(mse))
    # Calculate the r2 score
    r2 = r2_score(true,predicated)
    return {
        'MSE':mse,
        "MAE":mae,
        'RMSE':rmse,
        'R2_score':r2}
    
    
def best_model(models:dict,evaluated_models:dict):
    try:
        score_type='R2_score'
        max_score=0
        for i in range(len(list(models.values()))):
            model_scores=list(evaluated_models.values())[i]
            score=model_scores[score_type]
            if score>max_score:
                best_model_name=list(evaluated_models.keys())[i]
                max_score=score
                best_model=list(models.values())[i]
        return best_model_name,best_model,max_score
    except Exception as e:
        logging.error("Error occured during calculating the best model score: {}".format(e))
        raise CustomException(e,sys)
    
    
def load_pkl(pkl_path):
    try:
        with open(pkl_path,'rb') as file:
            return pickle.load(file)
    except Exception as e:
        logging.error("Error occured during loading the pkl file: {}".format(e))
        raise CustomException(e,sys)