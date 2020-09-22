import numpy as np
import utils

"""
Calculate the curvature in each of the 1400 steps (Krumning)
"""

# Retrieve derivative and 2nd derivative of y
dy = utils.get_dy()
d2y = utils.get_d2y()


k = []  # The curvature
for i in range(len(utils.get_y())):  # Iterate over all y elements with i as the index
    value = d2y[i] / (1 + dy[i] ** 2) ** (3 / 2)
    k.append(value)

# Plot the results
utils.plot(k, y_min=-2, y_max=3)
