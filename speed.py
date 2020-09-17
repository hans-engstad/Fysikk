import numpy as np
import utils

# Define some constants
g = 9.81  # Gravity constant
c = 1.5  # Mass distribution constant

# Retrieve the starting y position
first_y = utils.get_y()[0]

# Calculate speed in all positions
v = []
for current_y in utils.get_y():
    y_diff = first_y - current_y  # Difference from this y to first y
    value = np.sqrt(2 * g * y_diff / c)  # Value for speed in this position
    v.append(value)

# Plot the results
utils.plot(v, y_min=0, y_max=2.5)
