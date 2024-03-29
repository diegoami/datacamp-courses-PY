import pandas as pd
election = pd.read_csv('../data/elections.csv',index_col = 'county')
# Slice the row labels 'Perry' to 'Potter': p_counties
p_counties = election['Perry':'Potter']

# Print the p_counties DataFrame
print(p_counties)

# Slice the row labels 'Potter' to 'Perry' in reverse order: p_counties_rev
p_counties_rev = election['Potter':'Perry':-1]

# Print the p_counties_rev DataFrame
print(p_counties_rev)

