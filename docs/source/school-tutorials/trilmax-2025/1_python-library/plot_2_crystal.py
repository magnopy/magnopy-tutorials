r"""
Crystal structure
*****************

.. admonition:: Tutorial tasks

    *   Create a crystal structure for the material of your choice. Create a cell and a
        set of atoms. For each atom specify all properties mentioned on this page.
    *   (extra) Visualize created structure using :py:class:`magnopy.PlotlyEngine`
    *   (extra) Compute conventional and primitive cell of your structure (see
        :py:func:`wulfric.crystal.get_primitive` and
        :py:func:`wulfric.crystal.get_conventional`). Visualize them. Are they the same?
        Is it true for all crystals?

Cell and atoms
==============

There is a crystal structure at the heart of every spin Hamiltonian. It defines the unit
cell of the lattice and set of magnetic sites.

Unit cell is simply a set of three vectors. Magnopy stores it in the same way as
|wulfric|_ and many other Python codes do
"""

import magnopy

cell = [
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
]

# %%
# To read more about the cell see |magnopy-cell|_.
#
# Magnopy calls magnetic centers "atoms" due to historical reasons, but they are not
# necessary atoms. We will use the term "atoms" in this tutorial. In all cases "atoms"
# simply mean an object that has a set of properties
#
# *   Name.
#
#     A label of the magnetic center. If magnetic center coincides with an actual atom
#     of the crystal, then it is a good idea to include atom's type in its name (i. e.
#     ``"Cr1"`` or ``"I_000"``).
#
# *   Position.
#
#     Three numbers that define position of the atom in the basis of the unit cell. I. e.
#     relative position (can also be called "fractional").
#
# *   Spin.
#
#     Spin value of the magnetic center. Please note that this is a single number.
#
# *   g-factor.
#
#     Proportionality coefficient for the Zeeman term.
#
# Magnopy always uses a *set* of atoms (even if there is only one atom in the set). It
# stores them as a dictionary, for example


atoms = {
    "names": ["Cr1", "I1", "I2"],
    "positions": [[0.0, 0.0, 0.0], [0.5, 0.0, 0.0], [0.0, 0.5, 0.0]],
    "spins": [1.5, None, None],
    "g_factors": [2, None, None],
}

# %%
# Read more about atoms on the |magnopy-atoms|_.
#
# Visualization
# =============
#
# Magnopy relies on |wulfric|_ for all manipulations with the crystal. In fact, the
# visualization engine of magnopy (:py:class:`magnopy.PlotlyEngine`) is an extension of
# wulfric's visualization engine (:py:class:`wulfric.PlotlyEngine`). Both operate in the
# same way, the only difference is that magnopy's engine offers extra methods.
#
# There is a recommended scenario for using this kind of visualization. First, one shall
# create an instance of visualization backend

pe = magnopy.PlotlyEngine(_sphinx_gallery_fix=True)

# %%
#
# .. note::
#    Please ignore ``_sphinx_gallery_fix=True`` and do not include this argument in you
#    scripts.
#
# Then, plot what you want to plot. See API reference for the list of available plotting
# methods -  :py:class:`magnopy.PlotlyEngine`. For example, to display the cell
# and atoms

pe.plot_cell(cell, legend_label="Unit cell", color="Black")
pe.plot_atoms(cell, atoms, legend_label="Atoms of the unit cell")

# %%
# Finally, display or save the figure
#
# .. hint::
#     Figures are interactive. Try to rotate it. Try to zoom in/out. Try to click on the
#     elements of the legend.

pe.show(axes_visible=False)

# sphinx_gallery_thumbnail_path = 'img/cat-numbers/2.png'
