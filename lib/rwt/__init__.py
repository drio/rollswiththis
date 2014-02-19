import glob
import os
import errno
from rwt.post import Post
from jinja2 import FileSystemLoader
from jinja2.environment import Environment


main_dir = os.path.dirname(os.path.realpath(__file__)) + "/../../"

env = Environment()
env.loader = FileSystemLoader(main_dir + './templates')


# http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def load_posts():
    posts = []
    for pp in glob.glob("posts/*.interview"):
        posts.append(Post(pp))
    return posts


def render(data, out_file, tname='default.html'):
    mkdir_p(os.path.dirname(out_file))
    tmpl = env.get_template(tname)
    with open(out_file, 'w') as _f:
        _f.write(tmpl.render(data=data))
