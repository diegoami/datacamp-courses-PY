from data.cars import cars_df as df
from data.cars import sizes
import matplotlib.pyplot as plt
# Create a list of y-axis column names: y_columns
# Generate a scatter plot
df.plot(kind='scatter', x='hp', y='mpg',s=sizes)

# Add the title
plt.title('Fuel efficiency vs Horse-power')

# Add the x-axis label
plt.xlabel('Horse-power')

# Add the y-axis label
plt.ylabel('Fuel efficiency (mpg)')

# Display the plot
plt.show()
