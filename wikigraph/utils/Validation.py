
import logging
from six import string_types
from wikigraph.config.Config import Config


class Validator:
    '''
    superclass
    '''
    def __init__(self):
        logLevel = Config().getLogLevel()
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(getattr(logging, logLevel))
        
    def exec_validation(self, toValidate):
        raise NotImplementedError("Subclasses should implement this!")


class StringValidator(Validator):

    def __init__(self):
        Validator.__init__(self)

    def exec_validation(self, toValidate:str):
        """
        validate if var is a string
        @param toValidate: string
        @return:  bool
        """
        return isinstance(toValidate, string_types)
 
 
class ListValidator(Validator):

    def __init__(self):
        Validator.__init__(self)

    def exec_validation(self, toValidate:list):
        """
        validate if var is a list
        @param toValidate: list
        @return:  bool
        """    
        return isinstance(toValidate, list)
