import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline


def get_curves():
    h = 200
    xfast = np.asarray([0, h, 2 * h, 3 * h, 4 * h, 5 * h, 6 * h, 7 * h])
    yfast = [0.293, 0.24, 0.216, 0.159, 0.082, 0.053, 0.097, 0.136]

    xfast = xfast / 1000

    cs = CubicSpline(xfast, yfast, bc_type="natural")
    xmin = 0.000
    xmax = 1.401
    dx = 0.001
    x = np.arange(xmin, xmax, dx)
    Nx = len(x)
    y = cs(x)
    dy = cs(x, 1)
    d2y = cs(x, 2)

    return (y, dy, d2y)


def get_y():
    return get_curves()[0]


def get_dy():
    return get_curves()[1]


def get_d2y():
    return get_curves()[2]


def plot(
    y,
    x=np.arange(0.000, 1.401, 0.001),
    y_min=-1,
    y_max=1,
    title="Plot",
    x_unit="m",
    y_unit="m",
):
    baneform = plt.figure("y(x)", figsize=(12, 3))
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel("$x$ (" + x_unit + ")", fontsize=20)
    plt.ylabel("$y(x)$ (" + y_unit + ")", fontsize=20)
    plt.ylim(y_min, y_max)
    plt.grid()
    plt.show()

