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


class Training_Pipeline():
   def __init__(self):
      self.data_ingestion=DataIngestion()
      self.data_transform=DataTransformation()
      self.model_trainer=ModelTrainer()
      
   def run_pipeline(self):
      train_path,test_path=self.data_ingestion.initiate_data_ingestion()
      train_data,tets_data=self.data_transform.initiate_data_transformation(train_path,test_path)
      self.model_trainer.initiate_model_trainer(train_data,tets_data)
      
      
   