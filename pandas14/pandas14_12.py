# Import pyplot
import matplotlib.pyplot as plt

import pandas as pd
# Load DataFrame from file_path: editions
medals = pd.read_csv('../data/medals_2.csv')

# Construct the pivot_table: medal_counts
medal_counts = medals.pivot_table(index='Edition',values='Athlete',columns='NOC',aggfunc='count')

# Load DataFrame from file_path: editions
editions = pd.read_csv('../data/editions.csv')

# Set Index of editions: totals
totals = editions.set_index('Edition')

# Reassign totals['Grand Total']: totals
totals = totals['Grand Total']

# Divide medal_counts by totals: fractions
fractions = medal_counts.divide( totals, axis = 'rows' )

# Apply the expanding mean: mean_fractions
mean_fractions = fractions.expanding().mean()

# Compute the percentage change: fractions_change
fractions_change = mean_fractions.pct_change().multiply(100)

# Reset the index of fractions_change: fractions_change
fractions_change = fractions_change.reset_index()

ioc_codes = pd.read_csv('../data/country_codes.csv')

# Extract the relevant columns: ioc_codes
ioc_codes = ioc_codes[['Country', 'NOC']]

# Left join editions and ioc_codes: hosts
hosts = pd.merge(editions,ioc_codes, how='left')

# Extract relevant columns and set index: hosts
#hosts = hosts[['Edition','NOC']].set_index( 'Edition')

print(hosts)
# Reshape fractions_change: reshaped
reshaped = pd.melt(fractions_change,id_vars='Edition', value_name='Change')
print(reshaped)
print(hosts)
# Merge reshaped and hosts: merged
merged = pd.merge(reshaped,hosts,how='inner')


# Print first 5 rows of merged
print(merged)

# Set Index of merged and sort it: influence
influence = merged.set_index('Edition').sort_index()

# Print first 5 rows of influence
#print(influence.head())
# Extract influence['Change']: change
change =  influence['Change']

# Make bar plot of change: ax
ax = change.plot(kind='bar')

# Customize the plot to improve readability
ax.set_ylabel("% Change of Host Country Medal Count")
ax.set_title("Is there a Host Country Advantage?")
ax.set_xticklabels(editions['City'])

# Display the plot
plt.show()