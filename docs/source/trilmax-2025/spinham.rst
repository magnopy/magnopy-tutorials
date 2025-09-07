****************
Spin Hamiltonian
****************

At the heart of magnopy is the :magnopy:`SpinHamiltonian`.

It is created on some crystal, that has been discussed in the previous section and adds
*interaction parameters* to it. 

Hamiltonian's convention
========================

Before we move on to the Hamiltonian itself it is very important to understand that
there is a dozen of different conventions of it present in the literature.

Please read FIXME-convention-problem for the illustration of the challenges that this
problem introduces.


In |magnopy|_ we did not want to introduce a new one or to use one convention in particular.
As a solution we decided to support **any** convention that the user what to use. Naturally, 
that implied a responsibility on the user: to provide one! If SpinHamiltonian is
read from the knows source (i. e. |TB2J|_ or |GROGU|_), then magnopy knows the convention
and user can just read the Hamiltonian from the file like so

.. code-block::

    import magnopy

    # Reading from TB2J
    spinham = magnopy.io.load_tb2j("exchange.out")

    # Reading from GROGU
    spinham = magnopy.io.load_grogu("spinham-from-GROGU.txt")

However, when the SpinHamiltonian is created by user explicitly, the :magnopy:`Convention`
object has to be created. For example to introduce the convention for the Hamiltonian that
is written as

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

    import magnopy

    convention = magnopy.Convention(
        c21 = 1, 
        c22= 0.5, 
        multiple_counting=False, 
        spin_normalized=False
    )
