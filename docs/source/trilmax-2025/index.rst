**********************************************
TRILMAX summer school (8-12 September of 2025)
**********************************************

**Target magnopy's version**: v0.2.0

**First published**: 10 September 2025

**Last updated**: 10 September 2025

This tutorial was first give in the |TRILMAX-summer-school|_ organized by the 
|TRILMAX-consortium|_.

Magnopy as a python library
===========================

Every page of the tutorial explains some concepts about the |magnopy|_. There is a list
of "Tutorial tasks", that can be found on top of each tutorial page, that are meant for
you to complete. The tasks are connected to the content that you find in each page. The
idea is to read the list of tasks first and then to read the page and referenced
materials, when they are noted and try to complete the task.

.. toctree::
    python-library/introduction
    python-library/crystal
    python-library/convention
    python-library/spinham
    python-library/energy
    python-library/wulfric
    python-library/lswt

Magnopy as a black box
======================

Alternative way to use magnopy, that does not require knowledge of Python is through
its command line interface. 

First, one need to install magnopy. Open a terminal and run the following in it

.. code-block:: bash

    pip install "magnopy[visual]"

Check that everything is ok by executing the command

.. code-block:: bash

    magnopy

There are currently two command line scripts in magnopy. Use the |GROGU|_ file that you have
obtained to follow the tutorial for each of them.

.. hint:: 
    Those scripts can be run from within python as well, see: 
    |magnopy-scenarios|_. One can study the source code of
    :external:py:func:`magnopy.scenarios.optimize_sd` and
    :external:py:func:`magnopy.scenarios.solve_lswt` for more advance example of how
    magnopy can be used as a python library.

.. toctree::

    black-box/optimize-sd
    black-box/lswt
