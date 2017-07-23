# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# Print the covariance matrix
from plotting.plot___co3 import *
# Slice aapl from Nov. 2007 to Apr. 2008 inclusive: view
view = aapl['2007-11':'2008-04']

# Plot the entire series
plt.subplot(2,1,1)
plt.xticks(rotation=45)
plt.title('AAPL: 2001-2011')
plt.plot(aapl)
# Specify the axes
#plt.axes((0.25,0.5,0.35,0.35))

# Plot the sliced series in red using the current axes
plt.subplot(2,1,2)
plt.xticks(rotation=45)
plt.title('2007/11-2008/04')
plt.plot(view,color='red')
plt.show()

