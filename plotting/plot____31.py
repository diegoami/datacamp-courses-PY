# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
cov_matrix = pd.read_csv('cov_matrix.csv',index_col=0)
# Print the covariance matrix
print(cov_matrix)

# Visualize the covariance matrix using a heatmap
sns.heatmap(cov_matrix)
# Display the heatmap
plt.show()
