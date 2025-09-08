r"""
Classical Energy
****************


.. admonition:: Tutorial tasks

    *   Compute classical energy of one of the Hamiltonians from the previous tasks.
    *   Change the convention of the spin Hamiltonian and compute the energy again.
        Does it change?
    *   Use the set of Hamiltonians from :ref:`trilmax-2025_spinham_arithmetics`.
        Optimize the spin direction for the full Hamiltonian. Use them to compute
        energy contributions of every term.
    *   (extra) Create a Hamiltonian of the ferromagnet with an easy magnetic axis.
        Find out numerically the value of the magnetic field that need to be applied
        perpendicular to it in order to fully orient the spins along the magnetic field.

Classical energy of the spin Hamiltonian is implemented in a separate class.
"""

import magnopy

spinham = magnopy.examples.cubic_ferro_nn(S=1, J_21=(-1, 0, 1))

energy = magnopy.Energy(spinham=spinham)

# %%
# Now this object can be used to simply compute the energy for some set of spin directions

print(energy(spin_directions=[[1, 0, 0]]))
print(energy(spin_directions=[[0, 1, 0]]))
print(energy(spin_directions=[[0, 0, 1]]))

# %%
# or to optimize spin directions within unit cell to get the configuration of some local minima

optimized_sd = energy.optimize()

# %%
# see :external:py:class:`magnopy.Energy` for more details.

print(optimized_sd)
print(energy(optimized_sd))


# sphinx_gallery_thumbnail_path = 'img/gallery-thumbnails/trilmax-2025/python-library/energy.png'
