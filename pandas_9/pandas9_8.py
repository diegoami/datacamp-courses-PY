import pandas as pd
users = pd.read_csv('week2.csv',index_col=0)

# Melt users: skinny
skinny = pd.melt(users,id_vars=['weekday','city'], value_vars=['visitors','signups'])

# Print skinny
print(skinny)
