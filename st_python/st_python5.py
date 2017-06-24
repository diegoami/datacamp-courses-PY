import numpy as np
import pandas as pd

from datacamp.lib import *

from data.petals import *
# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
plt.plot(x_vers, y_vers,marker = '.', linestyle = 'none')

# Make the margins nice
plt.margins(0.02)

# Label the axes
plt.xlabel('plength dist')
plt.ylabel('ecdf')

# Display the plot
plt.show()
