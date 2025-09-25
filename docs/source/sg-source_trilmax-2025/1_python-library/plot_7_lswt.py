r"""
Linear Spin Wave theory
***********************

.. admonition:: Tutorial tasks

    * Use one of the spin Hamiltonians from the previous tutorial and compute all terms \
      of the magnon Hamiltonian.
    * Compute magnon dispersion of a simple ferromagnet.
    * Compute magnon dispersion of a simple antiferromagnetic.

All methods of linear spin-wave theory are grouped under the
:external:py:class:`magnopy.LSWT` class.

To create it one need two things

* Spin Hamiltonian
* Directions of spins in the ground state
"""

import numpy as np
import magnopy

spinham = magnopy.examples.cubic_ferro_nn(S=1, J_21=(0, 0, -0.5))

lswt = magnopy.LSWT(spinham=spinham, spin_directions=[[0, 0, 1]])

# %%
# Once created it can be used to compute parts of the magnon Hamiltonian
#
# Correction to the classical energy
# ==================================

print(lswt.E_2)

# %%
# Coefficients of the one-operator terms
# ======================================

print(lswt.O)

# %%
# Magnon energies
# ===============

print(lswt.omega(k=[0, 0, 0]))

# %%
# Parallelization
# ===============
#
# Typically one wants to compute magnon energies for a set of k-points. Often for a
# rather large set of k-points. Magnopy offers simple interface to parallelize the
# calculations over the k-points using multiprocessing. See
# :external:py:func:`magnopy.multiprocess_over_k` for details.
# For example, to compute magnon energies for the set of k-points (that are given as
# absolute coordinates in reciprocal space) using two processes use


kpoints = np.linspace([0, 0, 0], [1, 0, 0], 1000)

results = magnopy.multiprocess_over_k(
    kpoints=kpoints,
    relative=False,
    function=lswt.omega,
    number_processors=2,
)


# %%
# Note that ``results[i]`` is equivalent to ``lswt.omega(k=kpoints[i], relative=False)``.

print(results[42])

print(lswt.omega(k=kpoints[42], relative=False))


# sphinx_gallery_thumbnail_path = 'img/cat-numbers/7.png'
