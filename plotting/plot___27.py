# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
auto = pd.read_csv('../data/auto.csv')
# Generate a joint plot of 'hp' and 'mpg'
sns.jointplot('hp','mpg',auto)

# Display the plot
plt.show()
