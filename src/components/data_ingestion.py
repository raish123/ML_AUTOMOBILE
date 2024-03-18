#means reading the data from different source known as data ingestion
import src
import pandas as pd
from src.logger import logging
from src.exception import CustomException
import os,sys


from sklearn.model_selection import train_test_split   #we r getting train_set,test_set
from dataclasses import dataclass

#dataclass is a built in class of dataclasses module  help us directly to
#define the class variable/attributes by using @dataclass  decorato


#after reading the data where we have to save the raw_data 
#or after splitting the data where we have to save train_set/test_set data 
#so we have to mentioned the specific folder to stored the data!!



#creating dataingestionconfig class where all the path are define in these class using dataclasses module!!!

@dataclass
class DataIngestionConfig():
    #defining class variable or class attribute directly using dataclasses module
    train_data_path = os.path.join('artifact','train.csv')
    test_data_path = os.path.join('artifact','test.csv')
    raw_data_path = os.path.join('artifact','raw.csv')



#now creating another class for performing the dataingestion (means reading data from source,
#saving those raw data...then splitting the raw data into train_set and test_set)

class DataIngestion():
    #now all the paths are define DataIngestionConfig class we have to take access in  this class
    #so creating constructor method 
    def __init__(self):
        #here we r calling the DataIngestionConfig class all attibutes storing into instance variable/attributes
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Enter the data ingestion method or component')
        try:
            #here we r reading the raw data from source present in 
            df = pd.read_csv('notebook\cleaned_automobile.csv')  #in industry only we want to take care of this line only line will getting change remaining all same

            logging.info('Csv data successfully readed to df object')

            #now creating artifact folder and storing train_data_path in it
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            #saving the raw data into artifact specific folder
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            #splitting the dataset into 80:20  ratio of train_set and test_set respectively
            logging.info('Train test split of data initiated')
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=1)

            #again saving the train set and test test to artifact folder
            df.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            df.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Data Ingestion is done Successfully!')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                self.ingestion_config.raw_data_path
            )


        except Exception as e:
            raise CustomException(e,sys)
        

#checking the data ingestion file

if __name__ == '__main__':
    obj = DataIngestion()
    obj.initiate_data_ingestion()