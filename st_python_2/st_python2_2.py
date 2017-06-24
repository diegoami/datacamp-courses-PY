import numpy as np
import pandas as pd
# Seed random number generator

# Import plotting modules
import matplotlib.pyplot as plt
np.random.seed(42)
from datacamp.lib import *

from data.nohitter_times import *# Compute mean no-hitter time: tau
tau = np.mean(nohitter_times)

# Draw out of an exponential distribution with parameter tau: inter_nohitter_time
inter_nohitter_time = np.random.exponential(tau, 100000)

# Create an ECDF from real data: x, y
x, y = ecdf(nohitter_times)

# Create a CDF from theoretical samples: x_theor, y_theor
x_theor, y_theor = ecdf(inter_nohitter_time)

# Overlay the plots
plt.plot(x,y, marker = '.', linestyle = 'none')
plt.plot(x_theor, y_theor, marker = '.', linestyle = 'none')

# Margins and axis labels
plt.margins(0.02)
plt.xlabel('Games between no-hitters')
plt.ylabel('CDF')

# Show the plot
plt.show()
