.. _trilmax-2025_spinham:

****************
Spin Hamiltonian
****************

.. admonition:: Tutorial tasks

    *   Create a spin Hamiltonian of the orthorhombic ferromagnet with tree magnetic axis
        (easy, medium and hard).
    *   Change the convention of the spin Hamiltonian. Inspect how the parameters are
        changing when you do so.
    *   Add some magnetic field to it. check the values of the parameters of the
        Hamiltonian that stores the magnetic field.
    *   Add magnetic dipole-dipole interaction. Test both energy and distance cut-offs.
        Which parameters of the spin Hamiltonian change?


At the heart of magnopy is the :external:py:class:`magnopy.SpinHamiltonian`.

It is created on some crystal, that has been discussed in the previous section and adds
*interaction parameters* to it.

.. _trilmax-2025_spinham_creating:

Creating a Hamiltonian
======================

Spin Hamiltonian (an empty one) is created from three objects

* cell
* atoms
* convention

.. code-block:: python

    import numpy as np

    # Cubic cell with a = 1
    cell = np.eye(3)

    # One atom per unit cell
    atoms = dict(
        names = ["Fe"],
        positions = [[0.0, 0.0, 0.0]]
        spins = [2.5],
        g_factors = [2],

    )

    # Convention
    convention = magnopy.Convention(
        multiple_counting=True,
        spin_normalized=False,
        c1=1,
        c21=1,
        c22=1/2
    )

    # Create a Hamiltonian
    spinham = magnopy.SpinHamiltonian(
        cell=cell,
        atoms=atoms,
        convention=convention
    )

.. _trilmax-2025_spinham_add-params:

Adding parameter to the Hamiltonian
===================================

Now everything is ready to add some parameters to the spin Hamiltonian. Magnopy stores
the parameters in the form that is closely resemble mathematical form of the spin
Hamiltonian, that can be found in |magnopy-theory-spin-hamiltonian|_ page.

Magnopy supports up to four-spin terms with full tensors of the interaction parameters.
For the purpose of this tutorial we will focus on the first three terms of the expanded
form.

For each term of the spin Hamiltonian there are two functions defined, that add and remove
a parameter from the Hamiltonian. For example, to add an isotropic exchange parameter
between two different cites with the bond along the first lattice vector use

.. code-block:: python

    spinham.add_22(alpha=0, beta=0, nu=(1, 0, 0), parameter=np.eye(3))

Note several things:

*   ``alpha`` and ``beta`` are indices of the lists in ``atoms``. In that example they
    both point to the first atom.
*   Due to the translation symmetry of the Hamiltonian it is enough to specify all
    parameters for some chosen unit cell. This unit cell is commonly labeled as ``(0, 0, 0)``.
    index ``alpha`` specifies the first atom, that is in ``(0, 0, 0)`` unit cell.
    Index ``beta`` specify the second atom, that is understood to be located in the
    unit cell specified by ``nu``. In the example above second atom is from ``(1, 0, 0)``
    unit cell.
*   Any parameter for the term that involves two spins is a 3x3 matrix. An isotropic
    parameter in the matrix form is a diagonal matrix with all diagonal elements being the
    same.


To check what parameters you have in the spin Hamiltonian use the property, that is
defined for each term of the expanded form as well. For example for two-spins/two-sites
term

.. code-block:: python

    for alpha, beta, nu, parameter in spinham.p22:
        print(alpha, beta, nu)
        print(parameter)

.. _trilmax-2025_spinham_change-convention:

Changing the convention
=======================

The parameter that are added to the Hamiltonian are expected to be compliant with the
Hamiltonian's convention. The latter can always be checked with

.. code-block:: python

    print(spinham.convention.summary())

Once the parameter are added to the Hamiltonian there is an option of changing the
convention. Magnopy will recompute all the parameter in the way, that the Hamiltonian
will still describe the same physical system.

.. code-block:: python

    new_convention = magnopy.Convention.get_predefined(name="GROGU")

    spinham.convention = new_convention

.. _trilmax-2025_spinham_add-field:

Adding magnetic field
=====================

Due to the design choices that were made in magnopy, external magnetic field take the form
of the parameter with one-spin/one-site (``c1``, ``add_1``, ``remove_1``). To save the
effort of converting the vector of magnetic field to the parameter every time magnopy has
a method that is convenient to use. For example, to add an external magnetic field
directed along the y axis with the value of 1.42 Tesla use

.. code-block:: python

    spinham.add_magnetic_field(h = (0.0, 1.42, 0.0))

.. _trilmax-2025_spinham_add-dip-dip:

Adding magnetic dipole-dipole interaction
=========================================

Magnetic dipole-dipole interaction can be written ad a two-spin/two-sites parameter.
To save the burden of manual conversion in every use magnopy has a pre-defined method
that adds magnetic dipole-dipole interaction to the spin Hamiltonian.

This interaction is of the long range. Currently magnopy only implements its inclusion
by the cut-off value.

*   Cut-off by distance: all interaction that are shorter than cut-off are added

    .. code-block:: python

        spinham.add_add_dipole_dipole(R_cut=20)

*   Cut-off by parameter value (in meV): all interactions that are larger than the
    cut-off are added.

    .. code-block:: python

        spinham.add_add_dipole_dipole(E_cut=0.1)

See :external:py:meth:`magnopy.SpinHamiltonian.add_dipole_dipole` for more details.

.. _trilmax-2025_spinham_arithmetics:

Arithmetic operations
=====================

The mathematical form of the spin Hamiltonian involves a lot of summation. One would like
to easily sum two Hamiltonians to get a Hamiltonian for combined effects.

Good news is that magnopy implements addition and subtraction of two Hamiltonians.
Moreover, it implements multiplication of the Hamiltonian by any number.

.. important::
    For summation and subtraction the two Hamiltonians shall be defined on the same cell
    and atoms.

.. hint::

    To get an independent instance of spin Hamiltonian with the same cell, atoms but with
    all parameters removed from it you can use
    :external:py:meth:`magnopy.SpinHamiltonian.get_empty`


For example, imagine that you created the Hamiltonian with some set of parameters and you
would like to optimize spin direction on it and then get energy contributions of
different terms. This can be done as

.. code-block:: python

    spinham_exchange = magnopy.SpinHamiltonian(
        cell=cell,
        atoms=atoms,
        convention=convention
    )

    spinham_exchange.add_22(
        alpha=0,
        beta=0,
        nu=(1, 0, 0)
    )

    # Now get a Zeeman term
    spinham_zeeman = spinham_exchange.get_empty()
    spinham_zeeman.add_magnetic_field(h=(1.42, 0, 0))

    # Next get magnetic dipole-dipole term
    spinham_dd = spinham_exchange.get_empty()
    spinham_dd.add_dipole_dipole(R_cut=20)

    # Next get full Hamiltonian

    spinham_full = spinham_exchange + spinham_zeeman + spinham_dd

Now ``spinham_full`` can be used to optimize energy and get ``spin_direction`` of the
local minima (covered in the next sections), then obtained ``spin_directions`` can be used
with each individual term to get its contribution.
