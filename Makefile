.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

DB := mikefromit

clean: clean-build clean-pyc clean-test

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

test: ## run tests quickly with the default Python
	python setup.py test

docs: ## generate Sphinx HTML documentation

initdb:
	docker-compose exec db psql -h db -d postgres -U postgres -c "DROP DATABASE IF EXISTS mikefromit"
	docker-compose exec db psql -h db -d postgres -U postgres -c "CREATE DATABASE mikefromit ENCODING 'UTF8'"
	docker-compose exec web alembic upgrade head

venv:
	python3 -m venv .venv && \
		source .venv/bin/activate && \
		pip install -e .

help:
	@echo "The following targets are available"
	@echo "clean			Remove build, test, and file artifacts"
	@echo "clean-build 		Remove build artifacts"
	@echo "clean-pyc		Remove file artifacts"
	@echo "clean-test		Remove test artifacts"
	@echo "test				Run tests quickly with default python"
	@echo "initdb			Initialize the database and run migrations"

