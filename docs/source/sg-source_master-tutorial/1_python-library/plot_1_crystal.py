r"""
Crystal structure
*****************

.. include:: ../../exercises/1.inc

Every spin Hamiltonian in |magnopy|_ is defined on a lattice and a set of magnetic centers
in its unit cell. In other words, one needs to define a crystal structure in order to
define the spin Hamiltonian. This tutorial explains how to do that.

Crystal structure in |magnopy|_ is defined in the same way as in |wulfric|_: a unit cell
with the set of atoms (or "magnetic centers").
"""

import magnopy

# %%
# Cell
# ====
#
# Unit cell is simply a set of three vectors (rows are vectors, i. e. ``a_1 = cell[0]``).
# Read |magnopy-cell|_ for more information.

cell = [
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
]

# %%
#
# Atoms
# =====
#
# Magnopy calls magnetic centers "atoms" due to historical reasons, but they are not
# necessary atoms. We will use the term "atoms" in this tutorial. In all cases "atom"
# simply mean an object with the set of properties. Read |magnopy-atoms|_ for the full
# account of the expected properties and their meaning.
#
# Magnopy operates with a *set* of atoms (even if there is only one atom in the set).
# Atoms are stored as a python dictionary. For example, set of three atoms
#
# * "Cr1" atom located at :math:`(0, 0, 0)` with spin value :math:`1.5` and g-factor
#   :math:`2`.
# * "I1" atom located at :math:`(0.5, 0, 0)` with undefined spin value and g-factor.
# * "I2" atom located at :math:`(0, 0.5, 0)` with undefined spin value and g-factor.
#
# is defined as

atoms = {
    "names": ["Cr1", "I1", "I2"],
    "positions": [[0.0, 0.0, 0.0], [0.5, 0.0, 0.0], [0.0, 0.5, 0.0]],
    "spins": [1.5, None, None],
    "g_factors": [2, None, None],
}

# %%
#
# Visualization
# =============
#
# Magnopy relies on |wulfric|_ for all manipulations with the crystal. In fact,
# visualization engine of magnopy (:py:class:`magnopy.PlotlyEngine`) is an
# extension of wulfric's visualization engine (:py:class:`wulfric.PlotlyEngine`).
#
# There are three steps in using this visualization technique. First, one shall create an
# instance of the visualization backend

pe = magnopy.PlotlyEngine(_sphinx_gallery_fix=True)

# %%
#
# .. note::
#    Please ignore ``_sphinx_gallery_fix=True`` and do not include this argument in you
#    scripts.
#
# Second, plot what you want to plot. See API reference (:py:class:`magnopy.PlotlyEngine`)
# for the list of available plotting methods. For example, display cell with
# :py:meth:`magnopy.PlotlyEngine.plot_cell` and atoms with
# :py:meth:`magnopy.PlotlyEngine.plot_atoms`

pe.plot_cell(cell, legend_label="Unit cell", color="Black")
pe.plot_atoms(cell, atoms, legend_label="Atoms of the unit cell")

# %%
# Finally, display  the figure with :py:meth:`magnopy.PlotlyEngine.show` or save it with
# :py:meth:`magnopy.PlotlyEngine.save`

pe.show(axes_visible=False)

# %%
# .. hint::
#     Figures are interactive. Try to rotate it. Try to zoom in/out. Try to click on the
#     elements of the legend.

# sphinx_gallery_thumbnail_path = 'img/cat-numbers/1.png'
