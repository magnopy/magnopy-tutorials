r"""
Introducing magnopy
*******************

.. admonition:: Tutorial tasks

    *   Install magnopy
    *   Check that you have version 0.2.1 available

First of all, |magnopy|_ shall be installed. For the extended guide you can read
|magnopy-installation|_. Type the following command in the free notebook cell, run it and
restart the kernel if necessary.

.. code-block:: bash

    %pip install "magnopy[visual]" --upgrade

Note that you are installing the extended version of magnopy that supports generation of
``.png`` and ``.html`` files. Those files will be mentioned in this tutorial.

.. note::

    We recommend to install magnopy with its visual capabilities whenever possible.
    Magnopy outputs graphics by default if |plotly|_ and |matplotlib|_ are installed.
    Nevertheless, graphical libraries are not included as default dependencies
    of magnopy in order to offer computational capabilities of magnopy even if those
    libraries are unaccessible.


Import
======

Magnopy has a well defined set of public functions, that shall be available with code
completion. Full list of available methods and objects can always be found in the
|magnopy-API|_.

Import magnopy as any other Python library
"""

import magnopy

# %%
# Once imported, all magnopy's public objects are available under ``magnopy.``.
#
# .. hint::
#
#     It is enough to import magnopy once at the top of the notebook.
#
# Check that installation worked properly by printing magnopy's logo

print(magnopy.logo())

# %%
# .. important::
#     Check that you have magnopy version ``v0.2.1``.


# sphinx_gallery_thumbnail_path = 'img/cat-numbers/1.png'
