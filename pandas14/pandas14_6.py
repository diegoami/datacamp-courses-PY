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

# Print first & last 5 rows of fractions
print(fractions.head())
print(fractions.tail())