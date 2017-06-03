#Import pandas
import pandas as pd



# Load DataFrame from file_path: editions
editions = pd.read_csv('../data/editions.csv')

# Extract the relevant columns: editions
editions = editions[['Edition', 'Grand Total', 'City', 'Country']]

# Print editions DataFrame
print(editions)