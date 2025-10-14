R"""
magnopy-optimize-sd
*******************

This page explains how to use optimize spin direction via numerical minimization. See
docs for |magnopy-optimize-sd|_ for full list of supported arguments. On this page we
give examples of how to use the script and text and files that it can produce.

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

    * :download:`ferro-easy-axis.txt <../../resources/master-tutorial/ferro-easy-axis.txt>`


.. prompt-run::
    :input-prefix: ../../resources/master-tutorial/
    :output-prefix: 1
    :extra-command: -of {{OP:magnopy-results}}

    magnopy-optimize-sd --spinham-source GROGU --spinham-filename {{IP:ferro-easy-axis.txt}}

.. dropdown:: :octicon:`command-palette;1em;custom-octicon-output` Output to the console

    .. literalinclude:: prompt-run_plot-1-optimize-sd/1/console-output.txt

.. dropdown:: :octicon:`file;1em;custom-octicon-output` Created files

    * :download:`INITIAL_GUESS.txt <prompt-run_plot-1-optimize-sd/1/magnopy-results/INITIAL_GUESS.txt>`
    * :download:`SPIN_DIRECTIONS.txt <prompt-run_plot-1-optimize-sd/1/magnopy-results/SPIN_DIRECTIONS.txt>`
    * :download:`SPIN_DIRECTIONS.html <prompt-run_plot-1-optimize-sd/1/magnopy-results/SPIN_DIRECTIONS.html>`
    * :download:`SPIN_POSITIONS.txt <prompt-run_plot-1-optimize-sd/1/magnopy-results/SPIN_POSITIONS.txt>`


Minimization domain
===================

By default magnopy vary spins of the original unit cell. However, potential local or
global minima that span several unit cells can be missed. To address this issue, magnopy
offers an option of minimization on the supercell.

Supercell is defined by a number of the original unit cell's repetitions along each of its
three lattice vectors (``--superell``). For example, if you want to minimize on the
:math:`3\times7\times2` supercell use the command

.. dropdown:: :octicon:`file;1em;custom-octicon-input` Input files

    * :download:`ferro-easy-axis.txt <../../resources/master-tutorial/ferro-easy-axis.txt>`

.. prompt-run::
    :input-prefix: ../../resources/master-tutorial/
    :output-prefix: 2
    :extra-command: -of {{OP:magnopy-results}}

    magnopy-optimize-sd --supercell 3 7 2 --spinham-source GROGU --spinham-filename {{IP:ferro-easy-axis.txt}}

.. dropdown:: :octicon:`command-palette;1em;custom-octicon-output` Output to the console

    .. literalinclude:: prompt-run_plot-1-optimize-sd/2/console-output.txt

.. dropdown:: :octicon:`file;1em;custom-octicon-output` Created files

    * :download:`INITIAL_GUESS.txt <prompt-run_plot-1-optimize-sd/2/magnopy-results/INITIAL_GUESS.txt>`
    * :download:`SPIN_DIRECTIONS.txt <prompt-run_plot-1-optimize-sd/2/magnopy-results/SPIN_DIRECTIONS.txt>`
    * :download:`SPIN_DIRECTIONS.html <prompt-run_plot-1-optimize-sd/2/magnopy-results/SPIN_DIRECTIONS.html>`
    * :download:`SPIN_POSITIONS.txt <prompt-run_plot-1-optimize-sd/2/magnopy-results/SPIN_POSITIONS.txt>`

Then every spin in the :math:`3\times7\times2` supercell is treated as an individual
variable. Note, that the computational cost of minimization will grow with the size of the
supercell.

Accuracy or tolerance conditions
================================

Numerical optimization can continues indefinitely, improving accuracy of some target
value with each step. In reality an algorithm should reach some tolerance values in the
finite amount of steps.

The minimization algorithm implemented in magnopy [1]_ traces two values:

*   ``--energy-tolerance``

    Absolute value of the difference in total energy between two consecutive steps of the
    minimization.

*   ``--torque-tolerance``

    Maximum (among all spins of the unit cell or supercell) value of the torque vector.

An algorithm stops when both tolerance parameters are reached. The default values should
lead to the reasonable results in most of the cases.

However, if you want to increase accuracy of one or both parameters, then use the command

.. dropdown:: :octicon:`file;1em;custom-octicon-input` Input files

    * :download:`ferro-easy-axis.txt <../../resources/master-tutorial/ferro-easy-axis.txt>`

.. prompt-run::
    :input-prefix: ../../resources/master-tutorial/
    :output-prefix: 3
    :extra-command: -of {{OP:magnopy-results}}

    magnopy-optimize-sd --energy-tolerance 0.000001 --torque-tolerance 0.001 --spinham-source GROGU --spinham-filename {{IP:ferro-easy-axis.txt}}

.. dropdown:: :octicon:`command-palette;1em;custom-octicon-output` Output to the console

    .. literalinclude:: prompt-run_plot-1-optimize-sd/3/console-output.txt

.. dropdown:: :octicon:`file;1em;custom-octicon-output` Created files

    * :download:`INITIAL_GUESS.txt <prompt-run_plot-1-optimize-sd/3/magnopy-results/INITIAL_GUESS.txt>`
    * :download:`SPIN_DIRECTIONS.txt <prompt-run_plot-1-optimize-sd/3/magnopy-results/SPIN_DIRECTIONS.txt>`
    * :download:`SPIN_DIRECTIONS.html <prompt-run_plot-1-optimize-sd/3/magnopy-results/SPIN_DIRECTIONS.html>`
    * :download:`SPIN_POSITIONS.txt <prompt-run_plot-1-optimize-sd/3/magnopy-results/SPIN_POSITIONS.txt>`

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

    * :download:`ferro-easy-axis.txt <../../resources/master-tutorial/ferro-easy-axis.txt>`

.. prompt-run::
    :input-prefix: ../../resources/master-tutorial/
    :output-prefix: 4
    :extra-command: -of {{OP:magnopy-results}}

    magnopy-optimize-sd --magnetic-field 1.7112 1.7112 0 --spinham-source GROGU --spinham-filename {{IP:ferro-easy-axis.txt}}

.. dropdown:: :octicon:`command-palette;1em;custom-octicon-output` Output to the console

    .. literalinclude:: prompt-run_plot-1-optimize-sd/4/console-output.txt

.. dropdown:: :octicon:`file;1em;custom-octicon-output` Created files

    * :download:`INITIAL_GUESS.txt <prompt-run_plot-1-optimize-sd/4/magnopy-results/INITIAL_GUESS.txt>`
    * :download:`SPIN_DIRECTIONS.txt <prompt-run_plot-1-optimize-sd/4/magnopy-results/SPIN_DIRECTIONS.txt>`
    * :download:`SPIN_DIRECTIONS.html <prompt-run_plot-1-optimize-sd/4/magnopy-results/SPIN_DIRECTIONS.html>`
    * :download:`SPIN_POSITIONS.txt <prompt-run_plot-1-optimize-sd/4/magnopy-results/SPIN_POSITIONS.txt>`

to add magnetic field of :math:`2.42` Tesla along the direction :math:`(1, 1, 0)`
(i.e. in the :math:`xy` plane, right in between the :math:`x` and :math:`y` axis).


References
==========

.. [1] Ivanov, A.V., Uzdin, V.M. and Jónsson, H., 2021.
    Fast and robust algorithm for energy minimization of spin systems applied
    in an analysis of high temperature spin configurations in terms of skyrmion
    density.
    Computer Physics Communications, 260, p.107749.
"""

# sphinx_gallery_thumbnail_path = 'img/cat-numbers/1.png'
