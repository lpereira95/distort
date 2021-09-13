import numpy as np

from distort.utils import get_bounds


def field1(x):
    """Applies a linear distortion in x and squares y.
    """
    x = x.copy()

    x[:, 0] *= 2
    x[:, 1] *= x[:, 1]

    return x


def field2(x):
    """Sums x to y.
    """
    x = x.copy()

    x[:, 1] += x[:, 0]

    return x


def field3(x):
    """Bends like a free-free beam.
    """
    x = x.copy()

    min_, max_ = get_bounds(x)
    x_min, x_max = min_[0], max_[0]

    x_mid = (x_max - x_min) / 2

    x[:, 1] += np.abs(x[:, 0] - x_mid)

    return x
