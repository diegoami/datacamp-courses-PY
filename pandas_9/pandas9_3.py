import pandas as pd
users = pd.read_csv('../data/users.csv',index_col = 0)
# Pivot users with signups indexed by weekday and city: signups_pivot
#signups_pivot = users.pivot(index='weekday', columns='city', values = 'signups')
users = users.set_index(['city', 'weekday'])

# Unstack users by 'weekday': byweekday
byweekday = users.unstack('weekday')

# Print the byweekday DataFrame
print(byweekday)

# Stack byweekday by 'weekday' and print it
print(byweekday.stack(level='weekday'))