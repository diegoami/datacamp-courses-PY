import numpy as np
import pandas as pd
#In [1]: ts0.to_csv(sys.stdout)

ts1 = pd.read_csv('ts1.csv',parse_dates=True,index_col="Dates" )
ts2 = pd.read_csv('ts2.csv',parse_dates=True,index_col="Dates" )



# Reset the index of ts2 to ts1, and then use linear interpolation to fill in the NaNs: ts2_interp
ts2_interp = ts2.reindex(ts1.index).interpolate(how="linear")

# Compute the absolute difference of ts1 and ts2_interp: differences
differences = np.abs(ts1-ts2_interp)

# Generate and print summary statistics of the differences
print(differences.describe())
print(ts2)
print(ts2_interp)