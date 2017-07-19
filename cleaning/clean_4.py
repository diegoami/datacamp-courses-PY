# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt
# Read the file into a DataFrame: df
df = pd.read_csv('../data/job_applications_2.csv',low_memory=False)
df['Initial Cost'] = df['Initial Cost'].apply(lambda x: pd.to_numeric(x[1:],errors='coerce'))
# Create and display the first scatter plot
df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()


df_subset = pd.read_csv('../data/job_applications_2_subset.csv',low_memory=False)
df_subset['Initial Cost'] = df_subset['Initial Cost'].apply(lambda x: pd.to_numeric(x[1:],errors='coerce'))
# Create and display the first scatter plot
df_subset.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()
# Create and display the second scatter plot
#df_subset.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
#plt.show()