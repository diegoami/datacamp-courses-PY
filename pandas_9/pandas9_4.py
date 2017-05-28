import pandas as pd
users = pd.read_csv('../data/users.csv',index_col = 0)
# Pivot users with signups indexed by weekday and city: signups_pivot
#signups_pivot = users.pivot(index='weekday', columns='city', values = 'signups')
users = users.set_index(['city', 'weekday'])

# Unstack users by 'city': bycity
bycity = users.unstack('city')

# Print the bycity DataFrame
print(bycity)

# Stack bycity by 'city' and print it
print(bycity.stack(level='city'))