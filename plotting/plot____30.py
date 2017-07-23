# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
auto = pd.read_csv('../data/auto.csv')
# Print the first 5 rows of the DataFrame
print(auto.head())

# Plot the pairwise joint distributions grouped by 'origin' along with regression lines
sns.pairplot(auto, kind='reg', hue='origin')


# Display the plot
plt.show()
