
import pandas as pd

china = pd.read_csv('../data/china_gdp.csv',index_col=0,parse_dates=True)
us    = pd.read_csv('../data/usa_gdp.csv',index_col=0,parse_dates=True)


# Resample and tidy china: china_annual
china_annual = china.resample('A').pct_change(10).dropna()

# Resample and tidy us: us_annual
us_annual = us.resample('A').pct_change(10).dropna()

# Concatenate china_annual and us_annual: gdp
gdp = pd.concat([china_annual,us_annual], join='inner', axis=1)

# Resample gdp and print
print(gdp.resample('10A').last())