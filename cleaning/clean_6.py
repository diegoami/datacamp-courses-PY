
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
# Read the file into a DataFrame: df
airquality = pd.read_csv('../data/airquality.csv',low_memory=False,index_col=0)
# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')

# Print the head of airquality_melt
print(airquality_melt.head())

print(airquality_melt)

