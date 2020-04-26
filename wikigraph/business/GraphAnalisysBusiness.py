from wikigraph.business.Neo4JBusiness import Neo4JBusiness
from wikigraph.dao.GraphDao import GraphDao


class GraphBusiness(Neo4JBusiness):
    def __init__(self):
        Neo4JBusiness.__init__(self)
         #  creazione dao
        self.neoDao = GraphDao()

    def getMostRelatedSubGraph(self, represeDict:dict):
        return self.neoDao.findAllCombinations(represeDict)