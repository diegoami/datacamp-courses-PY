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
# Create a Boolean Series for sunny days: sunny
import matplotlib.pyplot as plt
sunny = df_clean['sky_condition'] == 'CLR'

# Resample the Boolean Series by day and compute the sum: sunny_hours
sunny_hours = sunny.resample('D').sum()

# Resample the Boolean Series by day and compute the count: total_hours
total_hours = sunny.resample('D').count()

# Divide sunny_hours by total_hours: sunny_fraction
sunny_fraction = sunny_hours / total_hours

# Make a box plot of sunny_fraction
sunny_fraction.plot(kind='box')
plt.show()