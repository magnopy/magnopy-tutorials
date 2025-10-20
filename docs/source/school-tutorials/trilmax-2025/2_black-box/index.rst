

.. _sphx_glr_school-tutorials_trilmax-2025_2_black-box:

Magnopy as a black box
======================

Magnopy can be used without any knowledge of Python programming. In other words it can be
used as a black-box software via its command line interface.

First, one need to install magnopy. Open a terminal and run the following command (type 
the command and press enter)

.. code-block:: bash

    pip install "magnopy[visual]"

Check that everything is ok by executing the command

.. code-block:: bash

    magnopy

There are currently two command line scripts in magnopy. Use |GROGU|_ file that you have
obtained to follow the tutorial for each of them.

.. hint::
    Those scripts can be run from within python as well, see:
    |magnopy-scenarios|_. One can study the source code of
    :external:py:func:`magnopy.scenarios.optimize_sd` and
    :external:py:func:`magnopy.scenarios.solve_lswt` for more advance example of how
    magnopy can be used as a python library.






.. raw:: html

    <div class="sphx-glr-thumbnails">

.. thumbnail-parent-div-open

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="       Display list of all available parameters for the script.        Optimize the Hamiltonian and inspect the output files.        Optimize the Hamiltonian on several super-cells. Are there any changes of the         ground state?        Optimize with different directions and values of the external magnetic field.         How does the result change?">

.. only:: html

  .. image:: /school-tutorials/trilmax-2025/2_black-box/images/thumb/sphx_glr_plot_1_optimize-sd_thumb.png
    :alt:

  :ref:`sphx_glr_school-tutorials_trilmax-2025_2_black-box_plot_1_optimize-sd.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Optimization of spin directions</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="       Display list of all available parameters for the script.        Run the script and examine the output. Is the space group the one you would expect?         If not, than try to increase --spglib-symprec and check if it changes.        Use spin directions file from the results of magnopy.optimize-sd to execute         this script.        Compute magnon dispersion for the custom k-path (Use only in-plane         high-symmetry points).">

.. only:: html

  .. image:: /school-tutorials/trilmax-2025/2_black-box/images/thumb/sphx_glr_plot_2_lswt_thumb.png
    :alt:

  :ref:`sphx_glr_school-tutorials_trilmax-2025_2_black-box_plot_2_lswt.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Linear Spin Wave theory</div>
    </div>


.. thumbnail-parent-div-close

.. raw:: html

    </div>


.. toctree::
   :hidden:

   /school-tutorials/trilmax-2025/2_black-box/plot_1_optimize-sd
   /school-tutorials/trilmax-2025/2_black-box/plot_2_lswt

