import pandas as pd
sales = pd.read_csv('../data/sales.csv',index_col=0)

# Reset the index: visitors_by_city_weekday
sales = sales.reset_index()

# Melt visitors_by_city_weekday: visitors
print(pd.melt(sales , id_vars=['month'], value_name='sold'))
