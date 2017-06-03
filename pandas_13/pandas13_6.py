import pandas as pd
revenue = pd.read_csv('../data/revenue_4.csv')
managers = pd.read_csv('../data/managers_4.csv')
sales = pd.read_csv('../data/sales_4.csv')
# Merge revenue and sales: revenue_and_sales
revenue_and_sales = pd.merge(revenue, sales, how='right', on=['city', 'state'])

# Print revenue_and_sales
print(revenue_and_sales)

# Merge sales and managers: sales_and_managers
sales_and_managers = pd.merge( sales, managers, how='left', left_on=['city', 'state'],right_on=['branch', 'state'])

# Print sales_and_managers
print(sales_and_managers)