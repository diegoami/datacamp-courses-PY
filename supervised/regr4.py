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


# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y , test_size = 0.2, random_state=42)

# Create the regressor: reg_all
reg_all = LinearRegression()

# Fit the regressor to the training data
reg_all.fit(X_train, y_train,)

# Predict on the test data: y_pred
y_pred = reg_all.predict(X_test)

# Compute and print R^2 and RMSE
print("R^2: {}".format(reg_all.score(X_test, y_test)))
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error: {}".format(rmse))
