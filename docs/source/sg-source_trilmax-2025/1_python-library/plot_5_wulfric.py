r"""
(extra) K-points with wulfric
*****************************


.. admonition:: Tutorial tasks

    * Get kpoints for future dispersion calculations with |wulfric|_.
    * (extra) Visualize Brillouin zone, k-points and k-path with
      :external:py:class:`wulfric.PlotlyEngine`.
    * (extra) Create a crystal on |wulfric-FCC|_ lattice with |wulfric|_. Visualize and
      compare primitive and conventional cells. Compute k-points, k-path, reciprocal cell
      of conventional cell, reciprocal cell of primitive cell and
      ``wulfric.Kpoints.rcell``.


One way to get a set of k-points and a k-path in reciprocal space is to use |wulfric|_
package.

We recommend to use its :external:py:class:`wulfric.Kpoints` interface. Here we provide
not the most straightforward way to interact with it, but one that give access
for more information. Note that symmetry search in wulfric is powered by |spglib|_.

Wulfric operates on the crystal structure. First we will get the information
from |spglib|_ via wulfric's interface to it.

.. code-block:: python

    spglib_data = wulfric.get_spglib_data(
        cell=spinham.cell,
        atoms = spinham.atoms,
    )

Now one can get the information about the space group or Bravais lattice type

.. code-block:: python

    print(spglib_data.space_group_number)
    print(spglib_data.crystal_family + spglib_data.centring_type)

Now we can create an instance of :external:py:class:`wulfric.Kpoints` class with one of
the implemented |wulfric-conventions|_ for the automatic choice of the high-symmetry
points and k-path.

.. code-block:: python

    kp_sc = wulfric.Kpoints.from_crystal(
        cell = spinham.cell,
        atoms = spinham.atoms,
        spglib_data=spglib_data,
        convention="SC",
    )

    kp_hpkot = wulfric.Kpoints.from_crystal(
        cell = spinham.cell,
        atoms = spinham.atoms,
        spglib_data=spglib_data,
        convention="HPKOT",
    )

    # Default convention is HPKOT
    kp = wulfric.Kpoints.from_crystal(
        cell = spinham.cell,
        atoms = spinham.atoms,
        spglib_data=spglib_data,
    )

Now those objects provide a simple interface

*   For calculations (:external:py:meth:`wulfric.Kpoints.points`)

    .. code-block:: python

        omegas = [lswt.omega(k=kpoint) for kpoint in kp.points()]

*   And for plotting

    .. code-block:: python

        import matplotlib.pyplot as plt

        _, ax = plt.subplots()

        ax.plot(kp.flat_points(), omegas)

        ax.set_xticks(kp.ticks(), kp.labels)

        ax.vlines(kp.ticks(), transform=ax.get_xaxis_tranform(), color="grey", lw=0.5)

        plt.show()
        plt.close()
"""

# sphinx_gallery_thumbnail_path = 'img/gallery-thumbnails/trilmax-2025/python-library/wulfric.png'
