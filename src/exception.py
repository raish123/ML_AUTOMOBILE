#in these file we r creating custom exception that help to findout error and raise the message 
#and those error are getting logged into  log files.

import sys   #sys module have all the error details present in it during runtime environment
from src.logger import logging

def get_error_message(error,error_detail:sys):
    """This function will take an error object  as input parameter and return its description"""

    _,_,exc_tb = error_detail.exc_info() #rtn 3 parameter in tuple formate (type,value,traceback)
    filename  = exc_tb.tb_frame.f_code.co_filename #get the error_name of current file 
    lineno = exc_tb.tb_lineno                     #get line number where this error occur

    #now representing the way to show case error_message
    error_message  = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        filename, exc_tb.tb_lineno, str(error)
    )
    return error_message


#creating custom exception class will inherit all property from pareant class Exception built in class of python
class CustomException(Exception):
    #creating  a constructor method for our own Exception class
    def __init__(self,error_message,error_detail:sys):
        #calling parent class constructor to get the error message information
        super().__init__(error_message)

        #whaterver error message we r getting from parent class exception we r passing parameter to the function
        self.error_message = get_error_message(error_message,error_detail=error_detail)  #calling the user defined function


    #error_message we r getting from function displaying by using __str__ special method 
    def __str__(self):
        return self.error_message




# if __name__ == '__main__':
#     try:
#         a=1/0

#     except Exception as e:
#         #these error we have to logged into  log file so we use logging module here
#         logging.info(e)
#         raise CustomException(e,sys)