import numpy as np
import pandas as pd

from datacamp.lib import *


# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns


from datacamp.lib import *

# Seed random number generator
np.random.seed(42)

# Initialize the number of defaults: n_defaults
n_defaults = np.empty(1000)

# Compute the number of defaults
for i in range(1000):
    n_defaults[i] =perform_bernoulli_trials(100 ,0.05)


# Take 10,000 samples out of the binomial distribution: n_defaults
n_defaults = np.random.binomial(n=100, p=0.05,size=10000)

# Compute bin edges: bins
bins = np.arange(0, max(n_defaults)  + 1.5) - 0.5

# Generate histogram
plt.hist(n_defaults, normed=True, bins=bins)

# Set margins
plt.margins(0.02)

# Label axes
plt.xlabel('x')
plt.ylabel('y')



# Show the plot
plt.show()

