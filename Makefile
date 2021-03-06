site:
	rm -rf site/ /usr/local/www/rollswiththis.com/public/*
	./tasks/build
	cp -r site/* /usr/local/www/rollswiththis.com/public/

virt_env:
	virtualenv virt_env
	./virt_env/bin/pip install jinja2
	./virt_env/bin/pip install markdown2
	./virt_env/bin/pip install pyyaml
	@echo '---'
	@echo '--> $ source virt_env/bin/activate'

test:
	python tests/*.py

watch:
	filewatcher "pages/*.html templates/*.html css/*" "rm -rf site; make site"

.PHONY: watch test
