r"""
Convention of spin Hamiltonian
******************************

.. include:: ../../exercises/2.inc

Before we move on to the Hamiltonian itself it is very important to understand that
there is a dozen of different conventions of essentially the same type of Hamiltonian
present in the literature. Here are a few examples of different conventions for the
isotropic exchange term

.. math::

    \mathcal{H}
    &=
    -\sum_{i,j}
    J_{ij}
    \boldsymbol{S}_i
    \cdot
    \boldsymbol{S}_j

    \mathcal{H}
    &=
    \sum_{i,j}
    J_{ij}
    \boldsymbol{e}_i
    \cdot
    \boldsymbol{e}_j

    \mathcal{H}
    &=
    -\dfrac{1}{2}\sum_{i<j}
    J_{ij}
    \boldsymbol{S}_i
    \cdot
    \boldsymbol{S}_j

Please read |magnopy-convention-problem|_ for the illustration of the challenges that this
problem introduces.

In |magnopy|_ we did not want to introduce a new one or to use one convention in
particular. As a solution we decided to support **any** convention that the user wants to
use. Naturally, that implied a responsibility on the user: to provide one! When spin
Hamiltonian is read from the knows source (i. e. |TB2J|_ or |GROGU|_), magnopy knows
the convention and user can just read the Hamiltonian from the file like so

.. code-block:: python

    # Reading from TB2J
    spinham = magnopy.io.load_tb2j("exchange.out")

    # Reading from GROGU
    spinham = magnopy.io.load_grogu("spinham-from-GROGU.txt")

However, :py:class:`magnopy.Convention` object has to be created and supplied when the
spin Hamiltonian is created by user. For example, to introduce the convention for the
Hamiltonian that is written as

.. math::

    \mathcal{H}
    =
    \sum_i
    K_z\left(S_i^z\right)^2
    +
    \dfrac{1}{2}
    \sum_{i, j>i}
    J_{i,j}
    \boldsymbol{S}_i
    \cdot
    \boldsymbol{S}_j

one shall create the convention object as
"""

import magnopy

convention = magnopy.Convention(
    c21=1, c22=0.5, multiple_counting=False, spin_normalized=False
)

# %%
#
# To consult the convention properties you can display either individual properties

print(convention.c21)
print(convention.multiple_counting)

# %%
#
# or the whole convention

print(convention)

# %%
# Pre-defined conventions
# =======================
#
# Magnopy has some pre-defined named conventions. To get one use

convention = magnopy.Convention.get_predefined("GROGU")
print(convention)
convention = magnopy.Convention.get_predefined("Vampire")
print(convention)
convention = magnopy.Convention.get_predefined("TB2J")
print(convention)

# %%
# Modifying convention
# ====================
#
# To get the convention where just a few of the properties are changed one can create a
# new convention and populate all of its properties again. Or use a shortcut

convention = magnopy.Convention.get_predefined("TB2J")
modified = convention.get_modified(c31=1, name="modified")
print(convention)
print(modified)

# sphinx_gallery_thumbnail_path = 'img/cat-numbers/2.png'
