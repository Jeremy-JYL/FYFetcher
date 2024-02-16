main:
	pyinstaller --onefile FYFetcher.py
	mv ./dist/FYFetcher .

install:
	cp ./FYFetcher /usr/bin/FYFetcher

cleanup:
	rm -rf dist build FYFetcher.spec
