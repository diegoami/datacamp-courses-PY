from data.cars import cars_df as df
from data.cars import sizes
import matplotlib.pyplot as plt
# Make a list of the column names to be plotted: cols
cols = ['weight', 'mpg']

# Generate the box plots
df[cols].plot(kind='box',subplots=True)

# Display the plot
plt.show()
