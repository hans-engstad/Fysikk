import numpy as np
import utils
import velocity
import curvature
import angle
import friction as friction_module
import normal_force as normal_force_module

"""
Calculate the absolute value of the ratio between friction and normal force in each of the 1400 steps 

|Friksjon / Normalkraft|
"""


def calculate():
    """Calculate the ratio, and return it as a list"""

    # Retrieve friction and normal force list
    friction = friction_module.calculate()
    normal_force = normal_force_module.calculate()

    # Calculate ratio
    ratio = []
    for i in range(len(friction)):
        value = np.abs(friction[i] / normal_force[i])
        ratio.append(value)

    return ratio


def main():
    """Method to execute when script is invoked"""

    # Retrieve ratio list
    ratio = calculate()

    # Plot the results
    utils.plot(
        ratio,
        y_min=0,
        y_max=0.3,
        x_label="x (m)",
        y_label="|f/N|",
        title="Forhold mellom friksjonskraft og normalkraft",
    )


# Snippet to run main function when script is executed
if __name__ == "__main__":
    main()
