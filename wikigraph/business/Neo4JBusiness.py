from wikigraph.config.Config import Config
import logging

class Neo4JBusiness:
    def __init__(self):
        self.config = Config()
        logLevel = self.config.getLogLevel()
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(getattr(logging, logLevel))