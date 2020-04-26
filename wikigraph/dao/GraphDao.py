from wikigraph.dao.Neo4JDao import Neo4JDao
from collections import deque
from operator import itemgetter
import itertools


class GraphDao(Neo4JDao):

    def __init__(self):
        Neo4JDao.__init__(self)

    def findShortestPaths(self, combo: list):
        """
        find shortest path between a list of nodes
        @:param combo: list
        @:return: dict
        """
        dict_shortest_path = {"entities_list": list(), 1: 0, 2: 0, 3: 0}
        with self.neoClient.session() as session:
            result = self.queryForShortestPath(session, combo)
            dict_shortest_path['entities_list'] = combo

        for elem in result:
            dict_shortest_path[elem[0]] = elem[1]

        self.log.debug("Entities list: {el}".format(el=dict_shortest_path))
        return dict_shortest_path


    def queryForShortestPath(tx: object, entities_list: list):
        """
        query for shortest path against neo4j
        @:param tx: object
        @:param entities_list: list
        @:return result: generator
        """
        result = tx.run("MATCH (n:Record) where n.title IN $entities_list "
                        "WITH collect(n) as nodes "
                        "UNWIND nodes as n "
                        "UNWIND nodes as m WITH * "
                        "WHERE id(n) < id(m) "
                        "MATCH path = allShortestPaths( (n)-[:HAS_LINK*..3]-(m) ) "
                        "RETURN length(path), count(*) ", entities_list=entities_list)
        return result

    def findAllCombinations(self, represeDict: dict):
        """
        get a set of set of all possible combination
        of entities, for each set is applied a convertion to list
        and query against Neo4j for shortest path between multiple nodes
        @:param represeDict: dict
        @:return ordinato: list
        """
        list_of_entities = []
        set_of_combination = set()
        list_of_result = []
        for key in represeDict.keys():
            if represeDict[key]:
                list_of_entities.append(represeDict[key])
        self.log.info("preparing to process possible results {le} .....".format(le=list_of_entities[:4]))
        for elem in deque(itertools.product(*list_of_entities)):
            elem = frozenset(elem)
            set_of_combination.add(elem)
        self.log.info("Find {comb} possible combination".format(comb=len(set_of_combination)))
        conteggio = 0
        for combo in set_of_combination:
            list_of_result.append(self.findShortestPaths(list(combo)))
            conteggio += 1
            self.log.info(
                "Processed {part} combination of {tot} total".format(part=conteggio, tot=len(set_of_combination)))

        list_of_result = sorted(list_of_result, key=itemgetter(1, 2, 3), reverse=True)
        return list_of_result
