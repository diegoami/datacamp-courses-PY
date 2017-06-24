
# Import plotting modules
import matplotlib.pyplot as plt



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

# Compute CDF: x, y
x,y = ecdf(n_defaults)

# Plot the CDF with axis labels
plt.plot(x,y, marker = '.', linestyle = 'none')
plt.xlabel('x')
plt.ylabel('y')




# Show the plot
plt.show()
