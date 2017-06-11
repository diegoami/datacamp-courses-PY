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



# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/petal_length.csv')
# Compute ECDF for versicolor data: x_vers, y_vers
# Create box plot with Seaborn's default settings
_ = sns.boxplot(x='species', y='petal length (cm)', data=df)

# Label the axes
_ = plt.xlabel('species')

_ = plt.ylabel('petal length (cm)')


# Show the plot
_ = plt.show()