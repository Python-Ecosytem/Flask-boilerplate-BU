.ONESHELL:

.PHONY: clean install tests run all

help:
	@echo "  env         create a development environment using virtualenv"
	@echo "  deps        install dependencies using pip"
	@echo "  clean       remove unwanted files like .pyc's"
	@echo "  lint        check style with flake8"
	@echo "  test        run all your tests using py.test"

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete
	find . | grep -E "(__pycache__|\.pyc|\.DS_Store|\.db|\.pyo$\)" | xargs rm -rf


env:
python3 -m venv env && \
. env/bin/activate && \
#make deps

install:
	virtualenv venv; \
	. venv/bin/activate; \
	pip install -r requirements.txt;

deps:
. venv/bin/activate; \
pip install -r requirements.txt

tests:
	. venv/bin/activate; \
	python manage.py test
	#py.test tests

lint:
	flake8 --exclude=env .


run:
	. venv/bin/activate; \
	python manage.py run

all: clean install tests run
