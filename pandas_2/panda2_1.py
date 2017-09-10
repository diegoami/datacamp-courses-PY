# Import cars data
import pandas as pd
cars = pd.read_csv('../data/cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']
print(dr)

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)