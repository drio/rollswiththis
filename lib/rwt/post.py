import sys
import yaml
import markdown2

reload(sys)
sys.setdefaultencoding('utf-8')


class Post(object):
    def __init__(self, path):
        self._input = open(path).read()
        self.yaml = {}
        self.markdown = ""
        self.load_yaml()
        self.load_markdown()

    def load_yaml(self):
        docs = yaml.load_all(self._input)
        first_doc = True
        for doc in docs:
            if first_doc:
                for k, v in doc.items():
                    self.yaml[k] = v
                first_doc = False
            else:
                break

        y = self.yaml
        self.dot_name = y['name'].replace(" ", ".")
        self.name = y['name']
        self.summary = y['summary']
        self.categories = y['categories']
        self.time = "XXXXXXXXXXXXXXXXXXXXX"

    def load_markdown(self):
        n = 0
        for l in self._input.split('\n'):
            if n == 2:
                self.markdown += l + "\n"
            if l[0:3] == '---':
                n += 1

    def html(self):
        return markdown2.markdown(self.markdown)
