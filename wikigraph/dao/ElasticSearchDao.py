from wikigraph.config.Config import Config
import logging

class ElasticSearchDao:
    '''
    superclass
    '''
    def __init__(self, indexName:str, esClient:object):
        self.indexName = indexName
        self.esClient = esClient

        logLevel = Config().getLogLevel()
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(getattr(logging, logLevel))