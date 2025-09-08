r"""
Convention of spin Hamiltonian
******************************

.. admonition:: Tutorial tasks

    *   Create an instance of :external:py:class:`magnopy.Convention` for every example
        mathematical formula that is written in this page.
    *   (extra) Write down the spin Hamiltonian in the convention that you are usually use
        or seen recently in some paper. Create an instance of the
        :external:py:class:`magnopy.Convention` that describe it.

Before we move on to the Hamiltonian itself it is very important to understand that
there is a dozen of different conventions of it present in the literature. Here are a
few examples with different conventions for the isotropic exchange term

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

In |magnopy|_ we did not want to introduce a new one or to use one convention in particular.
As a solution we decided to support **any** convention that the user what to use. Naturally,
that implied a responsibility on the user: to provide one! If spin Hamiltonian is
read from the knows source (i. e. |TB2J|_ or |GROGU|_), then magnopy knows the convention
and user can just read the Hamiltonian from the file like so

.. code-block::

    # Reading from TB2J
    spinham = magnopy.io.load_tb2j("exchange.out")

    # Reading from GROGU
    spinham = magnopy.io.load_grogu("spinham-from-GROGU.txt")

However, when the spin Hamiltonian is created by user explicitly, the
:external:py:class:`magnopy.Convention`. object has to be created. For example to
introduce the convention for the Hamiltonian that is written as

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

.. code-block:: python

    convention = magnopy.Convention(
        c21 = 1,
        c22= 0.5,
        multiple_counting=False,
        spin_normalized=False
    )
"""

# sphinx_gallery_thumbnail_path = 'img/gallery-thumbnails/trilmax-2025/python-library/convention.png'
