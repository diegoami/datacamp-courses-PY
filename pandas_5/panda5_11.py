import pandas as pd
#In [1]: ts0.to_csv(sys.stdout)
df = pd.read_csv('../data/airports.csv',parse_dates=True,index_col="Date (MM/DD/YYYY)" )
# Strip extra whitespace from the column names: df.columns
df.columns = df.columns.str.strip()

# Extract data for which the destination airport is Dallas: dallas
dallas = df['Destination Airport'].str.contains('DAL')

# Compute the total number of Dallas departures each day: daily_departures
daily_departures = dallas.resample('D').sum()

# Generate the summary statistics for daily Dallas departures: stats
stats = daily_departures.describe()

print(stats)
print(daily_departures)