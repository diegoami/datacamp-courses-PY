import numpy as np
import pandas as pd
aapl = pd.read_csv('../data/st_aapl.csv',parse_dates=True,index_col=0 )
ibm = pd.read_csv('../data/st_ibm.csv',parse_dates=True ,index_col=0)

csco = pd.read_csv('../data/st_csco.csv',parse_dates=True ,index_col=0)
msft = pd.read_csv('../data/st_msft.csv',parse_dates=True ,index_col=0)

mean_30 = pd.read_csv('../data/mean_30.csv',parse_dates=True,index_col=0 )
mean_75 = pd.read_csv('../data/mean_75.csv',parse_dates=True ,index_col=0)

mean_125 = pd.read_csv('../data/mean_125.csv',parse_dates=True ,index_col=0)
mean_250 = pd.read_csv('../data/mean_250.csv',parse_dates=True ,index_col=0)
