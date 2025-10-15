# ================================== LICENSE ===================================
# Magnopy - Python package for magnons.
# Copyright (C) 2023-2025 Magnopy Team
#
# e-mail: anry@uv.es, web: magnopy.org
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ================================ END LICENSE =================================


import sys
from datetime import datetime
from os.path import abspath, join
from magnopy import __version__ as version
from pathlib import Path

sys.path.insert(0, abspath(join("..", "..")))
sys.path.append(str(Path("_ext").resolve()))

import plotly.io as pio

pio.renderers.default = "sphinx_gallery"


##########################################################################################
##                                   Project metadata                                   ##
##########################################################################################
project = "magnopy-tutorials"
copyright = f"2025-{datetime.now().year}, Magnopy Team"
author = "Magnopy Team"


##########################################################################################
##                                      Extensions                                      ##
##########################################################################################
extensions = [
    "sphinx.ext.duration",  # Measure the time of the build
    "sphinx.ext.autodoc",  # Pull documentation from the docstrings
    "sphinx.ext.autosummary",  # Generate autodoc summaries
    "sphinx.ext.viewcode",  # Add links to highlighted source code
    "sphinx.ext.extlinks",  # Markup to shorten external links
    "sphinx.ext.mathjax",  # For latex-style math
    "sphinx.ext.doctest",  # For the doctest
    "sphinx_copybutton",  # Copybutton for the blocks
    "numpydoc",  # For the numpy-style docstrings
    "sphinx_design",  # For the design elements on the from page
    "sphinx.ext.intersphinx",  # Link to other projects
    "sphinx_gallery.gen_gallery",  # For graphical code examples
    "prompt-run",  # For cli examples
]

##########################################################################################
##                               Extension's configuration                              ##
##########################################################################################
sphinx_gallery_conf = {
    "examples_dirs": [
        "sg-source_master-tutorial",
    ],  # path to your example scripts
    "gallery_dirs": [
        "master-tutorial",
    ],  # path to where to save gallery generated output
    "capture_repr": ("_repr_html_", "__repr__"),  # To capture plotly's figures
    "remove_config_comments": True,  # To remove configuration comments
    "within_subsection_order": "FileNameSortKey",  # To sort by the name of the file
}

##########################################################################################
##                                  Intersphinx mapping                                 ##
##########################################################################################
intersphinx_mapping = {
    "wulfric": ("https://docs.wulfric.org/en/latest/", None),
    "magnopy": ("https://docs.magnopy.org/en/latest/", None),
}

##########################################################################################
##                                  Build configuration                                 ##
##########################################################################################
autosummary_generate = True
autodoc_member_order = "alphabetical"
smartquotes = False

# Avoid double generating the entries for the members of the class
numpydoc_class_members_toctree = False

# Fix problem with autosummary and numpydoc:
numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

##########################################################################################
##                                Options for HTML output                               ##
##########################################################################################

htmlhelp_basename = "magnopy-tutorials"
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["magnopy-tutorials.css"]

html_title = "Magnopy's tutorials"
html_favicon = "_static/favicon.ico"

# Theme-specific options
html_theme_options = {
    "light_logo": "logo-black.png",
    "dark_logo": "logo-white.png",
}

html_context = {
    "default_mode": "light",
    "display_github": True,  # Integrate GitHub
    "github_user": "magnopy",  # Username
    "github_repo": "magnopy-tutorials",  # Repo name
    "github_version": "main",
    "doc_path": "docs/source",  # Path in the checkout to the docs root
}


##########################################################################################
##              Custom variables with access from .rst files and docstrings             ##
##########################################################################################

# Custom variables with access from .rst files and docstrings
variables_to_export = ["project", "copyright", "version"]

frozen_locals = dict(locals())
rst_epilog = "\n".join(
    map(lambda x: f".. |{x}| replace:: {frozen_locals[x]}", variables_to_export)  # noqa F821
)
del frozen_locals

# Dynamic external links
# Usage :issue:`123`
extlinks = {
    "DOI": ("https://doi.org/%s", "DOI: %s"),
    "issue": ("https://github.com/magnopy/magnopy/issues/%s", "issue #%s"),
}

# Static external links
# Solution source:
# https://docutils.sourceforge.io/docs/ref/rst/directives.html#directives-for-substitution-definitions
# Usage: |Python|_
custom_links = {
    "Python": ("Python", "https://python.org"),
    "Python-installation": (
        "Python installation",
        "https://wiki.python.org/moin/BeginnersGuide/Download",
    ),
    "array-like": (
        "array-like",
        "https://numpy.org/doc/stable/glossary.html#term-array_like",
    ),
    "Git": ("Git", "https://git-scm.com/"),
    "git-add": ("git add", "https://git-scm.com/docs/git-add"),
    "git-commit": ("git commit", "https://git-scm.com/docs/git-commit"),
    "good-commit-messages": ("good commit messages", "https://cbea.ms/git-commit/"),
    "GitHub-discussions": (
        "Github discussions",
        "https://github.com/magnopy/magnopy/discussions",
    ),
    "GitHub-issues": (
        "Github issues",
        "https://github.com/magnopy/magnopy/issues",
    ),
    "repository": ("Magnopy repository", "https://github.com/magnopy/magnopy"),
    "issue-tracker": ("Issue Tracker", "https://github.com/magnopy/magnopy/issues"),
    "Forum-google-groups": (
        "Forum at google groups",
        "https://groups.google.com/g/magnopy",
    ),
    "pre-commit": ("pre-commit", "https://pre-commit.com"),
    "TB2J": ("TB2J", "https://tb2j.readthedocs.io/en/latest/"),
    "Vampire": ("Vampire", "https://vampire.york.ac.uk/"),
    "wulfric": ("wulfric", "https://docs.wulfric.org/en/latest/"),
    "magnopy": ("magnopy", "https://magnopy.org/en/latest/"),
    "wulfric-key-concepts": (
        "key concepts of wulfric",
        "https://docs.wulfric.org/en/latest/user-guide/usage/key-concepts.html",
    ),
    "myHDF5": ("myHDF5", "https://myhdf5.hdfgroup.org/"),
    "h5py": ("h5py", "https://www.h5py.org/"),
    "sphinx": ("Sphinx", "https://www.sphinx-doc.org/en/master/"),
    "sphinx-autodoc": (
        "sphinx.ext.autodoc",
        "https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html",
    ),
    "sphinx-autosummary": (
        "sphinx.ext.autosummary",
        "https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html",
    ),
    "doctest": (
        "sphinx.ext.doctest",
        "https://www.sphinx-doc.org/en/master/usage/extensions/doctest.html",
    ),
    "numpydoc": ("numpydoc", "https://numpydoc.readthedocs.io/en/latest/format.html"),
    "pytest": ("pytest", "https://docs.pytest.org/en/7.3.x/"),
    "hypothesis": ("hypothesis", "https://hypothesis.readthedocs.io/en/latest/"),
    "reStructuredText": (
        "reStructuredText",
        "https://docutils.sourceforge.io/rst.html",
    ),
    "GNU-make": ("GNU make", "https://www.gnu.org/software/make/manual/make.html"),
    "venv": ("venv", "https://docs.python.org/3/library/venv.html"),
    "PYPI": ("Python package index", "https://pypi.org/"),
    "GROGU": (
        "GROGU",
        "https://grogupy.readthedocs.io",
    ),
    "GROGU-FF": (
        "GROGU file format",
        "https://grogupy.readthedocs.io/en/latest/tutorials/magnopy_input.html",
    ),
    "BFGS": (
        "BFGS",
        "https://en.wikipedia.org/wiki/Broyden-Fletcher-Goldfarb-Shanno_algorithm",
    ),
    "multiprocessing": (
        "multiprocessing",
        "https://docs.python.org/3/library/multiprocessing.html",
    ),
    "plotly": ("Plotly", "https://plotly.com/python/"),
    "spglib": ("spglib", "https://spglib.readthedocs.io/en/stable/index.html"),
    "plotly-update-layout": (
        ".update_layout()",
        "https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html?highlight=update_layout#plotly.graph_objects.Figure.update_layout",
    ),
    "plotly-write-html": (
        ".write_html()",
        "https://plotly.com/python-api-reference/generated/plotly.io.to_html.html",
    ),
    "jupyter": ("jupyter lab or notebook", "https://jupyter.org/"),
    "matplotlib": ("matplotlib", "https://matplotlib.org/"),
    "TRILMAX-summer-school": (
        "TRILMAX summer school",
        "https://trilmax.elte.hu/trilmax-theory-summer-school/",
    ),
    "TRILMAX-consortium": ("TRILMAX consortium", "https://trilmax.elte.hu/"),
    "magnopy-installation": (
        "magnopy's guide on installation",
        "https://docs.magnopy.org/en/latest/user-guide/installation.html",
    ),
    "magnopy-API": (
        "magnopy's API page",
        "https://docs.magnopy.org/en/latest/api/index.html",
    ),
    "magnopy-cell": (
        "magnopy's dedicated documentation page",
        "https://docs.magnopy.org/en/latest/user-guide/usage/cell.html",
    ),
    "magnopy-atoms": (
        "magnopy's dedicated documentation page",
        "https://docs.magnopy.org/en/latest/user-guide/usage/atoms.html",
    ),
    "magnopy-convention-problem": (
        "Convention problem",
        "https://docs.magnopy.org/en/latest/user-guide/theory-behind/convention-problem.html",
    ),
    "magnopy-theory-spin-hamiltonian": (
        "Spin Hamiltonian",
        "https://docs.magnopy.org/en/latest/user-guide/theory-behind/spin-hamiltonian.html",
    ),
    "magnopy-how-to-execute-script": (
        "How to execute the script?",
        "https://docs.magnopy.org/en/latest/user-guide/cli/how-to-execute.html",
    ),
    "magnopy-optimize-sd": (
        "magnopy-optimize-sd",
        "https://docs.magnopy.org/en/latest/user-guide/cli/magnopy-optimize-sd/index.html",
    ),
    "magnopy-lswt": (
        "magnopy-lswt",
        "https://docs.magnopy.org/en/latest/user-guide/cli/magnopy-lswt/index.html",
    ),
    "magnopy-scenarios": (
        "magnopy.scenarios",
        "https://docs.magnopy.org/en/latest/api/scenarios.html",
    ),
    "wulfric-conventions": (
        "conventions in wulfric",
        "https://docs.wulfric.org/en/latest/user-guide/conventions/bravais-lattices/index.html",
    ),
    "wulfric-FCC": (
        "FCC",
        "https://docs.wulfric.org/en/latest/user-guide/conventions/bravais-lattices/2_sc/plot_02_FCC.html",
    ),
    "wulfric-kpath-string": (
        "wulfric: k-path",
        "https://docs.wulfric.org/en/latest/user-guide/usage/key-concepts.html#k-path",
    ),
    "wulfric-BL": (
        "wulfric: Bravais lattices",
        "https://docs.wulfric.org/en/latest/user-guide/conventions/bravais-lattices/index.html",
    ),
}
rst_epilog += "\n".join(
    map(
        lambda x: f"\n.. |{x}| replace:: {custom_links[x][0]}\n.. _{x}: {custom_links[x][1]}",
        [i for i in custom_links],
    )
)
