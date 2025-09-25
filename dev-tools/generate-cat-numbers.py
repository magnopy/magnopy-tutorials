import os
import matplotlib.pyplot as plt
import numpy as np

TAILLESS_CAT = [
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1],
    [0, 1, 1, 1, 1],
]
TAIL_ONE = [
    [0, 0, 1, 1, 0],
    [0, 1, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0],
]
TAIL_TWO = [
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
]
TAIL_THREE = [
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
]
ZERO = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
]
ONE = [
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
    [0, 1, 1, 1],
]
TWO = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 1, 1],
]
THREE = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
]
FOUR = [
    [0, 0, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 1, 1],
    [0, 0, 1, 0],
]
FIVE = [
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 1, 0],
]
SIX = [
    [0, 1, 1, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
]
SEVEN = [
    [1, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 0],
]
EIGHT = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
]
NINE = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
]

NUMBERS = [ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]


def plot_pixels(image, output_file):
    fig = plt.figure(figsize=(25, 18))
    ax = fig.add_axes((0, 0, 1, 1))

    ax.imshow(
        image,
        interpolation=None,
        vmin=0,
        vmax=1,
        cmap="binary",
    )

    ax.axis("off")

    fig.savefig(output_file, transparent=True, dpi=16)
    plt.close()


if __name__ == "__main__":
    # 0 - 9
    for number in range(0, 10):
        data = np.zeros((18, 25))
        data[:, :] = np.nan

        for i in range(len(TAILLESS_CAT)):
            for j in range(len(TAILLESS_CAT[i])):
                if TAILLESS_CAT[i][j]:
                    data[3 + i][7 + j] = TAILLESS_CAT[i][j]

        for i in range(len(TAIL_ONE)):
            for j in range(len(TAIL_ONE[i])):
                if TAIL_ONE[i][j]:
                    data[9 + i][12 + j] = TAIL_ONE[i][j]

        for i in range(len(NUMBERS[number])):
            for j in range(len(NUMBERS[number][i])):
                if NUMBERS[number][i][j]:
                    data[3 + i][13 + j] = NUMBERS[number][i][j]

        plot_pixels(
            image=data,
            output_file=os.path.join(
                "docs", "source", "img", "cat-numbers", f"{number}.png"
            ),
        )
        print(f"{number} done")

    # 10 - 99
    for number in range(10, 100):
        data = np.zeros((18, 25))
        data[:, :] = np.nan

        for i in range(len(TAILLESS_CAT)):
            for j in range(len(TAILLESS_CAT[i])):
                if TAILLESS_CAT[i][j]:
                    data[3 + i][5 + j] = TAILLESS_CAT[i][j]

        for i in range(len(TAIL_TWO)):
            for j in range(len(TAIL_TWO[i])):
                if TAIL_TWO[i][j]:
                    data[9 + i][10 + j] = TAIL_TWO[i][j]

        number1 = number // 10
        number2 = number % 10
        for i in range(len(NUMBERS[number1])):
            for j in range(len(NUMBERS[number1][i])):
                if NUMBERS[number1][i][j]:
                    data[3 + i][11 + j] = NUMBERS[number1][i][j]
        for i in range(len(NUMBERS[number2])):
            for j in range(len(NUMBERS[number2][i])):
                if NUMBERS[number2][i][j]:
                    data[3 + i][16 + j] = NUMBERS[number2][i][j]

        plot_pixels(
            image=data,
            output_file=os.path.join(
                "docs", "source", "img", "cat-numbers", f"{number}.png"
            ),
        )

        print(f"{number} done")

        # # 100 - 999
        # for number in range(100, 1000):
        #     data = np.zeros((18, 25))
        #     data[:, :] = np.nan

        #     for i in range(len(TAILLESS_CAT)):
        #         for j in range(len(TAILLESS_CAT[i])):
        #             if TAILLESS_CAT[i][j]:
        #                 data[3 + i][2 + j] = TAILLESS_CAT[i][j]

        #     for i in range(len(TAIL_THREE)):
        #         for j in range(len(TAIL_THREE[i])):
        #             if TAIL_THREE[i][j]:
        #                 data[9 + i][7 + j] = TAIL_THREE[i][j]

        #     number1 = number // 100
        #     number2 = number % 100 // 10
        #     number3 = number % 10
        #     for i in range(len(NUMBERS[number1])):
        #         for j in range(len(NUMBERS[number1][i])):
        #             if NUMBERS[number1][i][j]:
        #                 data[3 + i][8 + j] = NUMBERS[number1][i][j]
        #     for i in range(len(NUMBERS[number2])):
        #         for j in range(len(NUMBERS[number2][i])):
        #             if NUMBERS[number2][i][j]:
        #                 data[3 + i][13 + j] = NUMBERS[number2][i][j]
        #     for i in range(len(NUMBERS[number3])):
        #         for j in range(len(NUMBERS[number3][i])):
        #             if NUMBERS[number3][i][j]:
        #                 data[3 + i][18 + j] = NUMBERS[number3][i][j]

        #     plot_pixels(
        #         image=data,
        #         output_file=os.path.join(
        #             "docs", "source", "img", "cat-numbers", f"{number}.png"
        #         ),
        #     )

        print(f"{number} done")
