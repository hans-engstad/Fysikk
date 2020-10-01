import numpy as np
import utils
import velocity
import curvature
import angle

"""
Calculate the normal force in each of the 1400 steps (Normalkraft)
"""


def calculate():
    """Calculate the normal force, and return it as a list"""

    # Define some constants
    g = 9.81  # Gravity constant
    m = 0.0278  # Mass of ball (TODO: Insert correct mass)

    v = velocity.calculate()
    k = curvature.calculate()
    beta = angle.calculate()

    n = []
    for i in range(len(v)):
        # Calculate centripetal acceleration in this point (Sentripetalakselerasjon)
        a = v[i] ** 2 * k[i]

        # Calucalte normal force in this point
        current_n = m * (g * np.cos(beta[i]) + a)

        # Append value to the results
        n.append(current_n)

    return n


def main():
    """Method to execute when script is invoked"""

    # Retrieve normal force list
    n = calculate()

    # Plot the results
    utils.plot(
        n, y_min=0, y_max=40, x_label="x (m)", y_label="N (N)", title="Normalkraft"
    )


# Snippet to run main function when script is executed
if __name__ == "__main__":
    main()
