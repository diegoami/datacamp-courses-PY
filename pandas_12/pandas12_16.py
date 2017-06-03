
import pandas as pd

fns = ['df_0', 'df_1', 'df_2']
dataframes = []
for fn in fns:
    # Create the file name: file_name
    file_name = "%s.csv" % fn
    dataframe =  pd.read_csv(file_name,parse_dates=True,index_col=0)
    dataframes.append(dataframe)
#print(dataframes)
february = pd.concat(dataframes, axis=1,keys=['Hardware', 'Software', 'Service'])

# Print february.info()
print(february.info())

# Assign pd.IndexSlice: idx
idx = pd.IndexSlice

# Create the slice: slice_2_8
slice_2_8 = february.loc['2015-02-01':'2015-02-08', idx[:, 'Company']]

# Print slice_2_8
print(slice_2_8)
