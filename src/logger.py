import logging
import os
from datetime import datetime

<<<<<<< HEAD
FILE_PATH = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log'
log_filepath = os.path.join(os.getcwd(),"logs",FILE_PATH)
os.makedirs(log_filepath,exist_ok=True)

Log_File = os.path.join(log_filepath,FILE_PATH)


logging.basicConfig(filename=Log_File,level=logging.INFO,format="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]")
=======
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(module)s - %(message)s",
    level=logging.INFO
)
>>>>>>> 03dd003 (first commit)
