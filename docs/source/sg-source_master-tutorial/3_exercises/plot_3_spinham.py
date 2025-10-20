r"""
Spin Hamiltonian
****************

.. include:: ../../exercises/3.inc

"""

import numpy as np
import magnopy

# %%
#
# Exercise 1
# ==========

# Cubic cell with a = 1
cell = np.eye(3)

# One atom per unit cell
# located in the center of the unit cell
atoms = dict(
    names=["Fe"],
    positions=[[0.5, 0.5, 0.5]],
    spins=[2.5],
    g_factors=[2],
)

# Choose convention
convention = magnopy.Convention(multiple_counting=True, spin_normalized=False, c22=1)

# Create a Hamiltonian
spinham = magnopy.SpinHamiltonian(cell=cell, atoms=atoms, convention=convention)

# Add nearest neighbor parameter
# Choose 1D chain along the first lattice vector
parameter = magnopy.converter22.from_iso(iso=1)
spinham.add_22(alpha=0, beta=0, nu=(1, 0, 0), parameter=parameter)

# Add next-nearest neighbor parameter of opposite sign and slightly smaller absolute value
spinham.add_22(alpha=0, beta=0, nu=(2, 0, 0), parameter=-0.95 * parameter)

_, pe2 = magnopy.experimental.plot_spinham(spinham=spinham, _sphinx_gallery_fix=True)

pe2.show(axes_visible=False, legend_position="left")

# %%
#
# Exercise 2
# ==========

# Create two modified conventions

mod_conv_1 = convention.get_modified(multiple_counting=False)
mod_conv_2 = convention.get_modified(c22=-1)

# %%
#
# First, display the parameters in the original convention: they have the same values as
# the one we passed to :py:meth:`magnopy.SpinHamiltonian.add_22` function

for alpha, beta, nu, parameter in spinham.p22:
    print(
        f"{spinham.atoms.names[alpha]} -> {spinham.atoms.names[beta]} at {nu}\n{parameter}"
    )

# %%
#
# Next we disable multiple counting. As there are twice as less parameters in the
# Hamiltonian in the new convention, then values of the parameters shall be two times
# larger to preserve physical properties of the model (for example classical energy).

spinham.convention = mod_conv_1

for alpha, beta, nu, parameter in spinham.p22:
    print(
        f"{spinham.atoms.names[alpha]} -> {spinham.atoms.names[beta]} at {nu}\n{parameter}"
    )

# %%
#
# Finally, we change the sign in from of the two spins & two sites term. The parameter
# shall change their sign to preserve physical properties of the model.

spinham.convention = mod_conv_2

for alpha, beta, nu, parameter in spinham.p22:
    print(
        f"{spinham.atoms.names[alpha]} -> {spinham.atoms.names[beta]} at {nu}\n{parameter}"
    )

# sphinx_gallery_thumbnail_path = 'img/cat-numbers/3.png'
