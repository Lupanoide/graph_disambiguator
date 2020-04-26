from wikigraph.dao.ElasticSearchDao import ElasticSearchDao
from wikigraph.model.ElasticSearch.WikiResult import WikiResult
import re


class WikiDao(ElasticSearchDao):

    def __init__(self, indexName: str, esClient: object):
        ElasticSearchDao.__init__(self, indexName, esClient)
        self.express_regul = r"^{exp}(\s\(.*?\)|$)"

    def raffinateCandidates(self, word: str, set_candidates: set, redirect_candidate: set):
        """
        examinate candidates and give final response
        @:param word: string
        @:param set_candidates: set
        @:param redirect_candidate: set
        @:return candidatiFinali: set
        """
        candidatiFinali = self.checkThatFormat(word, set_candidates)
        if redirect_candidate:
            candidatiFinali = candidatiFinali.union([word for word in redirect_candidate if "disambigua" not in word])
        return candidatiFinali

    def checkThatFormat(self, word: str, set_candidates: set):
        """
        apply a regex to filter candidates
        @:param word: string
        @:param set_candidates: set
        @:return: insieme_risultati: set
        """
        insieme_risultati = set()
        pattern = re.compile(self.express_regul.format(exp=word.lower()))
        for can in set_candidates:
            result = pattern.match(can.lower())
            if result:
                if "disambigua" in can.lower():
                    continue
                else:
                    insieme_risultati.add(can)
        return insieme_risultati

    def checkRedirectFormat(self, word: str, candidate: str):
        """
        apply a regex on redirect
        @:param word: str
        @:param candidate: str
        @:return boole: boolean
        """
        boole = False
        pattern = re.compile(self.express_regul.format(exp=word.lower()))
        result = pattern.match(candidate.lower())
        if result:
            boole = True
        return boole

    def createQueryToGetEntities(self, word: str):
        """
        build a requests body to query against ES
        @:param word: string
        @:return body: dict
        """
        body = {
            "size": 5000,
            "query": {
                "bool": {
                    "should": [
                        {
                            "match_phrase": {
                                "redirect.title": {
                                    "query": word.lower(),
                                    "boost": 500000
                                }
                            }
                        },
                        {
                            "match_phrase": {
                                "title": word.lower()
                            }
                        }
                    ]
                }
            }
        }
        return body

    def createBulkFixSingleWord(self, word: str):
        """
        prepare mget query for bulk syntax
        @:param word: string
        @:return mgetL: list
        """
        mgetL = []
        mgetL.append({})
        mgetL.append(self.createQueryToGetEntities(word))
        return mgetL

    def bulkSearchOnES(self, body, list_of_words: list):
        """
        query an array of words against ES
        @:param body: list
        @:param list_of_words: list
        @:return maxi_dict: dict
        """
        redirect_candidate = set()
        set_candidates = set()
        maxi_dict = dict()
        responso = self.esClient.msearch(index=self.indexName, body=body)
        for count in range(len(responso['responses'])):
            for res in responso['responses'][count]['hits']['hits']:
                self.log.debug("bulk search query: {w}, result: {rs}".format(w=list_of_words[count], rs=res))
                esObject = WikiResult(res['_source'])
                title = esObject.get_title()
                set_candidates.add(title)
                redirectL = esObject.get_redirects()

                for redirect in redirectL:
                    if self.checkRedirectFormat(list_of_words[count], redirect):
                        redirect_candidate.add(title)

            set_elected_candidates = self.raffinateCandidates(list_of_words[count], set_candidates, redirect_candidate)

            maxi_dict[list_of_words[count]] = []
            maxi_dict[list_of_words[count]].extend(list(set_elected_candidates))
            redirect_candidate = set()
            set_candidates = set()

        return maxi_dict
