r"""
(extra) Wulfric
***************

.. include:: ../../exercises/7.inc
"""

import numpy as np
import wulfric

# %%
#
# Before moving on to the examples we define two plotting routines, that will be useful
# for us later


def plot_real_space_cells(cell, atoms, conv_cell, conv_atoms, prim_cell, prim_atoms):
    pe = wulfric.PlotlyEngine(_sphinx_gallery_fix=True)

    pe.plot_cell(cell=cell, legend_label="Original cell", color="#000000")
    pe.plot_atoms(
        cell=cell,
        atoms=atoms,
        legend_label="Original atoms",
        colors=["#000000" for _ in atoms["names"]],
    )

    pe.plot_cell(cell=conv_cell, legend_label="Conventional cell", color="#0057B7")
    pe.plot_atoms(
        cell=conv_cell,
        atoms=conv_atoms,
        legend_label="Conventional atoms",
        colors=["#0057B7" for _ in conv_atoms["names"]],
    )

    pe.plot_cell(cell=prim_cell, legend_label="Primitive cell", color="#FFDD00")
    pe.plot_atoms(
        cell=prim_cell,
        atoms=prim_atoms,
        legend_label="Primitive atoms",
        colors=["#FFDD00" for _ in prim_atoms["names"]],
    )
    return pe


def plot_k_points(kp, cell, prim_cell):
    kp_of_input_cell = wulfric.Kpoints.from_crystal(
        cell=cell, atoms=dict(spglib_types=[1], positions=[[0, 0, 0]])
    )

    pe = wulfric.PlotlyEngine(_sphinx_gallery_fix=True)

    pe.plot_kpoints(
        kp, color="#C8102E", legend_label="High-symmetry points (crystal-based)"
    )
    pe.plot_kpath(
        kp, color="#C8102E", legend_label="Recommended k-path (crystal-based)"
    )
    pe.plot_brillouin_zone(
        cell=prim_cell,
        color="#C8102E",
        legend_label="Brillouin zone of the primitive cell",
    )

    pe.plot_kpoints(
        kp_of_input_cell,
        color="#003DA5",
        legend_label="High-symmetry points (cell-based)",
    )
    pe.plot_kpath(
        kp_of_input_cell,
        color="#003DA5",
        legend_label="Recommended k-path (cell-based)",
    )
    pe.plot_brillouin_zone(
        cell=cell,
        color="#003DA5",
        legend_label="Brillouin zone of the input cell",
    )
    return pe


# %%
#
# Exercise 1
# ==========
#
# Simplest example is a cubic cell with a single atom at the origin. We will show another
# one - a hexagonal cell with two atoms.

# Create a crystal
cell = np.array(
    [
        [1.0, 0.0, 0.0],
        [-0.5, np.sqrt(3) / 2, 0.0],
        [0.0, 0.0, 2.0],
    ]
)

atoms = dict(
    names=["Cr", "Br", "Br"],
    positions=[[0.0, 0.0, 0.5], [1 / 3, 2 / 3, 0.25], [2 / 3, 1 / 3, 0.75]],
    spins=[3 / 2, None, None],
    g_factors=[2.0, None, None],
)

# %%
#
# Use |wulfric|_ to analyse the crystal symmetry and compute conventional and primitive
# cells.

spglib_data = wulfric.get_spglib_data(cell=cell, atoms=atoms)

print(f"Space group: {spglib_data.space_group_number}")
print(f"Bravais lattice: {spglib_data.crystal_family + spglib_data.centring_type}")

# Compute conventional and primitive cells
conv_cell, conv_atoms = wulfric.crystal.get_conventional(
    cell=cell, atoms=atoms, spglib_data=spglib_data, convention="HPKOT"
)

prim_cell, prim_atoms = wulfric.crystal.get_primitive(
    cell=cell, atoms=atoms, spglib_data=spglib_data, convention="HPKOT"
)

# %%
#
# Then, we visualize and compare real-space cells

# Visualize real-space cells
pe = plot_real_space_cells(
    cell=cell,
    atoms=atoms,
    conv_cell=conv_cell,
    conv_atoms=conv_atoms,
    prim_cell=prim_cell,
    prim_atoms=prim_atoms,
)

pe.show(axes_visible=False, legend_position="left")

# %%
#
# Finally, we compute high-symmetry k-points and k-path for the given crystal.

kp = wulfric.Kpoints.from_crystal(cell=cell, atoms=atoms)

print(f"Recommended k-path: {kp.path_string}")

pe = plot_k_points(kp=kp, cell=cell, prim_cell=prim_cell)

pe.show(axes_visible=False, legend_position="left")


# %%
#
# Exercise 2
# ==========
#
# Simplest example will be a supercell of any given cell. We will show another one,
# with one atom per unit cell.

# Create a crystal
cell = np.array(
    [
        [1.0, 0.0, 0.0],
        [1, 1, 0.0],
        [0.0, 0.0, 1.0],
    ]
)

atoms = dict(
    names=["Fe"],
    positions=[[0.0, 0.0, 0.0]],
    spins=[5 / 2],
    g_factors=[2.0],
)

# %%
#
# Use |wulfric|_ to analyse the crystal symmetry and compute conventional and primitive
# cells.

spglib_data = wulfric.get_spglib_data(cell=cell, atoms=atoms)

print(f"Space group: {spglib_data.space_group_number}")
print(f"Bravais lattice: {spglib_data.crystal_family + spglib_data.centring_type}")

# Compute conventional and primitive cells
conv_cell, conv_atoms = wulfric.crystal.get_conventional(
    cell=cell, atoms=atoms, spglib_data=spglib_data, convention="HPKOT"
)

prim_cell, prim_atoms = wulfric.crystal.get_primitive(
    cell=cell, atoms=atoms, spglib_data=spglib_data, convention="HPKOT"
)

# %%
#
# Then, we visualize and compare real-space cells

# Visualize real-space cells
pe = plot_real_space_cells(
    cell=cell,
    atoms=atoms,
    conv_cell=conv_cell,
    conv_atoms=conv_atoms,
    prim_cell=prim_cell,
    prim_atoms=prim_atoms,
)

pe.show(axes_visible=False, legend_position="left")

# %%
#
# Finally, we compute high-symmetry k-points and k-path for the given crystal.

kp = wulfric.Kpoints.from_crystal(cell=cell, atoms=atoms)

print(f"Recommended k-path: {kp.path_string}")

pe = plot_k_points(kp=kp, cell=cell, prim_cell=prim_cell)

pe.show(axes_visible=False, legend_position="left")

# %%
#
# .. note::
#
#     Even though the input cell and primitive cell are different, they both contain one
#     lattice point per cell, therefore they span the same real-space and reciprocal space
#     lattices. As a result, they have the same Brillouin zones.
#
# Exercise 3
# ==========

# Get a cubic cell with a = 4
cell = 4 * np.eye(3)

# Eight atoms: four will be magnetic, and four will not
atoms = dict(
    names=["Fe1", "Fe2", "Fe3", "Fe4", "O1", "O2", "O3", "O4"],
    positions=[
        [0.0, 0.0, 0.0],
        [0.5, 0.5, 0.0],
        [0.0, 0.5, 0.5],
        [0.5, 0.0, 0.5],
        [0.5, 0.5, 0.5],
        [0.5, 0.0, 0.0],
        [0.0, 0.5, 0.0],
        [0.0, 0.0, 0.5],
    ],
    spins=[2.5, 2.5, 2.5, 2.5, None, None, None, None],
    g_factors=[2, 2, 2, 2, None, None, None, None],
)

# Get spglib data for the original cell
spglib_data = wulfric.get_spglib_data(cell=cell, atoms=atoms)


# Make a supercell
super_cell = cell @ np.diag([2, 3, 1])

# Generate atoms of the super-cell
super_atoms = {}
for key in atoms:
    super_atoms[key] = []

for i in range(2):
    for j in range(3):
        for name, pos, spin, g_factor in zip(
            atoms["names"], atoms["positions"], atoms["spins"], atoms["g_factors"]
        ):
            super_atoms["names"].append(name)
            super_pos = [
                (pos[0] + i) / 2,
                (pos[1] + j) / 3,
                pos[2] / 1,
            ]
            super_atoms["positions"].append(super_pos)
            super_atoms["spins"].append(spin)
            super_atoms["g_factors"].append(g_factor)

# Get spglib data for the super-cell
super_spglib_data = wulfric.get_spglib_data(cell=super_cell, atoms=super_atoms)


# %%
#
# Visualize original cell and supercell in real space
pe = wulfric.PlotlyEngine(_sphinx_gallery_fix=True)

pe.plot_cell(cell=cell, legend_label="Original cell", color="#000000")
pe.plot_atoms(
    cell=cell,
    atoms=atoms,
    legend_label="Original atoms",
    colors=["#000000" for _ in atoms["names"]],
)

pe.plot_cell(cell=super_cell, legend_label="Super-cell", color="#0057B7")
pe.plot_atoms(
    cell=super_cell,
    atoms=super_atoms,
    legend_label="Atoms of the super-cell",
    colors=["#0057B7" for _ in super_atoms["names"]],
)
pe.show(axes_visible=False, legend_position="left")

# %%
#
# There are only two types of atoms in the super-cell, therefore original cell and
# super-cell generate the same crystal.

print(spglib_data.original_types)
print(super_spglib_data.original_types)

# %%
#
# Original cell and super-cell are of the same space group

print(f"Original cell space group: {spglib_data.space_group_number}")
print(
    f"Original cell Bravais lattice: {spglib_data.crystal_family + spglib_data.centring_type}"
)
print(f"Super-cell space group: {super_spglib_data.space_group_number}")
print(
    f"Super-cell Bravais lattice: {super_spglib_data.crystal_family + super_spglib_data.centring_type}"
)

# %%
#
# They have the same primitive cell

prim_cell, _ = wulfric.crystal.get_primitive(
    cell=cell, atoms=atoms, convention="HPKOT", spglib_data=spglib_data
)
super_prim_cell, _ = wulfric.crystal.get_primitive(
    cell=super_cell,
    atoms=super_atoms,
    convention="HPKOT",
    spglib_data=super_spglib_data,
)

print(f"Primitive cells are the same? {np.allclose(prim_cell, super_prim_cell)}")

# %%
#
# They have the same high-symmetry k-points and k-path

kp = wulfric.Kpoints.from_crystal(cell=cell, atoms=atoms, spglib_data=spglib_data)
super_kp = wulfric.Kpoints.from_crystal(
    cell=super_cell, atoms=super_atoms, spglib_data=super_spglib_data
)

print(f"Recommended k-path for the original cell: {kp.path_string}")
print(f"Recommended k-path for the super-cell: {super_kp.path_string}")

pe = wulfric.PlotlyEngine(_sphinx_gallery_fix=True)

pe.plot_kpoints(
    kp, color="#C8102E", legend_label="High-symmetry points (original cell)"
)
pe.plot_kpath(kp, color="#C8102E", legend_label="Recommended k-path (original cell)")
pe.plot_brillouin_zone(
    cell=cell,
    color="#C8102E",
    legend_label="Brillouin zone of the original cell",
)

pe.plot_kpoints(
    super_kp, color="#003DA5", legend_label="High-symmetry points (super-cell)"
)
pe.plot_kpath(super_kp, color="#003DA5", legend_label="Recommended k-path (super-cell)")
pe.plot_brillouin_zone(
    cell=super_cell,
    color="#003DA5",
    legend_label="Brillouin zone of the super-cell",
)

pe.plot_brillouin_zone(
    cell=prim_cell,
    color="#00A86B",
    legend_label="Brillouin zone of the primitive cell",
)

pe.show(axes_visible=False, legend_position="left")


# %%
#
# Exercise 4
# ==========
#
# We re-use the super-cell from the previous exercise

# Change spglib_types of all atoms to reflect sub-cells of the super-cell
new_types = [1, 1, 1, 1, 2, 2, 2, 2]  # original types for the 8 atoms
for i in range(1, 6):  # 6 sub-cells in the super-cell
    new_types += [
        1 + 2 * i,
        1 + 2 * i,
        1 + 2 * i,
        1 + 2 * i,
        2 + 2 * i,
        2 + 2 * i,
        2 + 2 * i,
        2 + 2 * i,
    ]

super_atoms["spglib_types"] = new_types

print("spglib_types from exercise 3 -> spglib_types for exercise 4")
for ex_3_type, ex_4_type in zip(
    super_spglib_data.original_types, super_atoms["spglib_types"]
):
    print(f"{ex_3_type:3} -> {ex_4_type}")

# Re-compute spglib data for the super-cell
super_spglib_data = wulfric.get_spglib_data(cell=super_cell, atoms=super_atoms)

# %%
#
# Now original cell and supercell essentially describe different crystals. They have
# different space groups.

print(f"Original cell space group: {spglib_data.space_group_number}")
print(
    f"Original cell Bravais lattice: {spglib_data.crystal_family + spglib_data.centring_type}"
)
print(f"Super-cell space group: {super_spglib_data.space_group_number}")
print(
    f"Super-cell Bravais lattice: {super_spglib_data.crystal_family + super_spglib_data.centring_type}"
)

# %%
#
# They have different primitive cells
prim_cell, _ = wulfric.crystal.get_primitive(
    cell=cell, atoms=atoms, convention="HPKOT", spglib_data=spglib_data
)
super_prim_cell, _ = wulfric.crystal.get_primitive(
    cell=super_cell,
    atoms=super_atoms,
    convention="HPKOT",
    spglib_data=super_spglib_data,
)

print(f"Primitive cells are the same? {np.allclose(prim_cell, super_prim_cell)}")

# %%
#
# They have different high-symmetry k-points and k-path

kp = wulfric.Kpoints.from_crystal(cell=cell, atoms=atoms, spglib_data=spglib_data)
super_kp = wulfric.Kpoints.from_crystal(
    cell=super_cell, atoms=super_atoms, spglib_data=super_spglib_data
)

print(f"Recommended k-path for the original cell: {kp.path_string}")
print(f"Recommended k-path for the super-cell: {super_kp.path_string}")

pe = wulfric.PlotlyEngine(_sphinx_gallery_fix=True)

pe.plot_kpoints(
    kp, color="#C8102E", legend_label="High-symmetry points (original cell)"
)
pe.plot_kpath(kp, color="#C8102E", legend_label="Recommended k-path (original cell)")
pe.plot_brillouin_zone(
    cell=cell,
    color="#C8102E",
    legend_label="Brillouin zone of the original cell",
)

pe.plot_kpoints(
    super_kp, color="#003DA5", legend_label="High-symmetry points (super-cell)"
)
pe.plot_kpath(super_kp, color="#003DA5", legend_label="Recommended k-path (super-cell)")
pe.plot_brillouin_zone(
    cell=super_cell,
    color="#003DA5",
    legend_label="Brillouin zone of the super-cell",
)

pe.show(axes_visible=False, legend_position="left")


# sphinx_gallery_thumbnail_path = 'img/cat-numbers/7.png'
