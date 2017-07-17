# Import pandas
import pandas as pd
from matplotlib import pyplot as plt

# Read 'gapminder.csv' into a DataFrame: df
df = pd.read_csv('../data/gapminder_4.csv')

# Create a boxplot of life expectancy per region
df.boxplot('life', 'Region', rot=60)

# Show the plot
plt.show()
