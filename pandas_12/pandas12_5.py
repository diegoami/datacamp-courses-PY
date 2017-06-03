# Import pandas
import pandas as pd
names_1981 =  pd.read_csv('../data/names_1981.csv',index_col=(0,1))
names_1881 =  pd.read_csv('../data/names_1881.csv',index_col=(0,1))

# Reindex names_1981 with index of names_1881: common_names
common_names = names_1981.reindex(names_1881.index)

# Print shape of common_names
print(common_names.shape)

# Drop rows with null counts: common_names
common_names = common_names.dropna()

# Print shape of new common_names
print(common_names.shape)

