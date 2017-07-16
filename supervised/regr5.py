# Import necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

import pandas as pd
import numpy as np
# Read the CSV file into a DataFrame: df
df = pd.read_csv('../data/gapminder_2.csv')
y_s = df['life'].values
X_fertility_s = df['fertility'].values
#nvalues = np.array(np.isfinite(X_fertility_s ))
nvalues = np.logical_not(np.isnan(X_fertility_s ))
print(nvalues)
X = X_fertility_s[nvalues]
print(len(X))
y = y_s[nvalues]
print(len(y))

# Create the regressor: reg
lx = len(X)

X= X.reshape(lx,1)
y = y.reshape(lx,1)

from sklearn.model_selection import cross_val_score

# Create a linear regression object: reg
reg = LinearRegression()

# Compute 5-fold cross-validation scores: cv_scores
cv_scores = cross_val_score(reg, X,y,cv=5)

# Print the 5-fold cross-validation scores
print(cv_scores)

print("Average 5-Fold CV Score: {}".format(np.mean(cv_scores)))

# Import necessary modules
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression



# Perform 3-fold CV
cvscores_3 = cross_val_score(reg, X,y,cv=3)
print(np.mean(cvscores_3))

# Perform 10-fold CV
cvscores_10 =  cross_val_score(reg, X,y,cv=3)
print(np.mean(cvscores_10))
