***********************
Linear Spin Wave theory
***********************

.. admonition:: Tutorial tasks

    * Use some spin Hamiltonian, compute all terms of the magnon Hamiltonian.
    * Compute magnon dispersion of a simple ferromagnet.
    * Compute magnon dispersion of a simple antiferromagnetic.

All methods of linear spin-wave theory are grouped under the 
:external:py:class:`magnopy.LSWT` class.

To create it one need two things

* Spin Hamiltonian
* Directions of spins in the ground state

.. code-block:: python

    lswt = magnopy.LSWT(
        spinham = spinham,
        spin_directions = [[0, 0, 1]]
    )

Once created it can be used to compute parts of the magnon Hamiltonian

Correction to the classical energy
==================================

.. code-block:: python

    print(lswt.E_2)

Coefficients of the one-operator terms
======================================

.. code-block:: python

    print(lswt.O)


Magnon energies
===============

.. code-block:: python

    print(lswt.omega(k=[0, 0, 0]))

Parallelization
===============

Typically one wants to compute magnon energies for a set of k-points. Sometimes for a 
rather large set of k-points. MAgnopy offers simple interface to parallelize the 
calculations over the k-points using multiprocessing. See 
:external:py:func:`magnopy.multiprocess_over_k` for details. 
For example, to compute magnon energies for the set of k-points (that are given as 
absolute coordinates in reciprocal space), using two processors use

.. code-block:: python

    kpoints = np.linspace([0, 0, 0],[1, 0, 0], 1000)

    results = magnopy.multiprocess_over_k(
        kpoints=kpoints,
        relative=False,
        callable=lswt.omega,
        number_processors=2,
    )

Now, the ``results[i]`` is equivalent to ``lswt.omega(k=kpoints[i], relative=False)``.