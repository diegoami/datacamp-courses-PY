import pandas as pd
titanic = pd.read_csv('../data/titanic.csv',index_col = 0)

# Group titanic by 'pclass'
by_class = titanic.groupby('pclass')

# Select 'age' and 'fare'
by_class_sub = by_class[['age','fare']]
print(type(by_class_sub))

# Aggregate by_class_sub by 'max' and 'median': aggregated
aggregated = by_class_sub.agg(['max','median'])

# Print the maximum age in each class
print(aggregated.loc[:, ('age','max')])

# Print the median fare in each class
print(aggregated.loc[:, ('fare','median')])

print(aggregated)

print(titanic.groupby('pclass')[['age','fare']].agg(['max','median']))

print(titanic.groupby('pclass')[['age','fare']].agg(['max','median']).loc[:, ('age','max')])

print(titanic.groupby('pclass')['age','fare'].agg(['max','median']))