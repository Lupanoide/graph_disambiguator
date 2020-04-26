from wikigraph.model.ElasticSearch.ElasticResult import ElasticResult


class WikiResult(ElasticResult):
    def __init__(self, data):
        ElasticResult.__init__(self, data)

    def get_title(self):
        return self.object.title

    def get_redirects(self):
        redirectL = list()
        redirects = self.object.redirect
        for redirect in redirects:
            redirectL.append(redirect.title)
        return redirectL





