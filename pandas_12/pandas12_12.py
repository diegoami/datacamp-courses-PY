
import pandas as pd

weather_max = pd.read_csv('../data/monthly_max_temp.csv',index_col='Month')
weather_mean = pd.read_csv('../data/monthly_mean_temp.csv',index_col='Month')
# Concatenate weather_max and weather_mean horizontally: weather
weather = pd.concat([weather_max,weather_mean],axis=1)

# Print weather
print(weather)
