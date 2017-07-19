# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv('../data/job_applications_2.csv',low_memory=False)
df['Initial Cost'] = df['Initial Cost'].apply(lambda x: pd.to_numeric(x[1:],errors='coerce'))
print(df.info())
import matplotlib.pyplot as plt

# Create the boxplot
df.boxplot(column='Initial Cost', by='Borough', rot=90)

# Display the plot
plt.show()
