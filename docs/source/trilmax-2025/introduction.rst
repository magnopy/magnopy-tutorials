*******************
Introducing magnopy
*******************

First of all, |magnopy|_ shall be installed. For the full guide on installation you can
read FIXME. For using magnopy in the school you need to install magnopy right within the 
jupyter notebook. Type the following command in the free notebook cell, run it and restart
the kernel if necessary.

.. code-block:: bash

    %pip install "magnopy[visual]"

Note that you are installing the extended version of magnopy that supports production of 
``.png`` and ``.html`` files, that will be mentioned in this tutorial.

.. note::

    We recommend to install magnopy with its visual capabilities whenever possible.
    Magnopy will output graphics by default if |plotly|_ and |magnopy|_ are installed.
    Nevertheless, we did not want to include graphical libraries as default dependencies
    to the package.

To check that installation worked properly try to execute in the notebook cell the following
code

.. code-block:: python

    import magnopy

    print(magnopy.logo())


Import
======

Magnopy have a well defined set of public functions, that shall be available in code
completion. Full list of available methods and objects one can always find FIXME.

to include magnopy in your script import it in the usual way

.. code-block:: python

    import magnopy

Now all magnopy's public objects are available under ``magnopy.``.

.. hint:: 
    
    It is enough to import magnopy once at the top of the notebook.


Crystal structure in magnopy
============================

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

To read more about the cell see FIXME.

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
        "names": ["Cr1", "I1", "I2", "I3"],
        "positions" : [[0.0, 0.0 ,0.0], [FIXME], [FIXME], [FIXME]],
        "spins" : [1.5, None, None, None],
        "g-factor" : [2, None, None, None],

    }

To read more about atoms see FIXME.





