r"""
Magnetic field
**************

.. include:: ../../exercises/4.inc

Magnetic field is an external effect. However, magnopy, perhaps counterintuitively, stores
it as an interaction parameter of the type :py:attr:`magnopy.SpinHamiltonian.p1`, i. e.
one spin and one site parameter.

This is a design choice that we made. It allows us to take care of the magnetic field in
one place (in the Hamiltonian) and treat it on the same grounds as other terms of the
Hamiltonian.

Said that, we defined a convenience method, that convert a vector of the magnetic flux
density into the one spin & one site parameter of the Hamiltonian:
:py:meth:`magnopy.SpinHamiltonian.add_magnetic_field`.

"""

import numpy as np
import magnopy

# %%
#
# For example, to add an external magnetic field directed along the y axis with the value of
# 1.42 Tesla use

# Cubic ferromagnet
cell = np.eye(3)

atoms = dict(
    names=["Fe"],
    positions=[[0.5, 0.5, 0.5]],
    spins=[2.5],
    g_factors=[2],
)

# Choose convention
convention = magnopy.Convention(
    multiple_counting=True, spin_normalized=False, c21=1, c22=1
)

# Create a Hamiltonian
spinham = magnopy.SpinHamiltonian(cell=cell, atoms=atoms, convention=convention)

# Try to add magnetic field
spinham.add_magnetic_field(B=(0.0, 1.42, 0.0))

print(len(spinham.p1))

# %%
#
# Surprisingly no magnetic field has been added. This is a subtle detail in magnopy
# that originates from the |magnopy-mag-vs-nomag|_ problem. In short: magnetic atoms are
# those that already have a parameter (of any group) associated with it. In this example the
# Hamiltonian is empty, thus magnopy considers all atoms to be non-magnetic.
#
# We are left with two choices: either add some other parameters to the model, that will
# make atoms magnetic or explicitly tell magnopy to which atoms we want to add coupling
# with the magnetic field

# Add magnetic field
spinham.add_magnetic_field(B=(0.0, 1.42, 0.0), alphas=[0])

# Now there is one parameter associated with magnetic field
print(len(spinham.p1))

for alpha, parameter in spinham.p1:
    print(
        f'Atom "{spinham.atoms.names[alpha]}" -> {parameter[0]:.5f} {parameter[1]:.5f} {parameter[2]:.5f}'
    )

# %%
#
# Technically, parameters are defined as
#
# ..  math::
#
#     \mathbf{J}_{\alpha} = \dfrac{\mu_B g_{\alpha} \mathbf{B}}{C_1}
#
# where :math:`\mu_B` is Bohr magneton, :math:`g_{\alpha}` is
# ``spinham.atoms.g_factors[alpha]`` and :math:`C_1` is ``spinham.convention.c1``.

# Bohr magneton in meV / Tesla
mu_B = magnopy.si.BOHR_MAGNETON / (magnopy.si.MILLI * magnopy.si.ELECTRON_VOLT)

print(
    mu_B
    * spinham.atoms.g_factors[0]
    * np.array([0.0, 1.42, 0.0])
    / spinham.convention.c1
)

# sphinx_gallery_thumbnail_path = 'img/cat-numbers/4.png'
