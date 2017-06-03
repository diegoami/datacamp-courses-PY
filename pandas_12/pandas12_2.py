# Import pandas
import pandas as pd

gold = pd.read_csv('../data/gold2.csv',index_col=0)
silver = pd.read_csv('../data/silver2.csv',index_col=0)
bronze = pd.read_csv('../data/bronze2.csv',index_col=0)

# Make a copy of gold: medals
medals = gold.copy()

# Create list of new column labels: new_labels
new_labels = ['NOC', 'Country', 'Gold']

# Rename the columns of medals using new_labels
medals.columns = new_labels

# Add columns 'Silver' & 'Bronze' to medals
medals['Silver'] = silver['Total']
medals['Bronze'] = bronze['Total']

# Print the head of medals
print(medals.head())