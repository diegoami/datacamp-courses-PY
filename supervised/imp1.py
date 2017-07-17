import pandas as pd
import numpy as np
df =  pd.read_csv('../data/votes_2.csv')

# Convert '?' to NaN
#df[df == '?'] = np.nan
df.iloc[:,2:] = df.iloc[:,2:].apply(pd.to_numeric,errors='coerce')

#print(df)
# Print the number of NaNs
print(df.isnull().sum())

# Print shape of original DataFrame
print("Shape of Original DataFrame: {}".format(df.shape))

# Drop missing values and print shape of new DataFrame
df = df.dropna()

# Print shape of new DataFrame
print("Shape of DataFrame After Dropping All Rows with Missing Values: {}".format(df.shape))
