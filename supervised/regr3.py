# Import numpy and pandas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Read the CSV file into a DataFrame: df
df = pd.read_csv('../data/gapminder_2.csv')
y_s = df['life'].values
X_fertility_s = df['fertility'].values
#nvalues = np.array(np.isfinite(X_fertility_s ))
nvalues = np.logical_not(np.isnan(X_fertility_s ))
print(nvalues)
X_fertility = X_fertility_s[nvalues]
print(len(X_fertility))
y = y_s[nvalues]
print(len(y))
# Import LinearRegression
from sklearn.linear_model import LinearRegression

# Create the regressor: reg
reg = LinearRegression()

# Create the prediction space
prediction_space = np.linspace(min(X_fertility), max(X_fertility)).reshape(-1,1)

lx = len(X_fertility )

X_fertility = X_fertility.reshape(lx,1)
y = y.reshape(lx,1)

# Fit the model to the data
reg.fit(X_fertility, y)

# Compute predictions over the prediction space: y_pred
y_pred = reg.predict(prediction_space)

# Print R^2
print(reg.score(X_fertility, y))

# Plot regression line
plt.scatter(X_fertility, y)
plt.plot(prediction_space, y_pred, color='black', linewidth=3)
plt.show()
