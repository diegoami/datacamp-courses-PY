import numpy as np
import pandas as pd
aapl = pd.read_csv('../data/st_aapl.csv',parse_dates=True,index_col=0 )
ibm = pd.read_csv('../data/st_ibm.csv',parse_dates=True ,index_col=0)

csco = pd.read_csv('../data/st_csco.csv',parse_dates=True ,index_col=0)
msft = pd.read_csv('../data/st_msft.csv',parse_dates=True ,index_col=0)
