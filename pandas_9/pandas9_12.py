import pandas as pd
# Set the new index: users_idx
users = pd.read_csv('week2.csv',index_col=0)

# Create the DataFrame with the appropriate pivot table: signups_and_visitors
signups_and_visitors = users.pivot_table(index='weekday',aggfunc=sum)

# Print signups_and_visitors
print(signups_and_visitors)

# Add in the margins: signups_and_visitors_total
signups_and_visitors_total = users.pivot_table(index='weekday',aggfunc=sum, margins=True)

# Print signups_and_visitors_total
print(signups_and_visitors_total)

