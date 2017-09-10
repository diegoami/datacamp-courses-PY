import pandas as pd
gapminder = pd.read_csv('../data/gapminder_2.csv',index_col=0)

# Melt users: skinny
mgmd = pd.melt(gapminder,id_vars=['Country','Year'], value_vars=['fertility','life','population','child_mortality','gdp'])

print(mgmd[mgmd['Country']== 'Italy'])

