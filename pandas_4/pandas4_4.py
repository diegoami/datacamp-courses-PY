from data.fraction import fraction_df as df

import matplotlib.pyplot as plt
# This formats the plots such that they appear on separate rows
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
print(ax1, ax2)

# Plot the CDF
df.fraction.plot(ax=ax1, kind='hist', bins=30, normed=True, cumulative=True, range=(0,.3))

# Plot the PDF
df.fraction.plot(ax=ax2, kind='hist', bins=30, normed=True, range=(0,.3))
plt.show()


print(df)