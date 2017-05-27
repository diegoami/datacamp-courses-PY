import pandas as pd
df_clean = pd.read_csv('p8_c.csv',parse_dates=True,index_col=0 )
#df_clean = pd.read_csv('p8_c.csv')
#df_climate = pd.read_csv('../data/temp3.csv',parse_dates=True,index_col='Date' )
df_climate = pd.read_csv('p8_d.csv',parse_dates=True,index_col='Date')
df_climate['Temperature'] = pd.to_numeric(df_climate['Temperature'], errors='coerce')
df_climate['Pressure'] = pd.to_numeric(df_climate['Pressure'], errors='coerce')
df_clean['dry_bulb_faren'] = pd.to_numeric(df_clean['dry_bulb_faren'], errors='coerce')

# Downsample df_clean by day and aggregate by mean: daily_mean_2011
daily_mean_2011 = df_clean.resample('D').mean()
print(daily_mean_2011)
# Extract the dry_bulb_faren column from daily_mean_2011 using .values: daily_temp_2011
#daily_temp_2011 = daily_mean_2011['dry_bulb_faren'].values
daily_temp_2011 = daily_mean_2011['dry_bulb_faren']
# Downsample df_climate by day and aggregate by mean: daily_climate
daily_climate = df_climate.resample('D').mean()

print(daily_climate)
# Extract the Temperature column from daily_climate using .reset_index(): daily_temp_climate
daily_temp_climate = daily_climate.reset_index()['Temperature']

print(daily_temp_climate)
print(type(daily_temp_2011),type(daily_temp_climate))
# Compute the difference between the two arrays and print the mean difference
#difference = daily_climate - daily_temp_climate
difference = daily_temp_2011 - daily_temp_climate

#print(daily_temp_2011)
#print(daily_temp_climate)



print(difference.mean())
