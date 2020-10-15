import numpy as np
import utils

"""
Calculate the angle of inclination of the track in each of the 1400 steps (Helningsvinkel)
"""


def calculate():
    """Calculate the angle, and return it as a list"""

    # Retrieve the derivative of y
    dy = utils.get_dy()

    # Caluclate angles using numpys arctan function
    beta = np.arctan(dy)

    return beta


def main():
    """Method to execute when script is invoked"""

    # Retrieve angle list
    beta = calculate()

    # Plot the results
    utils.plot(
        beta,
        y_min=-0.5,
        y_max=0.5,
        x_label="x (m)",
        y_label="β (rad)",
        title="Banens helningsvinkel",
    )


# Snippet to run main function when script is executed
if __name__ == "__main__":
    main()
