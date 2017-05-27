import pandas as pd
#In [1]: ts0.to_csv(sys.stdout)
df = pd.read_csv('../data/temp2.csv',parse_dates=True,index_col="Dates" )
# Downsample to 6 hour data and aggregate by mean: df1
df1 = df['Temperature'].resample('6h').mean()

# Downsample to daily data and count the number of data points: df2
df2 = df['Temperature'].resample('D').count()

print(df1)
print(df2)
