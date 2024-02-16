main:
	pyinstaller --onefile FYFetcher.py

install:
	cp ./dist/FYFetcher /usr/bin/FYFetcher

cleanup:
	rm -rf dist build FYFetcher.spec
