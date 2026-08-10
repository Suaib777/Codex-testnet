.PHONY: install test lint

install:
	pip install -r requirements.txt

test:
	pytest

lint:
	python -m compileall src
