import yaml


class Ware(object):
    def __init__(self, path):
        self._input = open(path).read()
        self.__load_yaml()

    def __load_yaml(self):
        y = {}
        docs = yaml.load_all(self._input)
        for doc in docs:
            for k, v in doc.items():
                y[k] = v

        self.name = y['name']
        self.description = y['description']
        self.url = y['url']
