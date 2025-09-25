r"""
Spin-plotting routine (3D)
**************************

Here you will find a pre-defined function that can plot the set of spin directions from
vampire's output file as a 3D plot.

Definition of the plotting function
===================================

Execute the cell below to have the function defined
"""

import wulfric
import numpy as np
from tqdm import tqdm
import matplotlib


def plot_spins(
    filename,
    skip_spins=100,
    scale=2.0,
    color_mode="z",
    color_projection=None,
    colormap="bwr",
    vmin=None,
    vmax=None,
    spin_origin=0.5,
    xrange=None,
    yrange=None,
    zrange=None,
):
    # Check spin origin
    if not 0 <= spin_origin <= 1:
        raise ValueError(
            f"Misplaced spin origin, Expected 0 <= spin_origin <= 1, got {spin_origin}."
        )

    # Load data
    data = np.loadtxt(filename, skiprows=1)

    # Get cmap
    cmap = matplotlib.colormaps[colormap]

    # Skip some spins
    orig_shape = data.shape
    data = data[::skip_spins]

    print(
        f"Got {orig_shape[0]} spins, using every {skip_spins} ({data.shape[0]} spins in total)"
    )

    # Make a cut if needded
    if xrange is not None:
        data = data[xrange[0] <= data[:, 0]]
        data = data[data[:, 0] <= xrange[1]]
    if yrange is not None:
        data = data[yrange[0] <= data[:, 1]]
        data = data[data[:, 1] <= yrange[1]]
    if zrange is not None:
        data = data[zrange[0] <= data[:, 2]]
        data = data[data[:, 2] <= zrange[1]]

    print(f"Plotting {data.shape[0]} spins after the real-space cut")

    # Compute color values
    if color_mode == "z":
        color_projection = [0.0, 0.0, 1.0]
    elif color_mode == "y":
        color_projection = [0.0, 1.0, 0.0]
    elif color_mode == "x":
        color_projection = [1.0, 0.0, 0.0]
    elif color_mode == "projection":
        if color_projection is None:
            raise ValueError(
                f"Expected vector for color_projection, got '{color_projection}'"
            )
    else:
        raise ValueError(
            f"Expected 'z', 'y', 'x' or 'projection' for color_mode, got '{color_mode}'"
        )
    color_projection = color_projection / np.linalg.norm(color_projection)
    colors_values = data[:, 3:] @ color_projection

    # Get the normalizer for color values
    if vmin is None:
        vmin = colors_values.min()
    if vmax is None:
        vmax = colors_values.max()
    norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax)

    # Scale spin vectors
    data[:, 3:] = data[:, 3:] * scale * 20

    # Plot all vectors
    pe = wulfric.PlotlyEngine(_sphinx_gallery_fix=True)
    for i, (x, y, z, sx, sy, sz) in enumerate(tqdm(data)):
        pe.plot_vector(
            start_point=[
                x - spin_origin * sx,
                y - spin_origin * sy,
                z - spin_origin * sz,
            ],
            end_point=[
                x + (1 - spin_origin) * sx,
                y + (1 - spin_origin) * sy,
                z + (1 - spin_origin) * sz,
            ],
            color=matplotlib.colors.rgb2hex(cmap(norm(colors_values[i]))),
        )

    print("All spins are processed, starting to show the plot ...")
    print("Hint: zoom out in the plot if necessary.")

    # Change from default camera position
    camera = dict(
        up=dict(x=0, y=0, z=1),
        center=dict(
            x=np.mean(data[:, 0]), y=np.mean(data[:, 1]), z=np.mean(data[:, 2])
        ),
        eye=dict(x=data[:, 0].min(), y=data[:, 1].min(), z=2),
    )

    pe.fig.update_layout(scene_camera=camera)

    # Show the plot
    return pe.show(width=1000, height=1000)


# %%
# Explanation for the parameters
# ==============================
#
# You have to provide one parameter
#
# *   filename : str
#
#     Name of the file with spin positions and directions.
#
# Other parameters are optional and they allow to control the appearence of the plot:
#
# *   skip_spins : int, default 100
#
#     There is a lot of spins in the output file, to make the plot responsive one need to plot only every Nth spin. This option sets that number N.
#
# *   scale : float, default 1.0
#
#     This parameter controls the scale of the spin vectors length, play with this value for better-looking result. Increase to make spin vectors appear longer.
#
# *   color_mode : str, default "z"
#
#     What value to use for coloring of the spins. Supported:
#
#     * "z" - use z components
#     * "y" - use y components
#     * "x" - use x components
#     * "projection" - use projection along ``color_projection``.
#
# *   color_projection : (3,) array-like
#
#     Direction for the spin projection to use for coloring. Used if ``color_mode = "projection"``.
#
# *   colormap : str, default "bwr"
#
#     Any colormap supported by matplotlib. See https://matplotlib.org/stable/users/explain/colors/colormaps.html for supported names.
#
# *   vmin : float, optional
#
#     min value for color value normalization.
#
# *   vmax : float, optional
#
#     max value for color value normalization.
#
# *   spin_origin : float, default 0.5
#
#     Where shall spin vector start. If 0, then position is at the begining of the vector, if 0.5 - then position is in the middle of the vector, if 1 - then position is at the end of the vector.
#
# *   xrange : tuple of 2 float
#
#     Specifies the real-space range on the graph that is plotted. Use it to cut the regions that you want to plot.
#
# *   yrange : tuple of 2 float
#
#     Specifies the real-space range on the graph that is plotted. Use it to cut the regions that you want to plot.
#
# *   zrange : tuple of 2 float
#
#     Specifies the real-space range on the graph that is plotted. Use it to cut the regions that you want to plot.
#
# Plot with all values set to defaults
plot_spins("spins-00000020.txt")

# %%
# Plot a real-space cut with all sping in this region (i.e. skipping none) and reduce visible spin vector length
plot_spins(
    "spins-00000020.txt", xrange=(-20, 20), yrange=(-20, 20), skip_spins=1, scale=0.1
)

# %%
# Plot same as befor, but coloring according to the value of s_y
plot_spins(
    "spins-00000020.txt",
    xrange=(-20, 20),
    yrange=(-20, 20),
    skip_spins=1,
    scale=0.1,
    color_mode="y",
)


# sphinx_gallery_thumbnail_path = 'img/cat-numbers/2.png'
