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
	-@rm -r magnopy/magnopy.egg-info
	-@rm -r build
	-@rm -r dist
	-@rm -r .venv/lib/python*/site-packages/magnopy*
	-@rm -r .venv/bin/magnopy*


html:
	@$(SPHINXBUILD) -M html "docs/$(SOURCEDIR)" "docs/$(BUILDDIR)" $(SPHINXOPTS)

clean-html: clean html
	@echo "Done"


# Tests
doctest:
	@$(SPHINXBUILD) -b doctest "docs/$(SOURCEDIR)" "docs/$(BUILDDIR)" $(SPHINXOPTS)
