# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv('../data/job_applications.csv')


# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()
