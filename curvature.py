import numpy as np
import utils

"""
Calculate the curvature in each of the 1400 steps (Krumning)
"""


def calculate():
    """Calculate the curvature, and return it as a list"""

    # Retrieve derivative and 2nd derivative of y
    dy = utils.get_dy()
    d2y = utils.get_d2y()

    k = []  # The curvature
    for i in range(
        len(utils.get_y())
    ):  # Iterate over all y elements with i as the index
        value = d2y[i] / (1 + dy[i] ** 2) ** (3 / 2)
        k.append(value)

    return k


def main():
    """Method to execute when script is invoked"""

    # Retrieve curvature list
    k = calculate()

    # Plot the results
    utils.plot(k, y_min=-2, y_max=3)


# Snippet to run main function when script is executed
if __name__ == "__main__":
    main()
