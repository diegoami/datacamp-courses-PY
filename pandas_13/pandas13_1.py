import pandas as pd
revenue = pd.read_csv('../data/revenue.csv')
managers = pd.read_csv('../data/managers.csv')

# Merge revenue with managers on 'city': merge_by_city
merge_by_city = pd.merge(revenue, managers, on = 'city')

# Print merge_by_city
print(merge_by_city)

# Merge revenue with managers on 'branch_id': merge_by_id
merge_by_id = pd.merge(revenue, managers, on = 'branch_id')

# Print merge_by_id
print(merge_by_id)