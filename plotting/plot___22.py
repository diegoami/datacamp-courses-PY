# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
auto = pd.read_csv('../data/auto.csv')

# Plot a linear regression between 'weight' and 'hp', with a hue of 'origin' and palette of 'Set1'
sns.lmplot(x='weight', y='hp', data=auto, hue='origin', palette='Set1')
# Display the plot
plt.show()

