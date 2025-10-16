r"""
Magnetic field
**************

.. include:: ../../exercises/4.inc
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
convention = magnopy.Convention(
    multiple_counting=True, spin_normalized=False, c1=1, c22=1
)

# Create a Hamiltonian
spinham = magnopy.SpinHamiltonian(cell=cell, atoms=atoms, convention=convention)

# Add nearest neighbor interactions
for nu in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
    spinham.add_22(
        alpha=0, beta=0, nu=nu, parameter=magnopy.converter22.from_iso(iso=-1)
    )

# Add magnetic field along +y of the value 2.432 Tesla
spinham.add_magnetic_field(B=(0, 2.432, 0))


# %%
#
# Exercise 2
# ==========
#
# First we create bae Hamiltonian with no magnetic field present.

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
convention = magnopy.Convention(
    multiple_counting=True, spin_normalized=False, c1=1, c22=1
)

# Create a Hamiltonian
spinham = magnopy.SpinHamiltonian(cell=cell, atoms=atoms, convention=convention)

# Add nearest neighbor interactions
for nu in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
    spinham.add_22(
        alpha=0, beta=0, nu=nu, parameter=magnopy.converter22.from_iso(iso=-1)
    )

# %%
#
# Then we create a Hamiltonian with only magnetic field of the value (0, 0.1, 0)

B_step = spinham.get_empty()

B_step.add_magnetic_field(B=(0, 0.1, 0), alphas=[0])

# %%
#
# Finally, we use arithmetics on spin Hamiltonians to get a list of ten Hamiltonians

spinhams = [spinham + (index + 1) * B_step for index in range(10)]

for spinham in spinhams:
    print(spinham.p1[0])

# sphinx_gallery_thumbnail_path = 'img/cat-numbers/4.png'
