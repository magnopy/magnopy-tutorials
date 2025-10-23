r"""
magnopy-lswt
************

This page explains how to use optimize spin direction via numerical minimization. See
docs for |magnopy-lswt|_ for full list of supported arguments. On this page we give
examples of how to use the script and text and files that it can produce.

Spin Hamiltonian and its source
===============================

This script works with the spin Hamiltonian that is coming from some third-party software.
At the moment magnopy supports |TB2J|_ and |GROGU|_.

.. hint::
    There is a number of ways to use this script with the hand-made Hamiltonian:

    * Prepare the file that mimics the format of |TB2J|_.
    * Prepare the file that mimics the |GROGU-FF|_.
    * Prepare the spin Hamiltonian programmatically and use the scenario of this
      command-line script from within your python script:
      :py:func:`magnopy.scenarios.optimize_sd`.

Two parameters are required

* Source of the spin Hamiltonian (``--spinham-source``);
* Path to the file with the spin Hamiltonian (``--spinham-filename``)

For example, if "ferro-easy-axis.txt" is a file with the spin Hamiltonian and the source
of the file is |GROGU|_, then you can run the script as

.. dropdown:: :octicon:`file;1em;custom-octicon-input` Input files

    * :download:`ferro-easy-axis.txt <../../resources/ferro-easy-axis.txt>`

.. prompt-run::
    :input-prefix: ../../resources/
    :output-prefix: 1
    :extra-command: -of {{OP:magnopy-results}}

    magnopy-lswt --spinham-source GROGU --spinham-filename {{IP:ferro-easy-axis.txt}}

.. dropdown:: :octicon:`command-palette;1em;custom-octicon-output` Output to the console

    .. literalinclude:: prompt-run_plot-2-lswt/1/console-output.txt

.. dropdown:: :octicon:`file;1em;custom-octicon-output` Created files

    * :download:`E_0.txt <prompt-run_plot-2-lswt/1/magnopy-results/E_0.txt>`
    * :download:`E_2.txt <prompt-run_plot-2-lswt/1/magnopy-results/E_2.txt>`
    * :download:`DELTAS.txt <prompt-run_plot-2-lswt/1/magnopy-results/DELTAS.txt>`
    * :download:`DELTAS.png <prompt-run_plot-2-lswt/1/magnopy-results/DELTAS.png>`
    * :download:`HIGH-SYMMETRY_POINTS.txt <prompt-run_plot-2-lswt/1/magnopy-results/HIGH-SYMMETRY_POINTS.txt>`
    * :download:`K-POINTS.txt <prompt-run_plot-2-lswt/1/magnopy-results/K-POINTS.txt>`
    * :download:`K-POINTS.html <prompt-run_plot-2-lswt/1/magnopy-results/K-POINTS.html>`
    * :download:`OMEGAS.txt <prompt-run_plot-2-lswt/1/magnopy-results/OMEGAS.txt>`
    * :download:`OMEGAS.png <prompt-run_plot-2-lswt/1/magnopy-results/OMEGAS.png>`
    * :download:`SPIN_VECTORS.txt <prompt-run_plot-2-lswt/1/magnopy-results/SPIN_VECTORS.txt>`
    * :download:`SPIN_DIRECTIONS.html <prompt-run_plot-2-lswt/1/magnopy-results/SPIN_DIRECTIONS.html>`

Ground state
============

One need to know the ground state (i. e. spin directions for every spin of the
Hamiltonian) for the calculation of the exited states. There are two ways for magnopy to
know the spin directions

*   Input from the user

    User can provide a file with spin directions using the command

    .. dropdown:: :octicon:`file;1em;custom-octicon-input` Input files

        * :download:`ferro-easy-axis.txt <../../resources/ferro-easy-axis.txt>`
        * :download:`sd-ferro-easy-axis.txt <../../resources/sd-ferro-easy-axis.txt>`

    .. prompt-run::
        :input-prefix: ../../resources/
        :output-prefix: 2
        :extra-command: -of {{OP:magnopy-results}}

        magnopy-lswt --spin-directions {{IP:sd-ferro-easy-axis.txt}} --spinham-source GROGU --spinham-filename {{IP:ferro-easy-axis.txt}}

    .. dropdown:: :octicon:`command-palette;1em;custom-octicon-output` Output to the console

        .. literalinclude:: prompt-run_plot-2-lswt/2/console-output.txt

    .. dropdown:: :octicon:`file;1em;custom-octicon-output` Created files

        * :download:`E_0.txt <prompt-run_plot-2-lswt/2/magnopy-results/E_0.txt>`
        * :download:`E_2.txt <prompt-run_plot-2-lswt/2/magnopy-results/E_2.txt>`
        * :download:`DELTAS.txt <prompt-run_plot-2-lswt/2/magnopy-results/DELTAS.txt>`
        * :download:`DELTAS.png <prompt-run_plot-2-lswt/2/magnopy-results/DELTAS.png>`
        * :download:`HIGH-SYMMETRY_POINTS.txt <prompt-run_plot-2-lswt/2/magnopy-results/HIGH-SYMMETRY_POINTS.txt>`
        * :download:`K-POINTS.txt <prompt-run_plot-2-lswt/2/magnopy-results/K-POINTS.txt>`
        * :download:`K-POINTS.html <prompt-run_plot-2-lswt/2/magnopy-results/K-POINTS.html>`
        * :download:`OMEGAS.txt <prompt-run_plot-2-lswt/2/magnopy-results/OMEGAS.txt>`
        * :download:`OMEGAS.png <prompt-run_plot-2-lswt/2/magnopy-results/OMEGAS.png>`
        * :download:`SPIN_VECTORS.txt <prompt-run_plot-2-lswt/2/magnopy-results/SPIN_VECTORS.txt>`
        * :download:`SPIN_DIRECTIONS.html <prompt-run_plot-2-lswt/2/magnopy-results/SPIN_DIRECTIONS.html>`


*   Internal optimization

    If user do not provide any input, then magnopy tries to optimize spin directions within
    unit cell. See also |magnopy-optimize-sd|_.


K-path and k-points
===================

Magnopy solves magnon problem for a set of points in reciprocal space. Therefore, it needs
to know a set of k-points to perform the calculations. User is left with two options

*   ``--kpoints``

    Provide explicit list of k-points

    .. dropdown:: :octicon:`file;1em;custom-octicon-input` Input files

        * :download:`ferro-easy-axis.txt <../../resources/ferro-easy-axis.txt>`
        * :download:`k-points-ferro-easy-axis.txt <../../resources/k-points-ferro-easy-axis.txt>`

    .. prompt-run::
        :input-prefix: ../../resources/
        :output-prefix: 3
        :extra-command: -of {{OP:magnopy-results}}

        magnopy-lswt --kpoints {{IP:k-points-ferro-easy-axis.txt}} --spinham-source GROGU --spinham-filename {{IP:ferro-easy-axis.txt}}

    .. dropdown:: :octicon:`command-palette;1em;custom-octicon-output` Output to the console

        .. literalinclude:: prompt-run_plot-2-lswt/3/console-output.txt

    .. dropdown:: :octicon:`file;1em;custom-octicon-output` Created files

        * :download:`E_0.txt <prompt-run_plot-2-lswt/3/magnopy-results/E_0.txt>`
        * :download:`E_2.txt <prompt-run_plot-2-lswt/3/magnopy-results/E_2.txt>`
        * :download:`DELTAS.txt <prompt-run_plot-2-lswt/3/magnopy-results/DELTAS.txt>`
        * :download:`DELTAS.png <prompt-run_plot-2-lswt/3/magnopy-results/DELTAS.png>`
        * :download:`K-POINTS.txt <prompt-run_plot-2-lswt/3/magnopy-results/K-POINTS.txt>`
        * :download:`OMEGAS.txt <prompt-run_plot-2-lswt/3/magnopy-results/OMEGAS.txt>`
        * :download:`OMEGAS.png <prompt-run_plot-2-lswt/3/magnopy-results/OMEGAS.png>`
        * :download:`SPIN_VECTORS.txt <prompt-run_plot-2-lswt/3/magnopy-results/SPIN_VECTORS.txt>`
        * :download:`SPIN_DIRECTIONS.html <prompt-run_plot-2-lswt/3/magnopy-results/SPIN_DIRECTIONS.html>`

*   ``--k-path``

    Let magnopy deduce the set of high-symmetry points based on the space group of the
    crystal and use recommended k-path (see documentation of |wulfric|_ for more details,
    magnopy uses ``convention="HPKOT"``). User can control k-path, but limited to the list
    of the predefined high-symmetry points.


    .. dropdown:: :octicon:`file;1em;custom-octicon-input` Input files

        * :download:`ferro-easy-axis.txt <../../resources/ferro-easy-axis.txt>`

    .. prompt-run::
        :input-prefix: ../../resources/
        :output-prefix: 4
        :extra-command: -of {{OP:magnopy-results}}

        magnopy-lswt --k-path GAMMA-X-S|GAMMA-Y --spinham-source GROGU --spinham-filename {{IP:ferro-easy-axis.txt}}

    .. dropdown:: :octicon:`command-palette;1em;custom-octicon-output` Output to the console

        .. literalinclude:: prompt-run_plot-2-lswt/4/console-output.txt

    .. dropdown:: :octicon:`file;1em;custom-octicon-output` Created files

        * :download:`E_0.txt <prompt-run_plot-2-lswt/4/magnopy-results/E_0.txt>`
        * :download:`E_2.txt <prompt-run_plot-2-lswt/4/magnopy-results/E_2.txt>`
        * :download:`DELTAS.txt <prompt-run_plot-2-lswt/4/magnopy-results/DELTAS.txt>`
        * :download:`DELTAS.png <prompt-run_plot-2-lswt/4/magnopy-results/DELTAS.png>`
        * :download:`HIGH-SYMMETRY_POINTS.txt <prompt-run_plot-2-lswt/4/magnopy-results/HIGH-SYMMETRY_POINTS.txt>`
        * :download:`K-POINTS.txt <prompt-run_plot-2-lswt/4/magnopy-results/K-POINTS.txt>`
        * :download:`K-POINTS.html <prompt-run_plot-2-lswt/4/magnopy-results/K-POINTS.html>`
        * :download:`OMEGAS.txt <prompt-run_plot-2-lswt/4/magnopy-results/OMEGAS.txt>`
        * :download:`OMEGAS.png <prompt-run_plot-2-lswt/4/magnopy-results/OMEGAS.png>`
        * :download:`SPIN_VECTORS.txt <prompt-run_plot-2-lswt/4/magnopy-results/SPIN_VECTORS.txt>`
        * :download:`SPIN_DIRECTIONS.html <prompt-run_plot-2-lswt/4/magnopy-results/SPIN_DIRECTIONS.html>`


External magnetic field
=======================

File with the spin Hamiltonian specifies interaction parameters that are intrinsic to the
material.

In order to add external effects, for instance an external magnetic field one can use
``--magnetic-field`` parameter.

This parameter expects three numbers, that specify three Cartesian components of the
external magnetic field (magnetic flux density, B). Values are interpreted in Tesla.

For example, use the command

.. dropdown:: :octicon:`file;1em;custom-octicon-input` Input files

    * :download:`ferro-easy-axis.txt <../../resources/ferro-easy-axis.txt>`

.. prompt-run::
    :input-prefix: ../../resources/
    :output-prefix: 5
    :extra-command: -of {{OP:magnopy-results}}

    magnopy-lswt --magnetic-field 1.7112 1.7112 0 --spinham-source GROGU --spinham-filename {{IP:ferro-easy-axis.txt}}

.. dropdown:: :octicon:`command-palette;1em;custom-octicon-output` Output to the console

    .. literalinclude:: prompt-run_plot-2-lswt/5/console-output.txt

.. dropdown:: :octicon:`file;1em;custom-octicon-output` Created files

    * :download:`E_0.txt <prompt-run_plot-2-lswt/5/magnopy-results/E_0.txt>`
    * :download:`E_2.txt <prompt-run_plot-2-lswt/5/magnopy-results/E_2.txt>`
    * :download:`DELTAS.txt <prompt-run_plot-2-lswt/5/magnopy-results/DELTAS.txt>`
    * :download:`DELTAS.png <prompt-run_plot-2-lswt/5/magnopy-results/DELTAS.png>`
    * :download:`HIGH-SYMMETRY_POINTS.txt <prompt-run_plot-2-lswt/5/magnopy-results/HIGH-SYMMETRY_POINTS.txt>`
    * :download:`K-POINTS.txt <prompt-run_plot-2-lswt/5/magnopy-results/K-POINTS.txt>`
    * :download:`K-POINTS.html <prompt-run_plot-2-lswt/5/magnopy-results/K-POINTS.html>`
    * :download:`OMEGAS.txt <prompt-run_plot-2-lswt/5/magnopy-results/OMEGAS.txt>`
    * :download:`OMEGAS.png <prompt-run_plot-2-lswt/5/magnopy-results/OMEGAS.png>`
    * :download:`SPIN_VECTORS.txt <prompt-run_plot-2-lswt/5/magnopy-results/SPIN_VECTORS.txt>`
    * :download:`SPIN_DIRECTIONS.html <prompt-run_plot-2-lswt/5/magnopy-results/SPIN_DIRECTIONS.html>`

to add magnetic field of :math:`2.42` Tesla along the direction :math:`(1, 1, 0)`
(i.e. in the :math:`xy` plane, right in between the :math:`x` and :math:`y` axis).


"""

# sphinx_gallery_thumbnail_path = 'img/cat-numbers/2.png'
