from wikigraph.config.Config import Config
import logging

class Neo4JDao():
    '''
    superclass
    '''
    def __init__(self):
        logLevel = Config().getLogLevel()
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(getattr(logging, logLevel))
        self.neoClient = Config().getNeoClient()
