r"""
Introducing magnopy
*******************

.. admonition:: Tutorial tasks

    *   Install magnopy
    *   Check that you have version 0.2.0 available

First of all, |magnopy|_ shall be installed. For the full guide on installation you can
read |magnopy-installation|_. For using magnopy in this part of the tutorial you need to
install it right within the jupyter notebook. Type the following command in the free
notebook cell, run it and restart the kernel if necessary.

.. code-block:: bash

    %pip install "magnopy[visual]" --upgrade

Note that you are installing the extended version of magnopy that supports production of
``.png`` and ``.html`` files. Those file will be mentioned in this tutorial.

.. note::

    We recommend to install magnopy with its visual capabilities whenever possible.
    Magnopy will output graphics by default if |plotly|_ and |matplotlib|_ are installed.
    Nevertheless, graphical libraries are not included as default dependencies
    to the package in order to offer computational capabilities of magnopy even if those
    libraries are unaccessible.


Import
======

Magnopy has a well defined set of public functions, that shall be available with code
completion. Full list of available methods and objects one can always find on
|magnopy-API|_.

to include magnopy in your script import it in the usual way
"""

import magnopy

# %%
# Now all magnopy's public objects are available under ``magnopy.``.
#
# .. hint::
#
#     It is enough to import magnopy once at the top of the notebook.
#
# To check that installation worked properly try to execute the following

print(magnopy.logo())

# %%
# .. important::
#     Check that you have magnopy version ``v0.2.0``.


# sphinx_gallery_thumbnail_path = 'img/gallery-thumbnails/trilmax-2025/python-library/introduction.png'
