<<<<<<< HEAD
import os
import sys
from src.logger import logging


def error_message_details(error,error_details:sys):

    _,_,exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename

    error_message =  "Error occure in python script name [{0}] line number [{1}] error message [{2}]".format(filename,exc_tb.tb_lineno,str(error))
=======
import sys
from src.logger import logging

def get_error_message(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename

    error_message  = "Error occure in python script name {} line number {} error message {}".format(filename,exc_tb.tb_lineno,error)
>>>>>>> 03dd003 (first commit)

    return error_message

class CustomeException(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
<<<<<<< HEAD
        self.error_message = error_message_details(error_message,error_details=error_details)
        
    def __str__(self):
        return self.error_message
=======
        self.error_message = get_error_message(error_message,error_details=error_details)

    def __str__(self):
        return self.error_message
>>>>>>> 03dd003 (first commit)
