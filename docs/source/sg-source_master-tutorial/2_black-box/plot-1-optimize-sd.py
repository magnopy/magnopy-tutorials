R"""
Optimization of spin directions
*******************************

This page explains how to use |magnopy-optimize-sd|_ and give examples of the
output files.

Spin Hamiltonian and its source
===============================

This script works with the spin Hamiltonian that is coming from some third-party software.
At the moment magnopy supports |TB2J|_ and |GROGU|_.

.. hint::
    There is number of ways to use this script with the hand-made Hamiltonian:

    * Prepare the file that mimics the format of |TB2J|_.
    * Prepare the file that mimics the |GROGU-FF|_.
    * Prepare the spin Hamiltonian programmatically and use the scenario of this
      command-line script from within your python script:
      :py:func:`magnopy.scenarios.optimize_sd`.

Two parameters are required for this script

* Source of the spin Hamiltonian (``-ss`` or ``--spinham-source``);
* Path to the file with the spin Hamiltonian (``-sf`` or ``--spinham-filename``)

For example, if "ferro-easy-axis.txt" is a file with the spin Hamiltonian and the source
of the file is |GROGU|_, then you can run the script as

.. prompt-run::
    :input-prefix: ../../resources/master-tutorial/
    :output-prefix: ./
    :extra-command: -of {{OP:magnopy-results}}

    magnopy-optimize-sd --spinham-source GROGU --spinham-filename {{IP:ferro-easy-axis.txt}}

Files produced by the script:

* :download:`INITIAL_GUESS.TXT <prompt-run_plot-1-optimize-sd/magnopy-results/INITIAL_GUESS.TXT>`
* :download:`SPIN_DIRECTIONS.txt <prompt-run_plot-1-optimize-sd/magnopy-results/SPIN_DIRECTIONS.txt>`
* :download:`SPIN_DIRECTIONS.html <prompt-run_plot-1-optimize-sd/magnopy-results/SPIN_DIRECTIONS.html>`
* :download:`SPIN_POSITIONS.txt <prompt-run_plot-1-optimize-sd/magnopy-results/SPIN_POSITIONS.txt>`

.. dropdown:: Output to the console

    .. literalinclude:: prompt-run_plot-1-optimize-sd/console-output.txt







.. _user-guide_cli_optimize-sd_supercell:

Minimization domain
===================

By default magnopy vary only the spins within the original unit cell of the Hamiltonian.
In that way it can miss the true ground state if it spans over several unit cells that
can not be transformed into one another by a simple translation. To address this issue,
we offer an option of minimization on the supercell. The supercell is produced by a number of
translations of the original unit cell (``-s`` or ``--superell``). For example, to ask
for a minimization of the :math:`3\times7\times2` supercell one can use the command


.. code-block:: bash

    magnopy-optimize-sd ... --supercell 3 7 2 ...

In that case every spin in the :math:`3\times7\times2` supercell is treated as an
individual variable. Note, that the computational cost of minimization will grow with
the size of the supercell.


.. note::
    The dots ``...`` are not a part of the syntax. They are used only to highlight the
    parameters that are described in the particular chapter of the documentation and
    hide all other parameters that might or might not be passed to the script.


.. _user-guide_cli_optimize-sd_tolerance:

Accuracy or tolerance conditions
================================

In theory numerical optimization can continues indefinitely, improving accuracy of
some target value with each step. In reality an algorithm should reach some values of the
tolerance after the finite amount of steps.

The minimization algorithm implemented in magnopy [1]_ traces two values:

* Absolute value of the difference in total energy between two consecutive steps
  of the minimization (``-et`` or ``--energy-tolerance``).
* Maximum (among all spins of the unit cell or supercell) value of the torque vector (``-tt`` or
  ``--torque-tolerance``).

An algorithm stops and output the obtained spin directions when both tolerance parameters
are reached. The default values, that magnopy uses should lead to the reasonable results
in most of the cases.

However, if you want to increase accuracy of one of the parameters or both, then try to
pass the corresponding parameters to the script

.. code-block:: bash

    magnopy-optimize-sd ... --energy-tolerance 0.000001 --torque-tolerance 0.001 ...


.. note::
    The dots ``...`` are not a part of the syntax. They are used only to highlight the
    parameters that are described in the particular chapter of the documentation and
    hide all other parameters that might or might not be passed to the script.

.. _user-guide_cli_optimize-sd_magnetic-field:

External magnetic field
=======================

The file with the :ref:`spin Hamiltonian <user-guide_cli_optimize-sd_spinham>`
specifies the interaction parameters that are intrinsic to the material.

In order to add additional effects, for instance an external magnetic field one
can use the ``-mf`` or ``--magnetic-field`` parameter.

This parameter expects three numbers, that specify three Cartesian components of the
external magnetic field. The value of the provided vector is interpreted in Tesla.

For example to add magnetic field of 2.42 Tesla along the direction :math:`(1, 1, 0)`
(i.e. in the :math:`xy` plane, right in between the :math:`x` and :math:`y` axis) pass
to the script the parameter

.. code-block:: bash

    magnopy-optimize-sd ... --magnetic-field 1.7112 1.7112 0 ...


.. note::
    The dots ``...`` are not a part of the syntax. They are used only to highlight the
    parameters that are described in the particular chapter of the documentation and
    hide all other parameters that might or might not be passed to the script.

.. _user-guide_cli_optimize-sd_output:


"""
