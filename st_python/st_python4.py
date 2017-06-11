import numpy as np
import pandas as pd

# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/petal_length.csv')

# Create bee swarm plot with Seaborn's default settings
_ = sns.swarmplot(x='species',y='petal length (cm)',data=df)

# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')


# Show the plot
_ = plt.show()
