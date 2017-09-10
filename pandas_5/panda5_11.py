import pandas as pd
#In [1]: ts0.to_csv(sys.stdout)
df = pd.read_csv('../data/airports.csv',parse_dates=True,index_col="Date (MM/DD/YYYY)" )
# Strip extra whitespace from the column names: df.columns
df.columns = df.columns.str.strip()

# Extract data for which the destination airport is Dallas: dallas
dallas = df['Destination Airport'].str.contains('DAL')
dallas_or_mdw = df['Destination Airport'].str.contains('MDW') | df['Destination Airport'].str.contains('DAL')

print(type(dallas))
print(dallas)
print(dallas_or_mdw)

print(dallas.resample('D').sum())
print(dallas.resample('D').count())

print(dallas_or_mdw.resample('D').sum())
print(dallas_or_mdw.resample('D').count())



# Compute the total number of Dallas departures each day: daily_departures
daily_departures = dallas.resample('D').sum()



# Generate the summary statistics for daily Dallas departures: stats
stats = daily_departures.describe()

#print(stats)
#print(daily_departures)