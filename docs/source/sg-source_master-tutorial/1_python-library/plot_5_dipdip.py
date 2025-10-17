r"""
Magnetic dipole-dipole interaction
**********************************

Magnetic dipole-dipole interaction can be written as a two-spin/two-sites parameter.
To save the burden of manual conversion, magnopy has a convenience method
that adds magnetic dipole-dipole interaction to the spin Hamiltonian.

This interaction is of the long range. Magnopy implements its inclusion within the cut-off
value.

.. note::

    Magnetic dipole dipole is added only to magnetic atoms, same as with
    :ref:`sphx_glr_master-tutorial_1_python-library_plot_4_magnetic_field.py`.

"""

import numpy as np
import magnopy

# Cubic ferromagnet
cell = np.eye(3)

atoms = dict(
    names=["Fe"],
    positions=[[0.5, 0.5, 0.5]],
    spins=[2.5],
    g_factors=[2],
)

# Choose convention
convention = magnopy.Convention(
    multiple_counting=True, spin_normalized=False, c21=1, c22=1
)

# Create a Hamiltonian
spinham = magnopy.SpinHamiltonian(cell=cell, atoms=atoms, convention=convention)

# %%
#
# Cut-off by distance
# ===================
#
# All interaction with the distance that is shorter than cut-off are added.


spinham.add_dipole_dipole(R_cut=2, alphas=[0])

print(len(spinham.p22))

for alpha, beta, nu, parameter in spinham.p22:
    print(
        f'Bond from "{spinham.atoms.names[alpha]}" to "{spinham.atoms.names[beta]}" in {nu}\n {parameter}'
    )


_, pe2 = magnopy.experimental.plot_spinham(
    spinham, distance_digits=3, _sphinx_gallery_fix=True
)


pe2.show(axes_visible=False, legend_position="left")

# %%
#
# Cut-off by energy
# =================
#
# All interactions with energy larger that energy cut-off (in units of ``spinham.units``)
# are added

# Reset all parameter
spinham = spinham.get_empty()

spinham.add_dipole_dipole(E_cut=0.1, alphas=[0])

print(len(spinham.p22))

for alpha, beta, nu, parameter in spinham.p22:
    print(
        f'Bond from "{spinham.atoms.names[alpha]}" to "{spinham.atoms.names[beta]}" in {nu}\n {parameter}'
    )


_, pe2 = magnopy.experimental.plot_spinham(
    spinham, distance_digits=3, _sphinx_gallery_fix=True
)


pe2.show(axes_visible=False, legend_position="left")


# %%
# See ::py:meth:`magnopy.SpinHamiltonian.add_dipole_dipole` for more details.


# sphinx_gallery_thumbnail_path = 'img/cat-numbers/5.png'
