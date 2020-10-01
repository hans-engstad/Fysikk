import numpy as np
import utils
import velocity
import curvature
import angle
import x_position

"""
Calculate the velocity as a function of time in each of the 1400 steps 

(Hastighet som funksjon av tiden)
"""


def calculate():
    """
    Calculate velocity at time t, and return it as a list. 

    Returns: [v_0, v_1, ..., v_n] where n=1400

    v_i = velocity at time t_i
    """

    # Define some constants
    delta_x = 0.001  # Horizontal distance between each step

    # Retrieve time list
    time = x_position.calculate_time()

    v = []
    for i in range(len(time)):
        if i == 0:
            # Avoid division by zero for first step
            v.append(0)
            continue

        current_time = time[i]
        current_position = delta_x * i

        value = current_position / current_time
        v.append(value)

    return v


def main():
    """Method to execute when script is invoked"""

    # Retrieve velocity as function of time
    v = calculate()

    # Retroeve list of times
    time = x_position.calculate_time()

    # Plot the results
    utils.plot(
        y=v,
        x=time,
        y_min=0,
        y_max=2,
        x_label="t (s)",
        y_label="v (m/s)",
        title="Hastighet som funksjon av tiden",
    )


# Snippet to run main function when script is executed
if __name__ == "__main__":
    main()
