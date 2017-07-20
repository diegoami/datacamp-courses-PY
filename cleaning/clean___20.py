import pandas as pd
import numpy as np
import re
tips = pd.read_csv('tips_2.csv',index_col = 0)



def recode_sex(sex_value):
    # Return 1 if sex_value is 'Male'
    if sex_value == 'Male':
        return 1

    # Return 0 if sex_value is 'Female'
    elif sex_value == 'Female':
        return 0

    # Return np.nan
    else:
        return np.nan


# Apply the function to the sex column
tips['sex_recode'] = tips['sex'].apply(recode_sex)

# Write the lambda function using replace
tips['total_dollar_replace'] = tips['total_dollar'].apply(lambda x: x.replace('$', ''))

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips['total_dollar'].apply(lambda x: re.findall('\d+\.\d+', x)[0])

# Print the head of tips
print(tips.head())


# Print the first five rows of tips
print(tips.head())
