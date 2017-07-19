
import numpy as np
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
# Read the file into a DataFrame: df
airquality = pd.read_csv('../data/airquality.csv',low_memory=False,index_col=0)
# Print the head of airquality
#print(airquality.head())
airquality_dup = pd.read_csv('../data/airquality_dup.csv',low_memory=False,index_col=0)
# Print the head of airquality
#print(airquality.head())

# Pivot airquality_dup: airquality_pivot
airquality_pivot = airquality_dup.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading', aggfunc=np.mean)

# Reset the index of airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

# Print the head of airquality_pivot
print(airquality_pivot.head())

# Print the head of airquality
print(airquality.head())
