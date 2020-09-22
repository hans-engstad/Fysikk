import numpy as np
import utils

"""
Calculate the angle of inclination of the track in each of the 1400 steps (Helningsvinkel)
"""

# Retrieve the derivative of y
dy = utils.get_dy()

# Caluclate angles using numpys arctan function
beta = np.arctan(dy)

# Plot the results
utils.plot(beta, y_min=-0.5, y_max=0.5)

