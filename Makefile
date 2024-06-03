SHELL:=/bin/bash
LIB_DIR=lib
PWD:=$(shell pwd)
VENV=venv/bin
PIP=$(VENV)/pip3
PIP_FLAGS=--trusted-host=http://pypi.python.org/simple/
PYTHON_VERSION=python3.11
HOST_PYTHON_VER=$(shell echo which $(PYTHON_VERSION))
VENV_PYTHON_VER=$(VENV)/python3

.PHONY: all venv

all: venv

venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || $(PYTHON_VERSION) -m venv venv --upgrade-deps
	$(VENV_PYTHON_VER) -m pip install --upgrade pip $(PIP_FLAGS)
	$(PIP) $(PIP_FLAGS) install --upgrade-strategy eager -Ur requirements.txt || ( touch requirements.txt && exit 1 )

clean:
	rm -rf .cache
	find . -name '*.pyc' -type f -delete
