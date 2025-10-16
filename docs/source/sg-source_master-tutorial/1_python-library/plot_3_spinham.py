r"""
Spin Hamiltonian
****************

.. include:: ../../exercises/3.inc

Now we are ready to discuss :py:class:`magnopy.SpinHamiltonian`.

It is created on some crystal, which was discussed in the previous section and adds
*interaction parameters* to it.

Read |magnopy-spinham|_ for the detailed introduction.


Creating a Hamiltonian
======================

Spin Hamiltonian is created from three objects

* cell
* atoms
* convention

Here we create a Hamiltonian for the ferromagnetic nearest-neighbor Heisenberg model with
triaxial on-site anisotropy on a simple orthorhombic lattice.

.. math::
    \mathcal{H}
    =
    \sum_{i}
    \Bigl(
        K_x (S_i^x)^2
        +
        K_y (S_i^y)^2
        +
        K_z (S_i^z)^2
    \Bigr)
    +
    \dfrac{1}{2}
    J
    \sum_{i, j}
    \mathbf{S}_i
    \cdot
    \mathbf{S}_j

In the notation (not convention, but notation) that resembles magnopy's code the same
Hamiltonian can be written as

.. math::
    \mathcal{H}
    =
    \sum_{\mu,\alpha}
    \mathbf{S}_{\mu, \alpha}
    \cdot
    \mathbf{J}_{\mu, \alpha}
    \cdot
    \mathbf{S}_{\mu, \alpha}
    +
    \dfrac{1}{2}
    \sum_{\mu,\nu,\alpha,\beta}
    \mathbf{S}_{\mu, \alpha}
    \cdot
    \mathbf{J}_{\alpha\beta,\nu}
    \cdot
    \mathbf{S}_{\mu+\nu, \beta}

where 

.. math::

    \mathbf{J}_{\mu\alpha}
    =
    \begin{pmatrix}
        K_x & 0 & 0 \\
        0 & K_y & 0 \\
        0 & 0 & K_z
    \end{pmatrix}

and 

.. math::

    \mathbf{J}_{\alpha\beta,\nu}
    =
    \begin{pmatrix}
        J & 0 & 0 \\
        0 & J & 0 \\    
        0 & 0 & J
    \end{pmatrix}

if :math:`\alpha = \beta` and :math:`\nu \in \{(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)\}` and 

.. math:: 

    \mathbf{J}_{\alpha\beta,\nu}
    =
    \begin{pmatrix}
        0 & 0 & 0 \\
        0 & 0 & 0 \\    
        0 & 0 & 0   
    \end{pmatrix}

otherwise.
"""

import numpy as np
import magnopy

# %%
#
# Creating a Hamiltonian instance
# ===============================

# Orthorhombic cell with a = 1, b=1.5, c=2
cell = np.diag([1, 1.5, 2])

# One atom per unit cell
atoms = dict(
    names=["Fe"],
    positions=[[0.0, 0.0, 0.0]],
    spins=[2.5],
    g_factors=[2],
)

# Convention
convention = magnopy.Convention(
    multiple_counting=True, spin_normalized=False, c21=1, c22=1 / 2
)

# Create a Hamiltonian
spinham = magnopy.SpinHamiltonian(cell=cell, atoms=atoms, convention=convention)

# %%
#
# Adding parameter to the Hamiltonian
# ===================================
#
# Now everything is ready to add some parameters. Magnopy stores the parameters in the
# form that closely resembles mathematical form of the spin Hamiltonian, which can be
# found in |magnopy-theory-spin-hamiltonian|_ page (see "Expanded form").
#
# Magnopy supports terms with up to four spins with full tensors of the interaction
# parameters
#
# * :math:`1\times3` for one-spin parameters
# * :math:`3\times3` for two-spin parameters
# * :math:`3\times3\times3` for three-spin parameters
# * :math:`3\times3\times3\times3` for four-spin parameters.
#
# For the purpose of this tutorial we will focus on the first three terms of the expanded
# form (i.e. one-spin and two-spin terms).
#
# Two functions are defined for each group of parameter, that add or
# remove a parameter from the Hamiltonian. For example, to add or remove a
# two-spin/two-sites parameter one can use :py:meth:`magnopy.SpinHamiltonian.add_22` or
# :py:meth:`magnopy.SpinHamiltonian.remove_22`.
#
# First, lets add isotropic exchange interaction between nearest neighbors with the value
# :math:`J = -1` meV.

# J < 0 for ferromagnetic coupling (according to the chosen convention: c22 = 1/2)
parameter = magnopy.converter22.from_iso(iso=-1)
print(f"parameter is \n{parameter}")

spinham.add_22(alpha=0, beta=0, nu=(1, 0, 0), parameter=parameter)
spinham.add_22(alpha=0, beta=0, nu=(0, 1, 0), parameter=parameter)
spinham.add_22(alpha=0, beta=0, nu=(0, 0, 1), parameter=parameter)

# %%
# .. note::
#
#   *  ``alpha`` and ``beta`` are indices of the lists in ``atoms``. In that example they
#      both point to the first atom.
#   *  Due to the translation symmetry of the Hamiltonian it is enough to specify all
#      parameters for some chosen unit cell. This unit cell is commonly labeled as
#      ``(0, 0, 0)``. Index ``alpha`` specifies the first atom, that is always in the
#      ``(0, 0, 0)`` unit cell. Index ``beta`` specify the second atom, that is understood
#      to be located in the unit cell specified by ``nu``. In the example above second
#      atom is from ``(1, 0, 0)``, ``(0, 1, 0)`` or ``(0, 0, 1)`` unit cell.
#   *  Any parameter for the term that involves two spins is a 3x3 matrix. An isotropic
#      parameter in the matrix form is a diagonal matrix with all diagonal elements being
#      the same.
#
# One does not need to add parameters for :math:`\nu \in \{(-1,0,0), (0,-1,0), (0,0,-1)\}`.
# Since multiple counting is ``True``, magnopy will automatically add those.


for index, (alpha, beta, nu, parameter) in enumerate(spinham.p22):
    atom_000 = spinham.atoms["names"][alpha]
    atom_nu = spinham.atoms["names"][beta]
    print(f"Bond #{index + 1}")
    print(f"{atom_000} in (0, 0, 0) unit cell -> {atom_nu} in {nu} unit cell")
    print(parameter)

# %%
#
# Next, we add on-site anisotropy with :math:`K_x = -0.1` meV, :math:`K_y = -0.2` and
# :math:`K_z = -0.3` meV.

parameter = np.diag([-0.1, -0.2, -0.3])
print(f"parameter is \n{parameter}")

spinham.add_21(alpha=0, parameter=parameter)

for alpha, parameter in spinham.p21:
    print(
        f"On-site anisotropy for atom {spinham.atoms['names'][alpha]} is\n{parameter}"
    )

# %%
#
# Changing convention
# ===================
#
# All parameters that are added to the Hamiltonian are expected to be compliant with the
# Hamiltonian's convention. The latter can always be checked with

print(spinham.convention)

# %%
# You can change the convention of the Hamiltonian at any moment. Magnopy will recompute
# all existing parameters in such a way, that physical properties of the Hamiltonian do
# not change. All parameters that will be added later shall be compliant with the new
# convention.

new_convention = magnopy.Convention.get_predefined(name="GROGU")

spinham.convention = new_convention

print(spinham.convention)

# %%
#
# Arithmetic operations
# =====================
#
# Mathematical form of the spin Hamiltonian involves a lot of summation. It might be
# convenient to be able to sum two Hamiltonians together.
#
# Good news is that magnopy implements addition and subtraction of two Hamiltonians.
# Moreover, it implements multiplication of the Hamiltonian by any number.
#
# .. important::
#     For summation and subtraction the Hamiltonians shall be defined on the same cell
#     and atoms.
#
# .. hint::
#
#     To get an independent instance of spin Hamiltonian with the same cell, atoms and
#     convention, but with no parameters you can use
#     :py:meth:`magnopy.SpinHamiltonian.get_empty`.
#
# For example, imagine that we want to have isotropic and anisotropic terms of the
# Hamiltonian separately.
#
# First, let us create an empty Hamiltonian with the same cell, atoms and convention
# for each term.

aniso_term = spinham.get_empty()
iso_term = spinham.get_empty()

# %%
# Then we add isotropic exchange to the first one and anisotropy to the second one
#
# .. note::
#     Parameters for (0, 0, 0) -> (1, 0, 0) bond and (0, 0, 0)-> (-1, 0, 0) bond are
#     connected via multiple counting. Therefore, when one of them is added, addition of
#     the second one will raise an error. Same problem will appear if we try to add
#     (0, 0, 0) -> (1, 0, 0) bond twice.
#
#     This happens because magnopy always stores only one of the equivalent bonds
#     internally, thus by adding the second parameter we essentially are trying to add
#     the parameter to the same bond again. In other words, the same problem appears if we
#     try to add (0, 0, 0) -> (1, 0, 0) bond twice.
#
#     When the parameter is added to the same bond again, magnopy raises an error by
#     default. There are a number of strategies on how magnopy can handle such situations
#     without raising an error. They are controlled with ``when_present`` argument, that
#     is present in all ``spinham.add_*`` methods. Here we use ``when_present="skip"``,
#     which means that repeated parameters are safely skipped without raising an error.
#     See :py:meth:`magnopy.SpinHamiltonian.add_22` for more options for ``when_present``
#     argument.

for alpha, parameter in spinham.p21:
    aniso_term.add_21(alpha=alpha, parameter=parameter)

for alpha, beta, nu, parameter in spinham.p22:
    iso_term.add_22(
        alpha=alpha, beta=beta, nu=nu, parameter=parameter, when_present="skip"
    )

# %%
#
# Now full Hamiltonian can be computed as simple as

full_spinham = aniso_term + iso_term

# %%
#
# Moreover, we can define new term - antisymmetric Dzyaloshinskii–Moriya interaction.


dmi_term = iso_term.get_empty()

dmi_term.add_22(
    alpha=0,
    beta=0,
    nu=(0, 1, 0),
    parameter=magnopy.converter22.from_dmi(dmi=(0.5, 0, 0)),
)

full_spinham = iso_term + aniso_term + dmi_term

# %%
# Visualizing
# ===========
#
# .. note::
#
#     This functionality of magnopy is still experimental.
#
# One can visualize on-site (involves one site) and two-spin/two-sites parameters using
# :py:func:`magnopy.experimental.plot_spinham`

pe1, pe2 = magnopy.experimental.plot_spinham(
    full_spinham, distance_digits=3, _sphinx_gallery_fix=True
)

# %%
# This function returns two instances of :py:class:`magnopy.PlotlyEngine`. First (``pe1``)
# with the on-site parameters
#
# .. hint::
#     Hover over the magnetic cites to see the values of parameters.
#
#     Click on the legend to hide some of the elements.

pe1.show(axes_visible=False)

# %%
# Adn second (``pe2``) one with all the exchange bonds. DMI vectors are displayed as well.
#
# .. hint::
#     Double-click on some element of the legend to hide all other ones.

pe2.show(axes_visible=False, legend_position="left")


# sphinx_gallery_thumbnail_path = 'img/cat-numbers/3.png'
