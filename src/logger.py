#during runtime execution of programme if any exception occur in try block or error occur if we want to track down 
#those error and stored into specific folder into text format then we have to used logging module

#importing all the important module used in  this program.
import os,logging
from datetime import datetime


#now creating the object of basicConfig class of logging module
#which having all information about the errors or exception

#creating a folder where all log file get stored in it
dir_name = 'LOGS'
if not os.path.exists(dir_name):                   #check if directory
    os.makedirs(dir_name,exist_ok=True)

log_file = f"Logs-{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

filepath = os.path.join(dir_name,log_file)    

logging.basicConfig(filename = filepath,
                    level = logging.INFO,
                    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
)


#now checking log file will getting stored into logs folder or not

#if __name__ == '__main__':
#    logging.info('THIS IS THE INFO LEVEL ERROR EXIST IN FILE')