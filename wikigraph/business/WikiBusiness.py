from wikigraph.business.ElasticSearchBusiness import ElasticSearchBusiness
from wikigraph.dao.WikiDao import WikiDao
from wikigraph.utils.Exception import WikipediaGraphException


class WikiBusiness(ElasticSearchBusiness):

    def __init__(self):
        ElasticSearchBusiness.__init__(self)

        #creazione dao
        self.wikidao = WikiDao(self.config.getIndexWikipedia(), self.config.getEsClient())

    def __bulkPrepareWords(self, list_of_words:list):
        """
        Data validation to get outgoing links of array of words. Preparing bulk query and return dict of results
        @:param list_of_words: list
        @:return dizionario: dict
        """
        arrayL = []
        list_of_words = [word.lower() for word in list_of_words if word.lower() not in self.stopWords]
        for word in list_of_words:
            if not self.stringValidator.exec_validation(word):
                self.log.error('bulkGetOutgoingLinks: {w} is not a valid string'.format(w=word))
                raise WikipediaGraphException(
                    'Oops. Looks like you have not passed a string or unicode var: {w})'.format(w=word))

            self.log.debug('preparing a bulk query. Word: {w}'.format(w=word.strip()))
            body = self.wikidao.createBulkFixSingleWord(word.strip())
            arrayL.extend(body)

        return self.wikidao.bulkSearchOnES(arrayL, list_of_words)


    def bulkGetPages(self, list_of_words:list):
        """
        get outgoing links by list of string
        @:param list_of_word: list
        @:return dizionario: dict
        """
        if not self.listValidator.exec_validation(list_of_words):
            self.log.error('bulkGetOutgoingLinks: {l} is not a list'.format(l=list_of_words))
            raise WikipediaGraphException('Oops. Looks like you have not passed a list var: {l})'.format(l=list_of_words))

        dizionario = self.__bulkPrepareWords(list_of_words)
        return dizionario
