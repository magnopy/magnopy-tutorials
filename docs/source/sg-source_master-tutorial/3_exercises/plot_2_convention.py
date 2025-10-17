r"""
Convention of spin Hamiltonian
******************************

.. include:: ../../exercises/2.inc
"""

import magnopy

# %%
#
# Exercise 1
# ==========

convention_1 = magnopy.Convention(
    name="H-1", multiple_counting=False, spin_normalized=False, c22=-1
)

convention_2 = magnopy.Convention(
    name="H-2", multiple_counting=True, spin_normalized=False, c22=-1
)

convention_3 = magnopy.Convention(
    name="H-3", multiple_counting=True, spin_normalized=False, c22=0.5
)

convention_4 = magnopy.Convention(
    name="H-4", multiple_counting=False, spin_normalized=True, c22=-1
)


# sphinx_gallery_thumbnail_path = 'img/cat-numbers/2.png'
