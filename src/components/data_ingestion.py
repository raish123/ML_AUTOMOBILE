#In data ingestion we perform 3 Action in it 
#1)data ingestion meaning reading the data from different source(can be database or cloud service)
#2)splitting the data into 80:20 ratio(splitting code we can write into utils file also if required)
#3) storing those (train_set and test_set and raw_set)data into specific folder(artifact)

#importing all the important libraries which is used during data ingestion!!!
import pandas as pd #this library we used to read the dataset
from sklearn.model_selection import train_test_split #these library we used  for splitting the data into train and test set.
import os,sys #os module we used to create directory or path where as 
#sys module will have all details of error in it these will help me to decode the error in logs file
#importing exception and logger modules in these file
from src.logger import logging
from src.exception import CustomException
import numpy as np
from dataclasses import dataclass 
#dataclass is a built in class of dataclasses module we used to 
#initialize directly class variable/attributes path and folder of file!!


#1)first creating class for storing (train_set and test_set and raw_set)data into specific folder(artifact)
@dataclass  #this line indicate these class variable 
class DataIngestionConfig():
    #initializing the train,test,raw data path
    train_data_path = os.path.join('artifacts','train.csv')
    test_data_path = os.path.join('artifacts','test.csv')
    raw_data_path = os.path.join('artifacts','raw.csv')



#2)data ingestion meaning reading the data from different source(local machine orcan be database or cloud service)
#so creating class for reading the data and  splitting the data into 80:20 ratio and storing the data into 
#DataIngestionConfig initialize path
    
class DataIngestion():
    #creating constructor method/object of DataIngestion class will have all details of the initialize data_path in it
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() 
        #self.ingestion_config is class variable which hold test,train,raw_data_path detail in it

    #now we will create method  for reading the data from csv file  and storing the data into specific folder
    def initiate_data_ingestion(self):
        logging.info('Data Ingestion initiated Started')
        try:
            #reading the data from csv file
            df = pd.read_csv('notebook\Automobile_data.csv')
            logging.info('Data Read successfully in DataFrame object')

            #now creating artifact folder 
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) 
            logging.info('artifact Folder Successfully Created')

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            #splitting the dataset into train and test set with 80:20 ratio
            train_df,test_df = train_test_split(df,test_size=0.2,random_state=42)

            logging.info('saving train and test_df into artifact folder by using self.ingestion_config train&test')
            #storing the train and test set into respective files
            train_df.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_df.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Data Ingestion is done Successfully!')

            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )


        except Exception as e:
            raise CustomException(e,sys)

if __name__ == '__main__':
    di = DataIngestion()
    di.initiate_data_ingestion()
    


