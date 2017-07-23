# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
auto = pd.read_csv('../data/auto.csv')
# Plot linear regressions between 'weight' and 'hp' grouped row-wise by 'origin'
sns.lmplot(x='weight', y='hp', data=auto, row='origin')

# Display the plot
plt.show()

