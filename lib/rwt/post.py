import sys
import yaml
import markdown2
import re
import datetime

MATCH_DATE = re.compile(r"posts/(\d+)-(\d+)-(\d+)-")

reload(sys)
sys.setdefaultencoding('utf-8')


class Post(object):
    def __init__(self, path):
        self._input = open(path).read()
        self.yaml = {}
        self.markdown = ""
        self.__extract_date(path)
        self.__load_yaml()
        self.__load_markdown()

    def __load_yaml(self):
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

    def __load_markdown(self):
        n = 0
        for l in self._input.split('\n'):
            if n == 2:
                self.markdown += l + "\n"
            if l[0:3] == '---':
                n += 1

    def html(self):
        return markdown2.markdown(self.markdown)

    def __extract_date(self, path):
        m = MATCH_DATE.search(path)
        if m:
            year, month, day = m.group(1), m.group(2), m.group(3)
            dt = datetime.datetime(int(year), int(month), int(day))
            self.time = dt.strftime('%d, %b %Y')
        else:
            raise Exception("Invalid post file format: %s" % self.path)
