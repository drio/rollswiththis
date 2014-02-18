site:
	rm -rf site/ /usr/local/www/rollswiththis.com/public/*
	./tasks/build
	cp -r site/* /usr/local/www/rollswiththis.com/public/

watch:
	filewatcher "pages/*.html templates/*.html css/*" "rm -rf site; make site"

.PHONY: watch
