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



# Compute ECDF: x, y
x,y = ecdf(n_defaults)

# Plot the ECDF with labeled axes
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x,y,  marker = '.', linestyle = 'none')


# Show the plot

plt.show()
# Compute the number of 100-loan simulations with 10 or more defaults: n_lose_money
n_lose_money = np.sum(n_defaults >= 10)

# Compute and print probability of losing money
print('Probability of losing money =', n_lose_money / len(n_defaults))