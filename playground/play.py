#!./virt_env/bin/python
#
from jinja2 import FileSystemLoader
from jinja2.environment import Environment

env = Environment()
env.loader = FileSystemLoader('./playground')

tmpl = env.get_template('interview.html')
data = {}
data['title'] = 'A great page title'
data['interview'] = 'the interview here...'
print tmpl.render(data=data)

tmpl = env.get_template('interviews.html')
data = {}
data['title'] = 'A great page title'
data['interviews'] = [{"name": "one"}, {"name": "two"}]
print tmpl.render(data=data)
