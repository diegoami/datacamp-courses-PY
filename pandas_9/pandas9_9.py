import pandas as pd
# Set the new index: users_idx
users = pd.read_csv('week2.csv',index_col=0)
users_idx = users.set_index(['city', 'weekday'])

# Print the users_idx DataFrame
print(users_idx)

# Obtain the key-value pairs: kv_pairs
kv_pairs = pd.melt(users_idx,col_level=0)

# Print the key-value pairs
print(kv_pairs)
print(kv_pairs.index)