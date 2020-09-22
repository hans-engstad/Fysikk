import numpy as np
import utils
import velocity
import curvature
import angle

"""
Calculate the friction force in each of the 1400 steps (Friksjonskraft)
"""


def calculate():
    """Calculate the friction, and return it as a list"""

    # Define some constants
    g = 9.81  # Gravity constant
    c = 1.5  # Mass distribution constant
    m = 2  # Mass of ball (TODO: Insert correct mass)

    # Retrieve angle of inclination (Helningsvinkel)
    beta = angle.calculate()

    friction = []
    for current_beta in beta:
        # Calculate friction for current point
        value = c * m * g * np.sin(current_beta) / (1 + c)

        # Append current point to list
        friction.append(value)

    return friction


def main():
    """Method to execute when script is invoked"""

    # Retrieve friction list
    friction = calculate()

    # Plot the results
    utils.plot(
        friction,
        y_min=-5,
        y_max=4,
        x_label="x (m)",
        y_label="Friksjon (N)",
        title="Friksjon",
    )


# Snippet to run main function when script is executed
if __name__ == "__main__":
    main()
