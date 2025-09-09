r"""
Linear Spin Wave theory
***********************

.. admonition:: Tutorial tasks

    *   Display list of all available parameters for the script.
    *   Run the script and examine the output. Is the space group the one you would expect?
        If not, than try to reduce ``--spglib-symprec`` and check if it changes.
    *   Use spin directions file from the results of ``magnopy.optimize-sd`` to execute
        this script.
    *   Compute magnon dispersion for the custom k-path (Use only in-plane
        high-symmetry points).

For the guide on the script read |magnopy-lswt|_.

Below we give two examples that were run on the reference files from |GROGU|_.

Two reference files can be found in the ``Tutorial_2/magnopy-as-a-black-box`` folder.

Each example is run for each file. We use files that were produced by the run on the
"reference-CrI3.txt" |GROGU|_ file. Links for downloading equivalent files for
"reference-CrI3_U.txt" can be found at the end of each section

LSWT calculations
=================

To do so run the commands

.. code-block:: bash

    magnopy-lswt -ss GROGU -sf CrI3/reference-GROGU.txt -sd CrI3/optimize-sd-output/SPIN_DIRECTIONS.txt -hpd -of CrI3/lswt-output > console-output.txt

and

.. code-block:: bash

    magnopy-lswt -ss GROGU -sf CrI3_U/reference-GROGU.txt -sd CrI3_U/optimize-sd-output/SPIN_DIRECTIONS.txt -hpd -of CrI3_U/lswt-output > console-output.txt

Input parameters
----------------

Let us go thought the parameters

*   ``-ss GROGU``

    Tells magnopy that the Hamiltonian is coming from |GROGU|_.

*   ``-sf CrI3/reference-GROGU.txt``

    Tells magnopy where the file with the Hamiltonian is located. The path, that is given
    for the ``-sf`` argument have to be either absolute or relative to the folder from
    which you execute the script.

*   ``-sd CrI3_U/optimize-sd-output/SPIN_DIRECTIONS.txt``

    Tells magnopy to use spin directions that were computed by the optimization routine.

*   ``-of CrI3/optimize-sd-output``

    Tells magnopy to save all output files inside the "CrI3/optimize-sd-output" folder.

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
    they have been saved.

    .. literalinclude:: ../../resources/trilmax-2025/CrI3/lswt/console-output.txt
        :caption: Content of "console-output.txt" for CrI3

*   "SPIN_VECTORS.txt"

    This is the file with the spin directions (first three numbers in each line) and spin
    value (fourth number of each line) that were used as a ground state for LSWT
    computation. One magnetic center per line, order is the same as in the input file from
    |GROGU|_.

    .. literalinclude:: ../../resources/trilmax-2025/CrI3/lswt/SPIN_VECTORS.txt
        :caption: Content of "SPIN_VECTORS.txt" for CrI3

*   "SPIN_DIRECTIONS.html"

    This file visualizes the spin directions that were used with the interactive 3D
    picture.

*   "HIGH-SYMMETRY_POINTS.txt"

    This file lists labels, absolute (k_x, k_y, k_z) and relative with respect to the
    reciprocal cell of the unit cell from |GROGU|_ file (r_b1, r_b2, r_b3) of
    high-symmetry k-points that are chosen based on HPKOT convention and space group of
    the crystal that were detected. See documentation of |wulfric|_ for more details.

    .. literalinclude:: ../../resources/trilmax-2025/CrI3/lswt/HIGH-SYMMETRY_POINTS.txt
        :caption: Content of "HIGH-SYMMETRY_POINTS.txt" for CrI3

*   "K-POINTS.txt"

    This file lists explicit list of all f-points that were used in calculations. Their
    absolute (k_x, k_y, k_z) and relative with respect to the reciprocal cell of the
    unit cell from |GROGU|_ file (r_b1, r_b2, r_b3) and a "flat" coordinate, that were
    used in the dispersion plot (flat index).

    .. dropdown:: Content of "K-POINTS.txt" for CrI3

        .. literalinclude:: ../../resources/trilmax-2025/CrI3/lswt/K-POINTS.txt

*   "K-POINTS.html"

    This file visualizes high-symmetry k-points, k-path, reciprocal cell of the
    unit cell from |GROGU|_ file and reciprocal cell of the primitive cell that is
    associated with the detected space group and given crystal structure.

*   "OMEGAS.txt"

    This is the file with the data of the magnon spectra. Each column is a separate magnon
    mode. Each line gives energies of the modes for the k-point of the same line in the
    "K-POINTS.txt file"

    .. dropdown:: Content of "OMEGAS.txt" for CrI3

        .. literalinclude:: ../../resources/trilmax-2025/CrI3/lswt/OMEGAS.txt

*   "OMEGAS.png"

    This is the plot of the magnon spectra.

    .. image:: ../../resources/trilmax-2025/CrI3/lswt/OMEGAS.png

*   "DELTAS.txt"

    This is k-resolved :math:`\Delta(\boldsymbol{k})` term. Each line gives :math:`\Delta`
    for the k-point of the same line in the "K-POINTS.txt file"

    .. dropdown:: Content of "DELTAS.txt" for CrI3

        .. literalinclude:: ../../resources/trilmax-2025/CrI3/lswt/DELTAS.txt

*   "DELTAS.png"

    This is the plot of the :math:`\Delta(\boldsymbol{k})` term.

    .. image:: ../../resources/trilmax-2025/CrI3/lswt/DELTAS.png


Download the files for "CrI3/reference-GROGU.txt"
-------------------------------------------------

* :download:`console-output.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/console-output.txt>`
* :download:`SPIN_VECTORS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/SPIN_VECTORS.txt>`
* :download:`SPIN_DIRECTIONS.html (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/SPIN_DIRECTIONS.html>`
* :download:`HIGH-SYMMETRY_POINTS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/HIGH-SYMMETRY_POINTS.txt>`
* :download:`K-POINTS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/K-POINTS.txt>`
* :download:`K-POINTS.html (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/K-POINTS.html>`
* :download:`OMEGAS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/OMEGAS.txt>`
* :download:`OMEGAS.png (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/OMEGAS.png>`
* :download:`DELTAS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/DELTAS.txt>`
* :download:`DELTAS.png (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/DELTAS.png>`


Download the files for "CrI3_U/reference-GROGU.txt"
---------------------------------------------------

* :download:`console-output.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/console-output.txt>`
* :download:`SPIN_VECTORS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/SPIN_VECTORS.txt>`
* :download:`SPIN_DIRECTIONS.html (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/SPIN_DIRECTIONS.html>`
* :download:`HIGH-SYMMETRY_POINTS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/HIGH-SYMMETRY_POINTS.txt>`
* :download:`K-POINTS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/K-POINTS.txt>`
* :download:`K-POINTS.html (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/K-POINTS.html>`
* :download:`OMEGAS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/OMEGAS.txt>`
* :download:`OMEGAS.png (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/OMEGAS.png>`
* :download:`DELTAS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/DELTAS.txt>`
* :download:`DELTAS.png (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt/DELTAS.png>`


Customizing LSWT calculations
=============================

Now there are at least two problems with the calculations above:

*   Unexpected detected space group.

    The space group is detected correctly, but due to the small displacements of the
    atomic positions during the DFT optimization the structure is distorted, thus leading
    to the detection of the unexpected space group. Which in turn leads to the unexpected
    k-path and high-symmetry k-points in the reciprocal space.

*   Inclusion of the "out-of plane" k-path sections.

    Those sections are included even though the system is a monolayer. This is expected
    behavior as magnopy (through |wulfric|_) choses full recommended k-path. One can
    ask it for custom k-path using available list of k-points.

To correct those two problems we reduce the accuracy that is used by |spglib|_ (which
powers space group detection in |wulfric|_) and ask for the custom k-path with the commands

.. code-block:: bash

    magnopy-lswt -kp "GAMMA-K-M-GAMMA|A-H-L-A" -spg-s 1e-2 -ss GROGU -sf CrI3/reference-GROGU.txt -sd CrI3/optimize-sd-output/SPIN_DIRECTIONS.txt -hpd -of CrI3/lswt-output-customized > console-output.txt

and

.. code-block:: bash

    magnopy-lswt -kp "GAMMA-K-M-GAMMA|A-H-L-A" -spg-s 1e-2 -ss GROGU -sf CrI3_U/reference-GROGU.txt -sd CrI3_U/optimize-sd-output/SPIN_DIRECTIONS.txt -hpd -of CrI3_U/lswt-output-customized > console-output.txt

Input parameters
----------------

There are two extra parameter in the input

*   ``-kp "GAMMA-K-M-GAMMA|A-H-L-A"``

    Tells magnopy to use custom k-path. The syntax of this argument is typical, you can
    read about in |wulfric-kpath-string|_, for example.

*   ``-spg-s 1e-2``

    Tells magnopy to reduce precision for the space group to :math:`0.01` (default value
    was :math:`0.00001`).


Output files
------------

The set of output files is the same

*   "console-output.txt"

    .. literalinclude:: ../../resources/trilmax-2025/CrI3/lswt-customized/console-output.txt
        :caption: Content of "console-output.txt" for CrI3

*   "SPIN_VECTORS.txt"

    .. literalinclude:: ../../resources/trilmax-2025/CrI3/lswt-customized/SPIN_VECTORS.txt
        :caption: Content of "SPIN_VECTORS.txt" for CrI3

*   "SPIN_DIRECTIONS.html"

*   "HIGH-SYMMETRY_POINTS.txt"

    .. literalinclude:: ../../resources/trilmax-2025/CrI3/lswt-customized/HIGH-SYMMETRY_POINTS.txt
        :caption: Content of "HIGH-SYMMETRY_POINTS.txt" for CrI3

*   "K-POINTS.txt"

    .. dropdown:: Content of "K-POINTS.txt" for CrI3

        .. literalinclude:: ../../resources/trilmax-2025/CrI3/lswt-customized/K-POINTS.txt

*   "K-POINTS.html"

*   "OMEGAS.txt"

    .. dropdown:: Content of "OMEGAS.txt" for CrI3

        .. literalinclude:: ../../resources/trilmax-2025/CrI3/lswt-customized/OMEGAS.txt

*   "OMEGAS.png"

    .. image:: ../../resources/trilmax-2025/CrI3/lswt-customized/OMEGAS.png

*   "DELTAS.txt"

    .. dropdown:: Content of "DELTAS.txt" for CrI3

        .. literalinclude:: ../../resources/trilmax-2025/CrI3/lswt-customized/DELTAS.txt

*   "DELTAS.png"

    .. image:: ../../resources/trilmax-2025/CrI3/lswt-customized/DELTAS.png


Download the files for "CrI3/reference-GROGU.txt"
-------------------------------------------------

* :download:`console-output.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/console-output.txt>`
* :download:`SPIN_VECTORS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/SPIN_VECTORS.txt>`
* :download:`SPIN_DIRECTIONS.html (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/SPIN_DIRECTIONS.html>`
* :download:`HIGH-SYMMETRY_POINTS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/HIGH-SYMMETRY_POINTS.txt>`
* :download:`K-POINTS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/K-POINTS.txt>`
* :download:`K-POINTS.html (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/K-POINTS.html>`
* :download:`OMEGAS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/OMEGAS.txt>`
* :download:`OMEGAS.png (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/OMEGAS.png>`
* :download:`DELTAS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/DELTAS.txt>`
* :download:`DELTAS.png (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/DELTAS.png>`


Download the files for "CrI3_U/reference-GROGU.txt"
---------------------------------------------------

* :download:`console-output.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/console-output.txt>`
* :download:`SPIN_VECTORS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/SPIN_VECTORS.txt>`
* :download:`SPIN_DIRECTIONS.html (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/SPIN_DIRECTIONS.html>`
* :download:`HIGH-SYMMETRY_POINTS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/HIGH-SYMMETRY_POINTS.txt>`
* :download:`K-POINTS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/K-POINTS.txt>`
* :download:`K-POINTS.html (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/K-POINTS.html>`
* :download:`OMEGAS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/OMEGAS.txt>`
* :download:`OMEGAS.png (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/OMEGAS.png>`
* :download:`DELTAS.txt (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/DELTAS.txt>`
* :download:`DELTAS.png (for CrI3.txt) <../../resources/trilmax-2025/CrI3/lswt-customized/DELTAS.png>`
"""

# sphinx_gallery_thumbnail_path = 'img/gallery-thumbnails/trilmax-2025/black-box/lswt.png'
