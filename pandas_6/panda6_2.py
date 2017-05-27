import pandas as pd
from matplotlib import pyplot as plt
#In [1]: ts0.to_csv(sys.stdout)
df = pd.read_csv('../data/temp3.csv',parse_dates=True,index_col='Date' )
# Plot the summer data
df.Temperature['2010-Jun':'2010-Aug'].plot()
plt.show()
plt.clf()

# Plot the one week data
df.Temperature['2010-06-10':'2010-06-17'].plot()
plt.show()
plt.clf()

