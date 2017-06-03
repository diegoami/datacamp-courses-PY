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
hosts = hosts[['Edition','NOC']].set_index( 'Edition')


# Reshape fractions_change: reshaped
reshaped = pd.melt(fractions_change,id_vars='Edition', value_name='Change')

# Print reshaped.shape and fractions_change.shape
print(reshaped.shape, fractions_change.shape)

# Extract rows from reshaped where 'NOC' == 'CHN': chn
chn = reshaped.loc[reshaped['NOC'] == 'CHN']
print(reshaped.loc[reshaped['NOC'] == 'ITA'])
print(reshaped.loc[reshaped['NOC'] == 'USA'])
print(reshaped.loc[reshaped['NOC'] == 'GER'])
print(reshaped.loc[reshaped['NOC'] == 'FRA'])

# Print last 5 rows of chn with .tail()
print(chn.tail())