r"""
Convention of spin Hamiltonian
******************************

.. admonition:: Tutorial tasks

    *   Create an instance of :external:py:class:`magnopy.Convention` for every
        mathematical formula on this page.
    *   (extra) Write down the spin Hamiltonian in the convention that you usually use
        or seen recently. Create an instance of the :py:class:`magnopy.Convention` that
        describes it.

Before we move on to the Hamiltonian itself it is very important to understand that
there is a dozen of different conventions present in the literature of essentially the
same type of Hamiltonian. Here are a few examples of different conventions for the
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

Please read |magnopy-convention-problem|_ with the illustration of challenges that this
problem introduces.

We did not want to introduce a new convention in |magnopy|_ neither to use a single
convention in particular. As a solution we decided to support **any** convention that user
wants to use. Naturally, that implied a responsibility on the user: to provide one! If
spin Hamiltonian is loaded from the known source (i. e. |TB2J|_ or |GROGU|_), then magnopy
knows the convention and user can just read the Hamiltonian from the file like so

.. code-block:: python

    # Reading from TB2J
    spinham = magnopy.io.load_tb2j("exchange.out")

    # Reading from GROGU
    spinham = magnopy.io.load_grogu("spinham-from-GROGU.txt")

However, when the spin Hamiltonian is created by user, the :py:class:`magnopy.Convention`
object has to be created. For example, to introduce the convention for the Hamiltonian

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
# To consult the convention properties you can either access individual options or print
# a summary

print(convention.multiple_counting)

convention.summary()

# %%
# Pre-defined conventions
# =======================
#
# Magnopy offers some pre-defined named conventions. Use

convention = magnopy.Convention.get_predefined("GROGU")
convention.summary()
convention = magnopy.Convention.get_predefined("Vampire")
convention.summary()
convention = magnopy.Convention.get_predefined("TB2J")
convention.summary()

# %%
#
# to get one.

# %%
# Modifying convention
# ====================
#
# To get the convention where just a few of the properties are changed one can create a
# new convention and populate all of its properties again. Or use a shortcut

modified = convention.get_modified(c31=1)
modified.summary()


# sphinx_gallery_thumbnail_path = 'img/cat-numbers/3.png'
