r"""
Crystal structure
*****************

.. admonition:: Tutorial tasks

    *   Create a crystal structure for the material of your choosing.
        Create a cell and a set of atoms. Specify all mentioned properties for each atom.
    *   (extra) Visualize your structure using :external:py:class:`magnopy.PlotlyBackend`

Cell and atoms
==============

At the heart of every spin Hamiltonian lies some crystal structure that defined the unit
cell of the lattice and set of magnetic sites.

Unit cell is simply a set of three vectors, that define the basis of the crystal. Magnopy
stores it in the same way as |wulfric|_ and as many other Python codes

.. code-block:: python

    cell = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
    ]

To read more about the cell see |magnopy-cell|_.

Magnopy calls magnetic centers ``atoms`` due to historical reasons, but they are not
necessary atoms. We will use the term atoms in this tutorial. In all cases the atoms will
simply mean an object that has a set of properties defined

*   Name.

    A label of the magnetic center. If magnetic center coincides with an actual atom
    of the crystal, then it is a good idea to include atom's type in its name (i. e.
    ``"Cr1"`` or ``"I_000"``).

*   Position.

    Three numbers that define position of the atom in the basis of the unit cell.

*   Spin.

    Spin value of the magnetic center. Please note that this is a single number.
    The direction of the spin vector or the local quantization axis is put aside of the
    crystal as it may be varied.

*   g-factor.

    Proportionality coefficient for the Zeeman term.

Now, magnopy stores and understand a *set* of atoms (even if there is only one atom in the set).
It store them as a dictionary, for example

.. code-block:: python

    atoms = {
        "names": ["Cr1", "I1", "I2"],
        "positions" : [[0.0, 0.0 ,0.0], [0.5, 0.0, 0.0], [0.0, 0.5, 0.0 ]],
        "spins" : [1.5, None, None],
        "g-factor" : [2, None, None],

    }

To read more about atoms see |magnopy-atoms|_.


Visualization
=============

Magnopy relies on |wulfric|_ for all manipulations with the crystal. In fact, the
visualization engine of magnopy (:external:py:class:`magnopy.PlotlyEngine`) is an
extension of wulfric's visualization engine (:external:py:class:`wulfric.PlotlyEngine`).
They both operate in the same way, the only difference is that magnopy's one have extra
methods for plotting spin Hamiltonian and spin directions.

The recommended scenario for using this kind of visualization is

*   Create an instance of visualization backend

    .. code-block:: python

        pe = magnopy.PlotlyEngine()

*   Plot what you want. See API reference for the list of available plotting methods:
    :external:py:class:`magnopy.PlotlyEngine`.

*   Display the figure

    .. code-block:: python

        pe.show(width=1000, height=1000)
"""

# sphinx_gallery_thumbnail_path = 'img/gallery-thumbnails/trilmax-2025/python-library/crystal.png'
