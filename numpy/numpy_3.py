# height and weight are available as a regular lists

# Import numpy
import numpy as np
height = [170,156,190]
weight = [72,59,84]

# Create array from height with correct units: np_height_m
np_height_m = np.array(height) * 0.0254

# Create array from weight with correct units: np_weight_kg
np_weight_kg = np.array(weight) * 0.453592

# Calculate the BMI: bmi
bmi = np_weight_kg / np_height_m ** 2 

# Print out bmi
print(bmi)
