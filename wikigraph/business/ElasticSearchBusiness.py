import logging
from wikigraph.utils.Validation import StringValidator, ListValidator
from wikigraph.config.Config import Config


class ElasticSearchBusiness:

    def __init__(self):
        self.config = Config()
        logLevel = self.config.getLogLevel()
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(getattr(logging, logLevel))

        # creazione validatori
        self.stringValidator = StringValidator()
        self.stopWords = self.config.getStopWords()
        self.listValidator = ListValidator()