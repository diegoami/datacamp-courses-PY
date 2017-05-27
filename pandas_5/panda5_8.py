import pandas as pd
#In [1]: ts0.to_csv(sys.stdout)
df = pd.read_csv('../data/temp2.csv',parse_dates=True,index_col="Dates" )
# Extract temperature data for August: august
august = df['Temperature'].loc['2010-August']

# Downsample to obtain only the daily highest temperatures in August: august_highs
august_highs = august.resample('D').max()

# Extract temperature data for February: february
february = df['Temperature'].loc['2010-February']

# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('D').min()

print(august_highs)
print(february_lows)