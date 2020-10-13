import numpy as np
import utils
import velocity
import curvature
import angle
import x_position
import matplotlib.pyplot as plt
import matplotlib

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


def get_experiment_data():
    """
    Return data captured during experiment
    
    Fra Økt 3 dokument: 
    Tidsutviklingen på den andre siden, er mer interessant i et kvalitativt 
    perspektiv, vi sammenligner derfor én utvalgt gjennomkjøring med simuleringen.

    Ser dermed kun på det første forsøket (Video 1)

    """

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
    ]
    velocity = [
        0,
        0.07317533134,
        0.1810987419,
        0.1976817387,
        0.2271770015,
        0.273938999,
        0.317849928,
        0.3378953688,
        0.3675408377,
        0.4226351624,
        0.4386357352,
        0.4700202691,
        0.524117347,
        0.5594120112,
        0.6213424976,
        0.6779588559,
        0.7104225487,
        0.7895118691,
        0.8427986279,
        0.8236527585,
        0.8141777874,
        0.8294510109,
        0.8421395858,
        0.834720757,
        0.8697099874,
        0.9225860991,
        0.9636905011,
        1.025644877,
        1.099176876,
        1.178818706,
        1.274513869,
        1.348949099,
        1.432742482,
        1.464288609,
        1.482338778,
        1.530667618,
        1.528266269,
        1.506792026,
        1.48366947,
        1.433161748,
        1.350788179,
        1.255469103,
        1.195311137,
        1.157875644,
        1.105170895,
        1.091130227,
        1.043980488,
    ]

    return time, velocity


def main():
    """Method to execute when script is invoked"""

    # Retrieve velocity as function of time
    simulation_velocity = calculate()

    # Retrive list of times
    simulation_time = x_position.calculate_time()

    experiment_time, experiment_velocity = get_experiment_data()

    baneform = plt.figure("y(x)", figsize=(12, 3))
    plt.plot(simulation_time, simulation_velocity, label="Simulering")
    plt.plot(
        experiment_time,
        experiment_velocity,
        label="Eksperiment 1",
        marker=".",
        linestyle="none",
    )
    plt.legend()
    plt.title("Hastighet som funksjon av tiden")
    plt.xlabel("t (s)", fontsize=20)
    plt.ylabel("v (m/s)", fontsize=20)
    plt.ylim(0, 2)
    plt.grid()
    plt.gcf().subplots_adjust(bottom=0.3, left=0.2)
    plt.show()


# Snippet to run main function when script is executed
if __name__ == "__main__":
    main()
