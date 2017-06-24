import numpy as np
import pandas as pd

from datacamp.lib import *



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