#!./virt_env/bin/python
#
from jinja2 import FileSystemLoader
from jinja2.environment import Environment
import markdown2
import rwt

env = Environment()
env.loader = FileSystemLoader('./playground')

tmpl = env.get_template('interview.html')
data = {}
data['title'] = 'A great page title'
data['interview'] = 'the interview here...'
#print tmpl.render(data=data, title="fooooooo")

tmpl = env.get_template('interviews.html')
data = {}
data['title'] = 'A great page title'
data['interviews'] = [{"name": "one"}, {"name": "two"}]
#print tmpl.render(data=data, title="barrrrrrrrrrrrra")



wares = rwt.load_wares()
print "Loaded %s wares." % len(wares)

p = rwt.Post('posts/2014-02-23-jordi.fernandez.interview', wares)
print "----"
print p.name
print p.summary
print p.categories
print p.markdown
#print p.html()


