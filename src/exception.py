import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys)->str:
    """It is used to get the detail error message using sys module for better exception handling

    Args:
        error (error): Basic Type of Error which is Occured
        error_detail (sys): Its a sys module which is used to get the detail error message

    Returns:
        str: It returns the Error in custom formatted string
    """
    _,_,exc_tb= error_detail.exc_info()
    filename=exc_tb.tb_frame.f_code.co_filename
    
    error_message = "\nError occurred in python script name [{0}] line number [{1}]\nError message is [{2}]\n".format(filename,exc_tb.tb_lineno,str(error))
    
    return error_message
    
class CustomException(Exception):
    """
    Custom Exception Class used for custom handling of exceptions.

    Attributes:
        error_message (str): The custom error message.
        error_detail (sys): The sys module used to get the detail error message.

    Methods:
        __init__(error_message, error_detail): Initializes the CustomException class.
        __str__(): Returns the custom error message as a string.

    Raises:
        Exception: The base exception class.
    """
    def __init__(self,error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":
    logging.info("Logging Is Started")
    
    try:
        a=1/0
    except Exception as e:
        logging.error(f"Error Occured: {e}")
        raise CustomException(e,sys)