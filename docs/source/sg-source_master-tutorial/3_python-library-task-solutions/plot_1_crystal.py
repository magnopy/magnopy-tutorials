r"""
Crystal structure
*****************

.. include:: ../../exercises/1.inc

We will use the fictitious crystal with the lattice vectors

* :math:`\boldsymbol{a}_1 = (5, 0, 0)`
* :math:`\boldsymbol{a}_2 = (0, 5, 0)`
* :math:`\boldsymbol{a}_3 = (0, 0, 5)`

and a set of eight atoms

* "Fe1" at (0, 0, 0) with spin value 5/2 and g-factor 2.
* "Fe2" at (0.5, 0.5, 0) with spin value 5/2 and g-factor 2.
* "Fe3" at (0, 0.5, 0.5) with spin value 5/2 and g-factor 2.
* "Fe4" at (0.5, 0, 0.5) with spin value 5/2 and g-factor 2.
* "O1" at (0.5, 0, 0) with undefined spin value and g-factor.
* "O2" at (0, 0.5, 0) with undefined spin value and g-factor.
* "O3" at (0, 0, 0.5) with undefined spin value and g-factor.
* "O4" at (0.5, 0.5, 0.5) with undefined spin value and g-factor.
"""

import magnopy
import wulfric

# %%
#
# Exercise 1
# ==========
#
# Simple syntax
# -------------

# Create a unit cell
cell = [
    [5.0, 0.0, 0.0],
    [0.0, 5.0, 0.0],
    [0.0, 0.0, 5.0],
]

# Create a set of atoms
atoms = {
    "names": ["Fe1", "Fe2", "Fe3", "Fe4", "O1", "O2", "O3", "O4"],
    "positions": [
        [0.0, 0.0, 0.0],
        [0.5, 0.5, 0.0],
        [0.0, 0.5, 0.5],
        [0.5, 0.0, 0.5],
        [0.5, 0.0, 0.0],
        [0.0, 0.5, 0.0],
        [0.0, 0.0, 0.5],
        [0.5, 0.5, 0.5],
    ],
    "spins": [5 / 2, 5 / 2, 5 / 2, 5 / 2, None, None, None, None],
    "g_factors": [2, 2, 2, 2, None, None, None, None],
}

# Display properties of each atom
for i in range(8):
    name = atoms["names"][i]
    position = atoms["positions"][i]
    spin = atoms["spins"][i]
    g_factor = atoms["g_factors"][i]

    if spin is None:
        spin = "None"
    if g_factor is None:
        g_factor = "None"

    print(f"Atom '{name}' at {position} with spin value {spin} and g-factor {g_factor}")

# %%
#
# Advanced syntax
# ---------------

# Create a unit cell
cell = [
    [5.0, 0.0, 0.0],
    [0.0, 5.0, 0.0],
    [0.0, 0.0, 5.0],
]

# Create a set of atoms
atoms = {
    "names": [f"Fe{_ + 1}" for _ in range(4)] + [f"O{_ + 1}" for _ in range(4)],
    "positions": [
        [0.0, 0.0, 0.0],
        [0.5, 0.5, 0.0],
        [0.0, 0.5, 0.5],
        [0.5, 0.0, 0.5],
        [0.5, 0.0, 0.0],
        [0.0, 0.5, 0.0],
        [0.0, 0.0, 0.5],
        [0.5, 0.5, 0.5],
    ],
    "spins": [5 / 2 for _ in range(4)] + [None for _ in range(4)],
    "g_factors": [2 for _ in range(4)] + [None for _ in range(4)],
}

# Display properties of each atom
for name, position, spin, g_factor in zip(
    atoms["names"], atoms["positions"], atoms["spins"], atoms["g_factors"]
):
    if spin is None:
        spin = "None"
    if g_factor is None:
        g_factor = "None"
    print(
        f"Atom {f'"{name}"':>5} at {position} with spin value {spin:>4} and g-factor {g_factor:>2}"
    )

# %%
#
# Exercise 2
# ==========

# Step 1 - create an instance of the engine
# (please ignore _sphinx_gallery_fix)
pe = magnopy.PlotlyEngine(_sphinx_gallery_fix=True)

# Step 2 - plot
pe.plot_cell(cell=cell)
# Note that cell is expected as well, as atom's positions are relative coordinates.
pe.plot_atoms(cell=cell, atoms=atoms)

# Step 3 - show
pe.show()

# %%
#
# Exercise 3
# ==========
#
# Simple approach
# ---------------

# Note: default convention of HPKOT is used
conv_cell, conv_atoms = wulfric.crystal.get_conventional(cell=cell, atoms=atoms)
prim_cell, prim_atoms = wulfric.crystal.get_primitive(cell=cell, atoms=atoms)


# %%
#
# Advanced approach
# -----------------

# Explicitly control what atoms are considered to be the same by spglib
atoms["spglib_types"] = [1, 1, 1, 1, 2, 2, 2, 2]

# Explicitly call spglib via wulfric's interface.
# Both get_conventional() and get_primitive() call spglib internally,
# thus doing double work in the simple approach.
spglib_data = wulfric.get_spglib_data(cell=cell, atoms=atoms, spglib_symprec=1e-5)

# Then use the resultto compute conventional and primitive cell
conv_cell, conv_atoms = wulfric.crystal.get_conventional(
    cell=cell, atoms=atoms, spglib_data=spglib_data
)
prim_cell, prim_atoms = wulfric.crystal.get_primitive(
    cell=cell, atoms=atoms, spglib_data=spglib_data
)

# %%
#
# Plotting
# --------

# Please ignore _sphinx_gallery_fix
pe = magnopy.PlotlyEngine(_sphinx_gallery_fix=True)


pe.plot_cell(cell=cell, legend_label="Original cell", color="#FD4837")
pe.plot_atoms(cell=cell, atoms=atoms, legend_label="Atoms of the original cell")

pe.plot_cell(cell=conv_cell, legend_label="Conventional cell", color="#2F58FE")
pe.plot_atoms(
    cell=conv_cell,
    atoms=conv_atoms,
    legend_label="Atoms of the conventional cell",
    colors=["#2F58FE" for _ in range(8)],
)

pe.plot_cell(cell=prim_cell, legend_label="Primitive cell", color="#0E7634")
pe.plot_atoms(
    cell=prim_cell,
    atoms=prim_atoms,
    legend_label="Atoms of the primitive cell",
    colors=["#0E7634" for _ in range(8)],
)

pe.show(axes_visible=False, legend_position="left")

# %%
#
# No, conventional and primitive cell are not necessarily the same. It will depend on the
# space group of the crystal and on the convention that is used to define conventional and
# primitive cell, see |wulfric-BL|_ for more examples.
#
# Moreover, input unit cell can be different from both conventional and primitive ones
# (consider a super-cell as an input cell, for example).
#
# .. note::
#
#     Space group is detected via |spglib|_. In general, the result depends on what atoms
#     are considered to be equivalent. Magnopy guesses ``spglib_types`` based on the
#     ``atoms["names"]`` via |wulfric|_ (see :py:func:`wulfric.get_spglib_types` to see
#     how exactly the guess is implemented).


# sphinx_gallery_thumbnail_path = 'img/cat-numbers/1.png'
