# Import pandas
import pandas as pd


# Read 'gapminder.csv' into a DataFrame: df
df = pd.read_csv('../data/gapminder_4.csv')

# Create dummy variables: df_region
df_region = pd.get_dummies(df)

# Print the columns of df_region
print(df_region.columns)

# Create dummy variables with drop_first=True: df_region
df_region = pd.get_dummies(df,drop_first=True)

# Print the new columns of df_region
print(df_region.columns)

X = df_region.drop("fertility", axis=1).values
y = df_region["fertility"]
df_columns = df_region.drop("fertility", axis=1).columns
# Import necessary modules
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score


# Instantiate a ridge regressor: ridge
ridge = Ridge(alpha=0.5, normalize=True)

# Perform 5-fold cross-validation: ridge_cv
ridge_cv = cross_val_score(ridge, X,y,cv=5)

# Print the cross-validated scores
print(ridge_cv)
