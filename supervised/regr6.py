
#pd.DataFrame(np.column_stack([X,y])).to_csv(sys.stdout)
# Import necessary modules
from sklearn.linear_model import Lasso
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np
# Read the CSV file into a DataFrame: df
df = pd.read_csv('../data/gapminder_3.csv')
X = df.drop('fertility', axis=1).values
y = df['fertility']
df_columns = df.drop('fertility', axis=1).columns
# Import Lasso
from sklearn.linear_model import Lasso


# Instantiate a lasso regressor: lasso
lasso = Lasso(alpha=0.4,normalize=True)

# Fit the regressor to the data
lasso.fit(X,y)

# Compute and print the coefficients
lasso_coef = lasso.coef_
print(lasso_coef)

# Plot the coefficients
plt.plot(range(len(df_columns)), lasso_coef)
plt.xticks(range(len(df_columns)), df_columns.values, rotation=60)
plt.margins(0.02)
plt.show()
