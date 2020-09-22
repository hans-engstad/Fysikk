import numpy as np
import utils
import velocity
import curvature
import angle

"""
Calculate the horizontal/x position as a function of time in each of the 1400 steps 

(Horisontal posisjon som funksjon av tiden)
"""


def calculate_time():
    """
    Calculate time it takes to position x, and return it as a list. 

    Returns: [t_0, t_1, ..., t_n] where n=1400

    t_i = time it takes to position x_i
    """

    # Define some constants
    delta_x = 0.001  # Horizontal distance between each step

    # Retrieve angle of inclination and velocity
    beta = angle.calculate()
    v = velocity.calculate()

    # Find time as function of position t(x)
    t_x = []
    for i in range(len(v)):
        if i == 0:
            # First point is reached after 0 seconds
            t_x.append(0)
            continue

        # Calculate average of horizontal velocity
        prev_v_x = v[i - 1] * np.cos(beta[i - 1])
        current_v_x = v[i] * np.cos(beta[i])
        average_v_x = 0.5 * (prev_v_x + current_v_x)

        # Calculate time estimate from previous to current position
        delta_t_n = delta_x / average_v_x

        # Calculate cumulative time value
        value = t_x[-1] + delta_t_n

        # Append value to list
        t_x.append(value)

    return t_x


def main():
    """Method to execute when script is invoked"""

    # Retrieve time list
    time = calculate_time()

    # Plot the results
    utils.plot(
        y=np.arange(0.000, 1.401, 0.001),
        x=time,
        y_min=0,
        y_max=1.5,
        x_label="t (s)",
        y_label="x (m)",
        title="Horisontal posisjon som funksjon av tiden",
    )


# Snippet to run main function when script is executed
if __name__ == "__main__":
    main()
