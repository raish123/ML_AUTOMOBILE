#these file we will used to write the code and provide the functionality in comman way to used by the application
#generally we will used this file to read the data from database or to push the model to aws or azure service

import os,sys
import numpy as np,pandas as pd
import dill
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)