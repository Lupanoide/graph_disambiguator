import unittest
from wikigraph.business.WikiBusiness import WikiBusiness



class WikiBusinessTest(unittest.TestCase):

    def setUp(self):
        self.business = WikiBusiness()

    def test_retrieve_sense_by_word(self):
        self.assertIsNotNone(self.business.retrieveSenseByWord("cane"))

    def test_lemmatize_retrieve_sense_by_word(self):
        self.assertIsNotNone(self.business.lemmatizeAndRetrieveSenseByWord("cane"))

    def test_bulk_retrieve_sense_by_list(self):
        self.assertIsNotNone(self.business.bulkRetrieveSenseByList(["cane","gatto"]))

    def test_lemmatize_bulk_retrieve_sense_by_list(self):
        self.assertIsNotNone(self.business.lemmatizeAndBulkRetrieveSenseByList(["cane","gatto"]))

    def test_retrieve_definition_gloss_by_synset(self):
        self.assertIsNotNone(self.business.retrieveDefinitionGlossBySynset("ita-10-07970721-n"))

    def test_multi_get_definition_gloss_by_list(self):
        self.assertIsNotNone(self.business.multiGetDefinitionGlossByList(["ita-10-07970721-n","ita-10-06202686-n"]))

    def test_retrieve_writtenform_by_synset(self):
        self.assertIsNotNone(self.assertIsNotNone(self.business.retrieveWrittenFormBySynset("ita-10-07970721-n")))

    def test_bulk_retrieve_writtenform_by_list(self):
        self.assertIsNotNone(self.business.bulkRetrieveWrittenFormByList(["ita-10-07970721-n","ita-10-06202686-n"]))

    def test_retrieve_semantic_relation_by_synset(self):
        self.assertIsNotNone(self.business.retrieveSemanticRelationshipBySynset("ita-10-07970721-n"))

    def test_retrive_semantic_relation_by_list(self):
        self.assertIsNotNone(self.business.retrieveSemanticRelationshipByList(["ita-10-07970721-n","ita-10-06202686-n"]))


if __name__ == '__main__':

    business = WikiBusiness()


    

