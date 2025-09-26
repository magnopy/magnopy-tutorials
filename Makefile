.DEFAULT_GOAL := help

# Sphinx-related variables
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = _build

help:
	@echo "\x1b[31m"
	@echo "Please specify what do you want to do."
	@echo "\x1b[0m"
	@echo "Available options are:\n"
	@echo "    help - show this message"
	@echo "    html - build the html docs"
	@echo "    clean-html - clean all files from docs and build html docs from scratch"
	@echo "    doctest - run doctests"
	@echo "    clean - clean all files from docs and pip routines"
	@echo "    requirements - install all requirements"

# Development environment
m:
	@pip install -r docs/requirements.txt --no-cache


clean:
	-@rm -r docs/_build
	-@rm -r docs/source/*/generated
	-@rm -r docs/source/*/*/generated
	-@rm -r docs/source/*/*/*/generated
	-@rm -r build
	-@rm -r dist
	-@rm -r docs/source/master-tutorial



html:
	@$(SPHINXBUILD) -M html "docs/$(SOURCEDIR)" "docs/$(BUILDDIR)" $(SPHINXOPTS)

clean-html: clean html
	@echo "Done"


# Tests
doctest:
	@$(SPHINXBUILD) -b doctest "docs/$(SOURCEDIR)" "docs/$(BUILDDIR)" $(SPHINXOPTS)

cats:
	-@rm docs/source/img/cat-numbers/*
	@python dev-tools/generate-cat-numbers.py


logo:
	-@ rm docs/source/_static/logo-black.png
	-@ rm docs/source/_static/logo-white.png
	@python dev-tools/generate-logo.py
