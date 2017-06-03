import pandas as pd

weather = pd.read_csv('../data/weather.csv')

temps_f = weather[['Min TemperatureF', 'Mean TemperatureF', 'Max TemperatureF']]

# Convert temps_f to celsius: temps_c
temps_c = (temps_f - 32) * 5 / 9

# Rename 'F' in column names with 'C': temps_c.columns
temps_c.columns = temps_f.columns.str.replace('F','C')

# Print first 5 rows of temps_c
print(temps_c.head())