# Import pandas
import pandas as pd


# Load DataFrame from file_path: ioc_codes
ioc_codes = pd.read_csv('../data/country_codes.csv')

# Extract the relevant columns: ioc_codes
ioc_codes = ioc_codes[['Country', 'NOC']]

# Print first and last 5 rows of ioc_codes
print(ioc_codes.head())
print(ioc_codes.tail())