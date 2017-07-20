import numpy as np
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
# Read the file into a DataFrame: df
airquality = pd.read_csv('../data/airquality.csv',low_memory=False,index_col=0)

# Calculate the mean of the Ozone column: oz_mean
oz_mean = airquality.Ozone.mean()

# Replace all the missing values in the Ozone column with the mean
airquality['Ozone'] = airquality['Ozone'].fillna(oz_mean)

# Print the info of airquality
print(airquality.info())
