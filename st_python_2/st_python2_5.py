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

# Set the margins and label axes
plt.margins(0.02)
_ = plt.xlabel('percent illiterate')
_ = plt.ylabel('fertility')

# Show the plot
plt.show()

# Show the Pearson correlation coefficient
print(pearson_r(illiteracy, fertility))