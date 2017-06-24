import numpy as np
import pandas as pd
# Seed random number generator

# Import plotting modules
import matplotlib.pyplot as plt
np.random.seed(42)
from datacamp.lib import *


from datacamp.lib import *

from data.ill_fert import *

# Plot the illiteracy rate versus fertility
_ = plt.plot(illiteracy, fertility, marker = '.', linestyle = 'none')

# Perform a linear regression using np.polyfit(): a, b
a, b = np.polyfit(illiteracy, fertility,1)

# Print the results to the screen
print('slope =', a, 'children per woman / percent illiterate')
print('intercept =', b, 'children per woman')

# Make theoretical line to plot
x = np.array([0,100])
y = a * x + b

# Add regression line to your plot
_ = plt.plot(x,y)

# Draw the plot
plt.show()
