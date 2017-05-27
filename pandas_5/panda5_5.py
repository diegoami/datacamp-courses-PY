import pandas as pd
#In [1]: ts0.to_csv(sys.stdout)
from data.date_list import temperature_list
ts0 = pd.read_csv('../data/temp2.csv',parse_dates=True,index_col="Dates" )

# Extract the hour from 9pm to 10pm on '2010-10-11': ts1
ts1 = ts0.loc['2010-10-11 21:00:00']

# Extract '2010-07-04' from ts0: ts2
ts2 = ts0.loc['July 4th, 2010']

# Extract data from '2010-12-15' to '2010-12-31': ts3
ts3 = ts0.loc['12/15/2010':'12/31/2010']
print(ts1,ts2,ts3)

