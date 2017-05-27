import pandas as pd
df_clean = pd.read_csv('p8_c.csv',parse_dates=True,index_col=0 )
#df_clean = pd.read_csv('p8_c.csv')
#df_climate = pd.read_csv('../data/temp3.csv',parse_dates=True,index_col='Date' )
df_climate = pd.read_csv('p8_d.csv',parse_dates=True,index_col='Date')
df_climate['Temperature'] = pd.to_numeric(df_climate['Temperature'], errors='coerce')
df_climate['Pressure'] = pd.to_numeric(df_climate['Pressure'], errors='coerce')
df_clean['dry_bulb_faren'] = pd.to_numeric(df_clean['dry_bulb_faren'], errors='coerce')
df_clean['visibility'] = pd.to_numeric(df_clean['visibility'], errors='coerce')
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Select the visibility and dry_bulb_faren columns and resample them: weekly_mean
weekly_mean = df_clean[['visibility','dry_bulb_faren']].resample('W').mean()

# Print the output of weekly_mean.corr()
print(weekly_mean.corr())

# Plot weekly_mean with subplots=True
weekly_mean.plot(subplots=True)
plt.show()
