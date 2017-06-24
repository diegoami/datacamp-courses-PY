import numpy as np
import pandas as pd

from datacamp.lib import *
from data.petals import *

from data.petals import *

# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns


# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)
x_set, y_set = ecdf(setosa_petal_length)
x_virg, y_virg = ecdf(virginica_petal_length)



# Plot all ECDFs on the same plot
_ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')

_ = plt.plot(x_set, y_set, marker='.', linestyle='none')
_ = plt.plot(x_virg, y_virg, marker='.', linestyle='none')

# Make nice margins
plt.margins(0.02)

# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()