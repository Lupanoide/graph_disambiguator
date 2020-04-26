
from elasticsearch import Elasticsearch
from neo4j import GraphDatabase
import codecs
import logging
import configparser
import os



class Config(object):
    '''
    Classe di utils per il file config
    '''
    def __init__(self):
        #name = os.path.abspath( os.path.join( __file__ , r"../../config/properties.ini"))
        name = os.path.abspath( os.path.join( __file__ , r"../../config/properties.ini.tmp"))
        self.config = configparser.ConfigParser()
        self.config._interpolation = configparser.ExtendedInterpolation()
        self.config.read(name)

        FORMAT = "%(asctime)s %(levelname)s %(name)s.%(funcName)s() - %(message)s"
        logging.basicConfig(format=FORMAT, filename=self.config.get("default", "log_file"), level=logging.DEBUG)

    def getLogLevel(self):
        return self.config.get("default", "log_level")

    def getIndexWikipedia(self):
        return self.config.get("elasticsearch" , "indexname")

    def getEsClient(self):
        clusterES = self.config.get("elasticsearch", "cluster").split("||")
        esClient = Elasticsearch(clusterES, maxsize=25, timeout=30, max_retries=10, retry_on_timeout=True)
        return esClient

    def getStopWords(self):
        stopWordFile = self.config.get("wordList", "stopword")
        stopWords = set()
        with codecs.open(stopWordFile, "r", encoding="utf-8") as f:
            for line in f.readlines():
                stop = line.strip()
                stopWords.add(stop.lower())
        return stopWords

    def getNeoClient(self):
        url = self.config.get("neo4j", "server")
        driver = GraphDatabase.driver(encrypted=False, uri="bolt://{url}".format(url=url))
        return driver

if __name__ == '__main__':

    c=Config()
    print(c.getEsConnector())
    print(c.getLemmatizedWords())