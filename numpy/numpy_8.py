# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np


# Create np_baseball (2 cols)
np_baseball = np.array(baseball)


# Print out addition of np_baseball and updated
print(np_baseball)

# Create Numpy array: conversion
conversion = np.array([0.0254, 0.453592, 1])

# Print out product of np_baseball and conversion
print(conversion * np_baseball )