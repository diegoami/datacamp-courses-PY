import pandas as pd
df_clean = pd.read_csv('p8_c.csv',parse_dates=True,index_col=0 )
#df_clean = pd.read_csv('p8_c.csv')
#df_climate = pd.read_csv('../data/temp3.csv',parse_dates=True,index_col='Date' )
df_climate = pd.read_csv('p8_d.csv',parse_dates=True,index_col='Date')
df_climate['Temperature'] = pd.to_numeric(df_climate['Temperature'], errors='coerce')
df_climate['Pressure'] = pd.to_numeric(df_climate['Pressure'], errors='coerce')
df_clean['dry_bulb_faren'] = pd.to_numeric(df_clean['dry_bulb_faren'], errors='coerce')

# Select days that are sunny: sunny
sunny = df_clean[df_clean['sky_condition'] == 'CLR']

# Select days that are overcast: overcast
overcast = df_clean[df_clean['sky_condition'].str.contains('OVC')]

# Resample sunny and overcast, aggregating by maximum daily temperature
sunny_daily_max = sunny.resample('D').max()
overcast_daily_max = overcast.resample('D').max()

# Print the difference between the mean of sunny_daily_max and overcast_daily_max
print(sunny_daily_max.mean() - overcast_daily_max.mean())
