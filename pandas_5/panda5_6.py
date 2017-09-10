import pandas as pd
#In [1]: ts0.to_csv(sys.stdout)

ts1 = pd.read_csv('ts1.csv',parse_dates=True,index_col="Dates" )
ts2 = pd.read_csv('ts2.csv',parse_dates=True,index_col="Dates" )

# Reindex without fill method: ts3
ts3 = ts2.reindex(ts1.index)

# Reindex with fill method, using forward fill: ts4
ts4 = ts2.reindex(ts1.index, method='ffill')

print(ts3)

print(ts4)
# Combine ts1 + ts2: sum12
sum12 = ts1 + ts2

# Combine ts1 + ts3: sum13
sum13 = ts1 + ts3

# Combine ts1 + ts4: sum14
sum14 = ts1 + ts4

print(sum12)
print(sum13)
print(sum14)

