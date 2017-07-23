# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
auto = pd.read_csv('../data/auto.csv')
# Generate a swarm plot of 'hp' grouped horizontally by 'cyl'
plt.subplot(2,1,1)
sns.swarmplot(x='cyl', y='hp', data=auto)

# Generate a swarm plot of 'hp' grouped vertically by 'cyl' with a hue of 'origin'
plt.subplot(2,1,2)
sns.swarmplot(x='hp', y='cyl',  data=auto, orient='h', hue='origin')

# Display the plot
plt.show()
