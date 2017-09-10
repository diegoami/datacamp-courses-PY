

# Import cars data
import pandas as pd
cars = pd.read_csv('../data/cars.csv', index_col = 0)

# Convert code to a one-liner
dr = cars['drives_right']
sel = cars[dr]

# Print sel
print(cars[cars['drives_right']])