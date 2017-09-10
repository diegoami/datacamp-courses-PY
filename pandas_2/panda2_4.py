# Import cars data
import pandas as pd
cars = pd.read_csv('../data/cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
medium = cars[np.logical_and( cars['cars_per_cap'] > 100 , cars['cars_per_cap'] < 500 ) ]

# Print medium
print(medium)

# Create medium: observations with cars_per_cap between 100 and 500
#medium2 = cars[cars['cars_per_cap'] > 100 & cars['cars_per_cap'] < 500  ]

# Print medium
#print(medium2)
s = cars['cars_per_cap'] > 100
print(s.values)
# Create medium: observations with cars_per_cap between 100 and 500
medium3 = cars[(cars['cars_per_cap'] > 100).values & (cars['cars_per_cap'] < 500).values ]

# Print medium
print(medium3)

medium4 = cars[s ]

# Print medium
print(medium4)