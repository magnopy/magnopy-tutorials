:orphan:

.. _trilmax-2025:

*********************
TRILMAX summer school 
*********************

**Dates**: 8-12 September of 2025
**Target magnopy's version**: v0.2.1

This tutorial was given in the |TRILMAX-summer-school|_ organized by the
|TRILMAX-consortium|_.

:download:`Slides from the school <../resources/trilmax-2025/Magnopy.pptx>`





.. raw:: html

    <div class="sphx-glr-thumbnails">

.. thumbnail-parent-div-open

.. thumbnail-parent-div-close

.. raw:: html

    </div>

Magnopy as a python library
===========================

Every page of the tutorial explains some concepts about the |magnopy|_. There is a list
of "Tutorial tasks", that can be found on top of each tutorial page, that are meant for
you to complete. The tasks are connected to the content that you find in each page. The
idea is to read the list of tasks first and then to read the page and referenced
materials, when they are noted and try to complete the task.



.. raw:: html

    <div class="sphx-glr-thumbnails">

.. thumbnail-parent-div-open

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="       Install magnopy        Check that you have version 0.2.0 available">

.. only:: html

  .. image:: /trilmax-2025/1_python-library/images/thumb/sphx_glr_plot_1_introduction_thumb.png
    :alt:

  :ref:`sphx_glr_trilmax-2025_1_python-library_plot_1_introduction.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Introducing magnopy</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="       Create a crystal structure for the material of your choosing.         Create a cell and a set of atoms. Specify all mentioned properties for each atom.        (extra) Visualize your structure using :external:pymagnopy.PlotlyEngine     *   (extra) Get conventional and primitive cell of your structure (see         :external:pywulfric.crystal.get_primitive and         :external:pywulfric.crystal.get_conventional). Visualize them. Are they         they the same for your crystal? Shall they be the same always or not?">

.. only:: html

  .. image:: /trilmax-2025/1_python-library/images/thumb/sphx_glr_plot_2_crystal_thumb.png
    :alt:

  :ref:`sphx_glr_trilmax-2025_1_python-library_plot_2_crystal.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Crystal structure</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="       Create an instance of :external:pymagnopy.Convention for every example         mathematical formula that is written in this page.        (extra) Write down the spin Hamiltonian in the convention that you usually use         or seen recently in some paper. Create an instance of the         :external:pymagnopy.Convention that describe it.">

.. only:: html

  .. image:: /trilmax-2025/1_python-library/images/thumb/sphx_glr_plot_3_convention_thumb.png
    :alt:

  :ref:`sphx_glr_trilmax-2025_1_python-library_plot_3_convention.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Convention of spin Hamiltonian</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="       Create a spin Hamiltonian of the orthorhombic ferromagnet with tree magnetic axes         (easy, medium and hard).        Change the convention of the spin Hamiltonian. Inspect how the parameters are         changing when you do so.        Add some magnetic field to it. CCheck the values of the parameters of the         Hamiltonian that store the magnetic field.        Add magnetic dipole-dipole interaction. Test both energy and distance cut-offs.         Which parameters of the spin Hamiltonian change?">

.. only:: html

  .. image:: /trilmax-2025/1_python-library/images/thumb/sphx_glr_plot_4_spinham_thumb.png
    :alt:

  :ref:`sphx_glr_trilmax-2025_1_python-library_plot_4_spinham.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Spin Hamiltonian</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip=" .. admonition:: Tutorial tasks">

.. only:: html

  .. image:: /trilmax-2025/1_python-library/images/thumb/sphx_glr_plot_5_energy_thumb.png
    :alt:

  :ref:`sphx_glr_trilmax-2025_1_python-library_plot_5_energy.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Classical Energy</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip=" .. admonition:: Tutorial tasks">

.. only:: html

  .. image:: /trilmax-2025/1_python-library/images/thumb/sphx_glr_plot_6_wulfric_thumb.png
    :alt:

  :ref:`sphx_glr_trilmax-2025_1_python-library_plot_6_wulfric.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">(extra) K-points with wulfric</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="     Use one of the spin Hamiltonians from the previous tutorial and compute all terms \       of the magnon Hamiltonian.      Compute magnon dispersion of a simple ferromagnet.     * Compute magnon dispersion of a simple antiferromagnetic.">

.. only:: html

  .. image:: /trilmax-2025/1_python-library/images/thumb/sphx_glr_plot_7_lswt_thumb.png
    :alt:

  :ref:`sphx_glr_trilmax-2025_1_python-library_plot_7_lswt.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Linear Spin Wave theory</div>
    </div>


.. thumbnail-parent-div-close

.. raw:: html

    </div>

Magnopy as a black box
======================

Alternative way to use magnopy, that does not require knowledge of Python is through
its command line interface.

First, one need to install magnopy. Open a terminal and run the following in it

.. code-block:: bash

    pip install "magnopy[visual]"

Check that everything is ok by executing the command

.. code-block:: bash

    magnopy

There are currently two command line scripts in magnopy. Use the |GROGU|_ file that you have
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

    <div class="sphx-glr-thumbcontainer" tooltip="       Display list of all available parameters for the script.        Optimize the Hamiltonian and inspect the output files.        Optimize the Hamiltonian on several super-cells.         Are there any changes of the ground state?        Optimize with different directions and value of the external magnetic field.         How does the result changes?">

.. only:: html

  .. image:: /trilmax-2025/2_black-box/images/thumb/sphx_glr_plot_1_optimize-sd_thumb.png
    :alt:

  :ref:`sphx_glr_trilmax-2025_2_black-box_plot_1_optimize-sd.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Optimization of spin directions</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="       Display list of all available parameters for the script.        Run the script and examine the output. Is the space group the one you would expect?         If not, than try to reduce --spglib-symprec and check if it changes.        Use spin directions file from the results of magnopy.optimize-sd to execute         this script.        Compute magnon dispersion for the custom k-path (Use only in-plane         high-symmetry points).">

.. only:: html

  .. image:: /trilmax-2025/2_black-box/images/thumb/sphx_glr_plot_2_lswt_thumb.png
    :alt:

  :ref:`sphx_glr_trilmax-2025_2_black-box_plot_2_lswt.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Linear Spin Wave theory</div>
    </div>


.. thumbnail-parent-div-close

.. raw:: html

    </div>

Preparing files for Vampire
===========================

This tutorial gives instructions on how to get .UCF and .mat files from |GROGU|_ file
using magnopy.


.. raw:: html

    <div class="sphx-glr-thumbnails">

.. thumbnail-parent-div-open

.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="This tutorial is a special one - it does not require you to finish any task and give all the code that you need to execute. You can get a notebook for this tutorial in the Tutorial_2/magnopy-vampire-link folder.">

.. only:: html

  .. image:: /trilmax-2025/3_Vampire_link/images/thumb/sphx_glr_plot_0_convert_thumb.png
    :alt:

  :ref:`sphx_glr_trilmax-2025_3_Vampire_link_plot_0_convert.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Getting files for Vampire</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Here you will find a pre-defined function that can plot the set of spin directions from vampire&#x27;s output file as a 2D plot.">

.. only:: html

  .. image:: /trilmax-2025/3_Vampire_link/images/thumb/sphx_glr_plot_1_spins_2d_thumb.png
    :alt:

  :ref:`sphx_glr_trilmax-2025_3_Vampire_link_plot_1_spins_2d.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Spin-plotting routine (2D)</div>
    </div>


.. raw:: html

    <div class="sphx-glr-thumbcontainer" tooltip="Here you will find a pre-defined function that can plot the set of spin directions from vampire&#x27;s output file as a 3D plot.">

.. only:: html

  .. image:: /trilmax-2025/3_Vampire_link/images/thumb/sphx_glr_plot_2_spins_3d_thumb.png
    :alt:

  :ref:`sphx_glr_trilmax-2025_3_Vampire_link_plot_2_spins_3d.py`

.. raw:: html

      <div class="sphx-glr-thumbnail-title">Spin-plotting routine (3D)</div>
    </div>


.. thumbnail-parent-div-close

.. raw:: html

    </div>


.. toctree::
   :hidden:
   :includehidden:


   /trilmax-2025/1_python-library/index.rst
   /trilmax-2025/2_black-box/index.rst
   /trilmax-2025/3_Vampire_link/index.rst


.. only:: html

  .. container:: sphx-glr-footer sphx-glr-footer-gallery

    .. container:: sphx-glr-download sphx-glr-download-python

      :download:`Download all examples in Python source code: trilmax-2025_python.zip </trilmax-2025/trilmax-2025_python.zip>`

    .. container:: sphx-glr-download sphx-glr-download-jupyter

      :download:`Download all examples in Jupyter notebooks: trilmax-2025_jupyter.zip </trilmax-2025/trilmax-2025_jupyter.zip>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
