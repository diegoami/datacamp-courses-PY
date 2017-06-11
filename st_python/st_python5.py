import numpy as np
import pandas as pd

def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""

    # Number of data points: n

    n = len(data)
    # x-data for the ECDF: x

    x = np.sort(data)
    # y-data for the ECDF: y
    y = np.arange(1,n+1) / n

    return x, y


versicolor_petal_length = np.array([ 4.7,  4.5,  4.9,  4. ,  4.6,  4.5,  4.7,  3.3,  4.6,  3.9,  3.5,
        4.2,  4. ,  4.7,  3.6,  4.4,  4.5,  4.1,  4.5,  3.9,  4.8,  4. ,
        4.9,  4.7,  4.3,  4.4,  4.8,  5. ,  4.5,  3.5,  3.8,  3.7,  3.9,
        5.1,  4.5,  4.5,  4.7,  4.4,  4.1,  4. ,  4.4,  4.6,  4. ,  3.3,
        4.2,  4.2,  4.2,  4.3,  3. ,  4.1])

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
