import sys
import yaml
import markdown2
import re
import datetime

MATCH_DATE = re.compile(r"posts/(\d+)-(\d+)-(\d+)-")
MATCH_WARE = re.compile(r"(\[[\w-]+\]\(\))")
MATCH_NAME = re.compile(r"\[([\w-]+)\]")

reload(sys)
sys.setdefaultencoding('utf-8')


class Post(object):
    def __init__(self, path, wares):
        self._input = open(path).read()
        self.p_wares = set([])
        self.wares = wares
        self.yaml = {}
        self.markdown = ""
        self.__extract_date(path)
        self.__load_yaml()
        self.__load_markdown()
        self.__expand_wares()

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

    def __expand_wares(self):
        d_wr = {}
        for md_ware in re.findall(MATCH_WARE, self.markdown):
            for w_name in re.findall(MATCH_NAME, md_ware):
                n = w_name.lower()
                if n in self.wares:
                    d_wr[n] = self.wares[n].url
                else:
                    raise Exception("I cannot expand ware: %s" % w_name)

        for name, url in d_wr.items():
            self.p_wares.add(name)
            self.markdown = self.markdown.replace('[%s]()' % name,
                                                  '[%s](%s)' % (name, url))

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
