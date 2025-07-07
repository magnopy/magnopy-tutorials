import magnopy
from argparse import ArgumentParser
import numpy as np
import os

if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("-supercell", nargs=3, type=int)
    parser.add_argument("-sd", type=str)
    parser.add_argument("-sp", type=str)
    parser.add_argument("-i", type=str)
    parser.add_argument("-o", type=str)

    args = parser.parse_args()

    spinham = magnopy.io.load_grogu(filename=args.i)

    filename = os.path.join(args.o, "SPIN_DIRECTIONS_LIGHT")

    positions = np.loadtxt(args.sp)
    spin_directions = np.loadtxt(args.sd)

    magnopy.io.plot_spin_directions(
        output_name=filename,
        positions=positions,
        spin_directions=spin_directions,
        cell=spinham.cell,
        highlight=[i for i in range(spinham.M)],
        name_highlighted="Original unit cell",
        name_other="Other unit cells",
        _full_plotly=False,
    )
