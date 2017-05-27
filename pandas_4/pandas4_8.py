from data.weather_udg import january_df as january
from data.weather_udg import march_df as march


import matplotlib.pyplot as plt


# Print the number of countries reported in 2015
# Print the mean of the January and March data
print(january.mean(), march.mean())

# Print the standard deviation of the January and March data
print(january.std(), march.std())
