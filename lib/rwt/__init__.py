import glob
import os
import errno
from rwt.post import Post
from rwt.ware import Ware
from jinja2 import FileSystemLoader
from jinja2.environment import Environment


main_dir = os.path.dirname(os.path.realpath(__file__)) + "/../../"

env = Environment()
env.loader = FileSystemLoader(main_dir + './templates')


# http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def load_posts(wares):
    posts = []
    categories = set([])
    n_wares = 0
    for pp in glob.glob("posts/*.interview"):
        p = Post(pp, wares)
        for c in p.categories:
            categories.add(c)
        posts.append(p)
        n_wares += len(p.p_wares)
    return posts, len(categories), n_wares


def load_wares():
    wares = {}
    for wy in glob.glob("data/wares/*/*.yml"):
        w = Ware(wy)
        k = str(w.short_name).lower()
        wares[k] = w
    return wares


def render(out_file, tname='default.html', **kwargs):
    mkdir_p(os.path.dirname(out_file))
    tmpl = env.get_template(tname)
    with open(out_file, 'w') as _f:
        _f.write(tmpl.render(**kwargs))
