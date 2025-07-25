import sys
import traceback
from logger.custom_logger import CustomLogger

logger = CustomLogger().get_logger("Exception_experiment")

class DocumnetPortalException(Exception):
    """ 
    Custom Exception for Documnet Portal
    """
    def __init__(self,error_message:str,error_details:sys):
        _,_,exc_tb = error_details.exc_info() #Provide the compelte exceution detail
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.lineno = exc_tb.tb_lineno
        self.error_message = str(error_message)
        self.traceback_str = ''.join(traceback.format_exception(*error_details.exc_info()))

        
    def __str__(self):
        return f""" 
        Error in [{self.file_name}] at line [{self.lineno}]
        Message : {self.error_message}
        Traceback:{self.traceback_str}
        """
    

if __name__=="__main__":
    try :
        #simulate an error
        a = 1 / 0
        print(a)
    except Exception as e:
        app_exc = DocumnetPortalException(e,sys)
        logger.error(app_exc) #log the Exeption
        raise app_exc    
    

