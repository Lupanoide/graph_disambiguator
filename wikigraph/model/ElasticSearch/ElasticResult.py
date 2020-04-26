from types import SimpleNamespace as Namespace
import json


class ElasticResult:

    def __init__(self, data):
        str_data = json.dumps(data)
        object = json.loads(str_data, object_hook=lambda d: Namespace(**d))
        self.object = object



