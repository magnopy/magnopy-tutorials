r"""
Classical Energy
****************

.. include:: ../../exercises/6.inc


Classical energy of the spin Hamiltonian is implemented in a separate class.
"""

import magnopy

# Get an example of the ferromagnet on a cubic lattice, with an easy axis
spinham = magnopy.examples.cubic_ferro_nn(S=1, J_iso=1, J_21=[0, 0, -0.1])

# Create an instance of the energy class
energy = magnopy.Energy(spinham=spinham)

# %%
# Now this object can be used to compute the energy for some set of spin directions
#
# .. note::
#
#     By default energy is returned in meV.

print(f" Energy with spin along x axis: {energy(spin_directions=[[1, 0, 0]]):.4f} meV")
print(f" Energy with spin along y axis: {energy(spin_directions=[[0, 1, 0]]):.4f} meV")
print(f" Energy with spin along z axis: {energy(spin_directions=[[0, 0, 1]]):.4f} meV")

# %%
#
# Energy optimization
# ===================
# Magnopy implements numerical minimization of classical energy, by varying spin
# directions of all magnetic centers in the unit cell on a sphere [1]_. A local minima can be
# found in that way.

optimized_sd = energy.optimize()
print(
    f"Optimized spin directions are\n{optimized_sd}\nwith the energy of {energy(optimized_sd)} meV"
)

# %%
# see :py:class:`magnopy.Energy` for more details.
#
# References
# ==========
#
# .. [1] Ivanov, A.V., Uzdin, V.M. and Jónsson, H., 2021.
#     Fast and robust algorithm for energy minimization of spin systems applied
#     in an analysis of high temperature spin configurations in terms of skyrmion
#     density.
#     Computer Physics Communications, 260, p.107749.


# sphinx_gallery_thumbnail_path = 'img/cat-numbers/6.png'
