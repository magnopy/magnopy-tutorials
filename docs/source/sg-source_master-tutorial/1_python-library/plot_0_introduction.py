r"""
Introducing magnopy
*******************

.. include:: ../../exercises/0.inc

.. note::

    We recommend to install magnopy with its visual capabilities whenever possible
    (magnopy[visual]). Magnopy will output graphics by default if |plotly|_ and
    |matplotlib|_ are installed. Nevertheless, graphical libraries are not included as
    default dependencies in order to offer computational capabilities of magnopy even if
    those libraries are not available.


Import
======

Magnopy has a well defined set of public functions, that shall be available with code
completion. One can always find full list of available methods and objects on
|magnopy-API|_.
"""

import magnopy

# %%
# Now all magnopy's public objects are available under ``magnopy.``.
#
# To check that installation worked properly try print magnopy's logo

print(magnopy.logo())

# %%
# Version
# =======
# Version of magnopy can be seen in the summary printed by the :py:func:`magnopy.logo`
# function. To access the version alone you can use

print(magnopy.__version__)

# %%
# Task solutions
# ==============
#
# task 1
# ------
#
# .. code-block:: bash
#
#     %pip install "magnopy[visual]" --upgrade
#
# task 2
# ------

print(magnopy.__version__)

# sphinx_gallery_thumbnail_path = 'img/cat-numbers/0.png'
