import numpy as np
import utils

"""
Calculate the velocity in each of the 1400 steps (Hastighet)
"""


def calculate():
    """Calculate the velocity, and return it as a list"""

    # Define some constants
    g = 9.81  # Gravity constant
    c = 0.5  # Mass distribution constant

    # Retrieve the starting y position
    first_y = utils.get_y()[0]

    # Calculate speed in all positions
    v = []
    for current_y in utils.get_y():
        y_diff = first_y - current_y  # Difference from this y to first y
        value = np.sqrt(2 * g * y_diff / (1 + c))  # Value for speed in this position
        v.append(value)

    return v


def main():
    """Method to execute when script is invoked"""

    # Retrieve velocity list
    v = calculate()

    # Plot the results
    utils.plot(
        v,
        y_min=0,
        y_max=3.5,
        x_label="x (m)",
        y_label="v (m/s)",
        title="Hastighet som funksjon av horisontal posisjon",
    )


# Snippet to run main function when script is executed
if __name__ == "__main__":
    main()
