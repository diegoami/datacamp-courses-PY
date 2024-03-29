import pandas as pd
# Read the CSV file into a DataFrame and sort the index: gapminder
gapminder_2010 = pd.read_csv('gapminder_2010.csv')

# Import zscore
from scipy.stats import zscore
# Group gapminder_2010: standardized
# Import zscore
from scipy.stats import zscore

# Group gapminder_2010: standardized
standardized = gapminder_2010.groupby('region')['life','fertility'].transform(zscore)

# Construct a Boolean Series to identify outliers: outliers
outliers = (standardized['life'] < -3) | (standardized['fertility'] > 3)

# Filter gapminder_2010 by the outliers: gm_outliers
gm_outliers = gapminder_2010.loc[outliers,:]

# Print gm_outliers
print(gm_outliers)


