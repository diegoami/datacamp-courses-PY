# Import numpy and pandas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Read the CSV file into a DataFrame: df
df = pd.read_csv('../data/gapminder_2.csv')
sns.heatmap(df.corr(), square=True, cmap='RdYlGn')
plt.show()
print(np.mean(df['life']))
print(type(df['fertility']))
print(df.info())