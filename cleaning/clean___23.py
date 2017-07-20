
import pandas as pd


ebola = pd.read_csv('../data/ebola.csv',index_col=0)

print(ebola.notnull())
print(ebola.notnull().all())
print(ebola.notnull().all().all())

# Assert that there are no missing values
assert ebola.notnull().all().all()
# Assert that there are no missing values
assert pd.notnull(ebola).all().all()


# Assert that all values are >= 0
assert (ebola >= 0).all().all()
