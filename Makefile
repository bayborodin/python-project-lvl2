install:
	@poetry install

build:
	@poetry build

lint:
	@poetry run flake8 gendiff

run:
	@poetry run gendiff ~/file1.json ~/file2.json

.PHONY: install build lint run
