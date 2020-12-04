install:
	@poetry install

lint:
	@poetry run flake8 gendiff

test:
	@poetry run pytest --cov=gendiff --cov-report xml tests/

selfcheck:
	@poetry check

check: selfcheck test lint

build: check
	@poetry build

.PHONY: install build lint test selfcheck check
