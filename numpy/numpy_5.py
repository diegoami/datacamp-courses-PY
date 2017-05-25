# height and weight are available as a regular lists

# Import numpy
import numpy as np
height = [170,156,190]
weight = [72,59,84]

# Store weight and height lists as numpy arrays
np_weight = np.array(weight)
np_height = np.array(height)

# Print out the weight at index 50
print(np_weight[2])

# Print out sub-array of np_height: index 100 up to and including index 110
print(np_height[0:2])