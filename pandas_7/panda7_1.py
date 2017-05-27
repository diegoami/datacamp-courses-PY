import pandas as pd
election = pd.read_csv('../data/elections.csv',index_col = 'county')
print(election.loc['Bedford','winner'])
