r"""
Optimization of spin directions
*******************************

.. admonition:: Tutorial tasks

    *   Display list of all available parameters for the script.
    *   Optimize the Hamiltonian and inspect the output files.
    *   Optimize the Hamiltonian on several super-cells.
        Are there any changes of the ground state?
    *   Optimize with different directions and value of the external magnetic field.
        How does the result changes?

For the guide on the script read |magnopy-optimize-sd|_.

Below we give two examples that were run on the reference files from |GROGU|_.

Two reference files can be found in the ``Tutorial_2/magnopy-as-a-black-box`` folder.

Each example is run for each file. We use files that were produced by the run on the
"reference-CrI3.txt" |GROGU|_ file. Links for downloading equivalent files for
"reference-CrI3_U.txt" can be found at the end of each section

Optimization on the unit cell
=============================

First let us optimize the spin directions on the given unit cell of the spin Hamiltonian.

To do so run the commands

.. code-block:: bash

    magnopy-optimize-sd -ss GROGU -sf reference-CrI3.txt -of optimize-sd-output -hpd > console-output.txt

and

.. code-block:: bash

    magnopy-optimize-sd -ss GROGU -sf reference-CrI3_U.txt -of optimize-sd-output -hpd > console-output.txt

in the terminal.

Input parameters
----------------

Let us go thought the parameters

*   ``-ss GROGU``

    Tells magnopy that the Hamiltonian is coming from |GROGU|_.

*   ``-sf reference-CrI3.txt`` or ``-sf reference-CrI3_U.txt``

    Tells magnopy where the file with the Hamiltonian is located. The path, that is given
    for the ``-sf`` argument have to be either absolute or relative to the folder from
    which you execute the script.

*   ``-of optimize-sd-output``

    Tell magnopy to save all output files inside the "optimize-sd-output" folder.

*   ``-of -hpd``

    Tells magnopy to hide some of the private user's data in the output. Do not affect
    the calculation of magnopy, simply a decoration for the output.

*   ``> console-output.txt``

    Redirects text output of magnopy and saves in to the file "console-output.txt", that
    will be created in the folder from which you executed the script. To display the
    text in the terminal and to save it to the file simultaneously use
    ``| tee console-output.txt`` instead.

Output files
------------

After the successful completion of the script you can find several files in the
output folder. Below we list all those files and give links where you can download
examples of those files.

*   "console-output.txt"

    This is the main output file of magnopy that list the steps of the calculations,
    give comments, warnings and details on which files with data were produced and where
    they have been saved. Here is the content of that file for CrI3.txt

    .. literalinclude:: ../../resources/trilmax-2025/CrI3/optimize-sd/console-output.txt
        :caption: Content of "console-output.txt" for CrI3

*   "INITIAL_GUESS.txt"

    This file gives you the initial guess for spin directions that was used by the
    optimization routine. The initial guess is random, meaning that it is going to be
    different every time you run the program. In the file you will find one direction per
    line - initial guesses for each magnetic center. In the same order as they appear in
    the input file from |GROGU|_.

    .. literalinclude:: ../../resources/trilmax-2025/CrI3/optimize-sd/INITIAL_GUESS.txt
        :caption: Content of "INITIAL_GUESS.txt" for CrI3

*   "SPIN_POSITIONS.txt"

    This file gives Cartesian (absolute) coordinates of every magnetic center in the unit
    cell. One magnetic center per line, order is the same as in the input file from
    |GROGU|_.

    .. literalinclude:: ../../resources/trilmax-2025/CrI3/optimize-sd/SPIN_POSITIONS.txt
        :caption: Content of "SPIN_POSITIONS.txt" for CrI3

*   "SPIN_DIRECTIONS.txt"

    This file gives final, optimized spin directions for each spin in the unit cell. One
    spin per line, order is the same as in the input file from |GROGU|_.

    .. literalinclude:: ../../resources/trilmax-2025/CrI3/optimize-sd/SPIN_DIRECTIONS.txt
        :caption: Content of "SPIN_DIRECTIONS.txt" for CrI3

*   "SPIN_DIRECTIONS.html"

    This file visualizes the results of calculation in the interactive 3D picture. Unit
    cell, supercell (if any), initial guess and optimize spin directions are plotted.


Download the files for "reference-CrI3.txt"
-------------------------------------------

* :download:`console-output.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/optimize-sd/console-output.txt>`
* :download:`INITIAL_GUESS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/optimize-sd/INITIAL_GUESS.txt>`
* :download:`SPIN_POSITIONS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/optimize-sd/SPIN_POSITIONS.txt>`
* :download:`SPIN_DIRECTIONS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/optimize-sd/SPIN_DIRECTIONS.txt>`
* :download:`SPIN_DIRECTIONS.html (for CrI3.txt) <../../resources/trilmax-2025/CrI3/optimize-sd/SPIN_DIRECTIONS.html>`


Download the files for "reference-CrI3_U.txt"
---------------------------------------------

* :download:`console-output.txt (for CrI3_U.txt) <../../resources/trilmax-2025/CrI3_U/optimize-sd/console-output.txt>`
* :download:`INITIAL_GUESS.txt (for CrI3_U.txt) <../../resources/trilmax-2025/CrI3_U/optimize-sd/INITIAL_GUESS.txt>`
* :download:`SPIN_POSITIONS.txt (for CrI3_U.txt) <../../resources/trilmax-2025/CrI3_U/optimize-sd/SPIN_POSITIONS.txt>`
* :download:`SPIN_DIRECTIONS.txt (for CrI3_U.txt) <../../resources/trilmax-2025/CrI3_U/optimize-sd/SPIN_DIRECTIONS.txt>`
* :download:`SPIN_DIRECTIONS.html (for CrI3_U.txt) <../../resources/trilmax-2025/CrI3_U/optimize-sd/SPIN_DIRECTIONS.html>`



Optimization on the supercell
=============================

For some systems the true ground state may not have the same periodicity as the unit cell
of the underlying crystal. In that case one shall try to optimize the spin directions on
the supercell and check if any new local minima can be found.

To do so run the commands

.. code-block:: bash

    magnopy-optimize-sd -s 5 5 1 -ss GROGU -sf reference-CrI3.txt -of optimize-sd-output-5-5-1 -hpd > console-output.txt

and

.. code-block:: bash

    magnopy-optimize-sd -s 5 5 1 -ss GROGU -sf reference-CrI3_U.txt -of optimize-sd-output-5-5-1 -hpd > console-output.txt

in the terminal.

Input parameters
----------------

There is one extra parameter in the input

*   ``-s 5 5 1``

    Tells magnopy to construct a :math:`(5,5,1)` supercell and minimize spin directions by
    varying all spins in the supercell independently.

Output files
------------

The set of output files is the same


*   "console-output.txt"

    .. literalinclude:: ../../resources/trilmax-2025/CrI3/optimize-sd-5-5-1/console-output.txt
        :caption: Content of "console-output.txt" for CrI3

*   "INITIAL_GUESS.txt"

    .. literalinclude:: ../../resources/trilmax-2025/CrI3/optimize-sd-5-5-1/INITIAL_GUESS.txt
        :caption: Content of "INITIAL_GUESS.txt" for CrI3

*   "SPIN_POSITIONS.txt"

    .. literalinclude:: ../../resources/trilmax-2025/CrI3/optimize-sd-5-5-1/SPIN_POSITIONS.txt
        :caption: Content of "SPIN_POSITIONS.txt" for CrI3

*   "SPIN_DIRECTIONS.txt"

    .. literalinclude:: ../../resources/trilmax-2025/CrI3/optimize-sd-5-5-1/SPIN_DIRECTIONS.txt
        :caption: Content of "SPIN_DIRECTIONS.txt" for CrI3

*   "SPIN_DIRECTIONS.html"

Download the files for "reference-CrI3.txt"
-------------------------------------------

* :download:`console-output.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/optimize-sd-5-5-1/console-output.txt>`
* :download:`INITIAL_GUESS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/optimize-sd-5-5-1/INITIAL_GUESS.txt>`
* :download:`SPIN_POSITIONS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/optimize-sd-5-5-1/SPIN_POSITIONS.txt>`
* :download:`SPIN_DIRECTIONS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/optimize-sd-5-5-1/SPIN_DIRECTIONS.txt>`
* :download:`SPIN_DIRECTIONS.html (for CrI3.txt) <../../resources/trilmax-2025/CrI3/optimize-sd-5-5-1/SPIN_DIRECTIONS.html>`


Download the files for "reference-CrI3_U.txt"
---------------------------------------------

* :download:`console-output.txt (for CrI3_U.txt) <../../resources/trilmax-2025/CrI3_U/optimize-sd-5-5-1/console-output.txt>`
* :download:`INITIAL_GUESS.txt (for CrI3_U.txt) <../../resources/trilmax-2025/CrI3_U/optimize-sd-5-5-1/INITIAL_GUESS.txt>`
* :download:`SPIN_POSITIONS.txt (for CrI3_U.txt) <../../resources/trilmax-2025/CrI3_U/optimize-sd-5-5-1/SPIN_POSITIONS.txt>`
* :download:`SPIN_DIRECTIONS.txt (for CrI3_U.txt) <../../resources/trilmax-2025/CrI3_U/optimize-sd-5-5-1/SPIN_DIRECTIONS.txt>`
* :download:`SPIN_DIRECTIONS.html (for CrI3_U.txt) <../../resources/trilmax-2025/CrI3_U/optimize-sd-5-5-1/SPIN_DIRECTIONS.html>`






"""

# sphinx_gallery_thumbnail_path = 'img/gallery-thumbnails/trilmax-2025/black-box/optimize-sd.png'
