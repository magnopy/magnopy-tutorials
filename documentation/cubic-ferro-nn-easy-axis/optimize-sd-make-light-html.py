import magnopy
from argparse import ArgumentParser
import numpy as np
import os

if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("-msdi", nargs=3, type=int)
    parser.add_argument("-sd", type=str)
    parser.add_argument("-i", type=str)
    parser.add_argument("-o", type=str)

    args = parser.parse_args()

    spinham = magnopy.io.load_grogu(filename=args.i)

    positions = np.array(spinham.magnetic_atoms.positions) @ spinham.cell
    filename = os.path.join(args.o, "SPIN_DIRECTIONS_LIGHT")

    spin_directions = np.loadtxt(args.sd)[np.newaxis, :]

    magnopy.io.plot_spin_directions(
        output_name=filename,
        positions=positions,
        spin_directions=spin_directions,
        unit_cell=spinham.cell,
        repeat=args.msdi,
        _full_plotly=False,
    )
