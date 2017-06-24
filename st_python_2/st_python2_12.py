import numpy as np
import pandas as pd
# Seed random number generator

# Import plotting modules
import matplotlib.pyplot as plt
np.random.seed(42)

from datacamp.lib import *

from data.rainfall import *

# Generate 10,000 bootstrap replicates of the variance: bs_replicates
bs_replicates =  draw_bs_reps(rainfall,np.var,10000)

# Put the variance in units of square centimeters
bs_replicates = bs_replicates / 100

# Make a histogram of the results
_ = plt.hist(bs_replicates, bins=50, normed=True)
_ = plt.xlabel('variance of annual rainfall (sq. cm)')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()
