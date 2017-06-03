# Import pandas
import pandas as pd

# Create the list of file names: filenames
filenames = ['../data/Gold.csv', '../data/Silver.csv', '../data/Bronze.csv']

# Create the list of three DataFrames: dataframes
dataframes = []
for filename in filenames:
    dataframes.append(pd.read_csv(filename))

# Print top 5 rows of 1st DataFrame in dataframes
print(dataframes[0].head())