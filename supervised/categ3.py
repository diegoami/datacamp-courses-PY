# Import pandas
import pandas as pd


df = pd.read_csv('../data/gapminder_5.csv')
X = df.drop("13", axis=1).values
y = df["13"]
df_columns = df.drop("13", axis=1).columns
# Import necessary modules
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score


# Instantiate a ridge regressor: ridge
ridge = Ridge(alpha=0.5, normalize=True)

# Perform 5-fold cross-validation: ridge_cv
ridge_cv = cross_val_score(ridge, X,y,cv=5)

# Print the cross-validated scores
print(ridge_cv)
