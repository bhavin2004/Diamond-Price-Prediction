#Import neccessary libraries
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
if __name__=='__main__':
   obj = DataIngestion()
   train_set,test_set=obj.initiate_data_ingestion()
   print(train_set,test_set)
   data_transformation_obj=DataTransformation()
   x_train,y_train,x_test,y_test,preprocessor=data_transformation_obj.initiate_data_transformation(train_set,test_set)
   model_trainer_obj=ModelTrainer()
   model_trainer_obj.initiate_model_trainer(x_train,x_test,y_train,y_test)
   