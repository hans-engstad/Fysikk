import numpy as np
import utils
import velocity
import curvature
import angle
import matplotlib.pyplot as plt
import matplotlib

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


def get_experiment():

    time = [
        0,
        0.03333333333,
        0.06666666667,
        0.1,
        0.1333333333,
        0.1666666667,
        0.2,
        0.2333333333,
        0.2666666667,
        0.3,
        0.3333333333,
        0.3666666667,
        0.4,
        0.4333333333,
        0.4666666667,
        0.5,
        0.5333333333,
        0.5666666667,
        0.6,
        0.6333333333,
        0.6666666667,
        0.7,
        0.7333333333,
        0.7666666667,
        0.8,
        0.8333333333,
        0.8666666667,
        0.9,
        0.9333333333,
        0.9666666667,
        1,
        1.033333333,
        1.066666667,
        1.1,
        1.133333333,
        1.166666667,
        1.2,
        1.233333333,
        1.266666667,
        1.3,
        1.333333333,
        1.366666667,
        1.4,
        1.433333333,
        1.466666667,
        1.5,
        1.533333333,
        1.566666667,
    ]

    x_position = [
        0.006768725204,
        0.005022002841,
        0.01102455449,
        0.01707094468,
        0.02419084458,
        0.03200421107,
        0.04179375293,
        0.05265668736,
        0.06366585831,
        0.07655670714,
        0.0913282362,
        0.1048197224,
        0.1215916356,
        0.138854748,
        0.1575953683,
        0.1788784337,
        0.2016086266,
        0.2251856154,
        0.2536158687,
        0.2810610777,
        0.3082865671,
        0.335112329,
        0.3633056609,
        0.3910175414,
        0.4183248516,
        0.4475351368,
        0.4780782671,
        0.5092449823,
        0.5431467613,
        0.5783391066,
        0.6162009904,
        0.6563707218,
        0.698559518,
        0.7456729837,
        0.7918070079,
        0.841200463,
        0.8916299165,
        0.9425861485,
        0.9920823032,
        1.041011856,
        1.085439649,
        1.12802419,
        1.167041762,
        1.206691359,
        1.243476115,
        1.279196564,
        1.314022934,
        1.345801494,
    ]
    return time, x_position


def main():
    """Method to execute when script is invoked"""

    experiment_time, experiment_position = get_experiment()

    # Plot the results
    plt.plot(calculate_time(), np.arange(0.000, 1.401, 0.001), label="Simulering")
    plt.plot(
        experiment_time,
        experiment_position,
        label="Eksperiment 1",
        marker=".",
        linestyle="none",
    )
    plt.legend()
    plt.title("X-Posisjon som funksjon av tiden")
    plt.xlabel("t (s)", fontsize=20)
    plt.ylabel("x (m)", fontsize=20)
    plt.ylim(0, 2)
    plt.grid()
    plt.gcf().subplots_adjust(bottom=0.3, left=0.2)
    plt.show()


# Snippet to run main function when script is executed
if __name__ == "__main__":
    main()
