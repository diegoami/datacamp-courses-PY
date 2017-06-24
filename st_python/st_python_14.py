import numpy as np
import pandas as pd

from datacamp.lib import *


versicolor_petal_length = np.array([ 4.7,  4.5,  4.9,  4. ,  4.6,  4.5,  4.7,  3.3,  4.6,  3.9,  3.5,
        4.2,  4. ,  4.7,  3.6,  4.4,  4.5,  4.1,  4.5,  3.9,  4.8,  4. ,
        4.9,  4.7,  4.3,  4.4,  4.8,  5. ,  4.5,  3.5,  3.8,  3.7,  3.9,
        5.1,  4.5,  4.5,  4.7,  4.4,  4.1,  4. ,  4.4,  4.6,  4. ,  3.3,
        4.2,  4.2,  4.2,  4.3,  3. ,  4.1])


versicolor_petal_width =  np.array([ 1.4,  1.5,  1.5,  1.3,  1.5,  1.3,  1.6,  1. ,  1.3,  1.4,  1. ,
        1.5,  1. ,  1.4,  1.3,  1.4,  1.5,  1. ,  1.5,  1.1,  1.8,  1.3,
        1.5,  1.2,  1.3,  1.4,  1.4,  1.7,  1.5,  1. ,  1.1,  1. ,  1.2,
        1.6,  1.5,  1.6,  1.5,  1.3,  1.3,  1.3,  1.2,  1.4,  1.2,  1. ,
        1.3,  1.2,  1.3,  1.3,  1.1,  1.3])


setosa_petal_length = np.array([ 1.4,  1.4,  1.3,  1.5,  1.4,  1.7,  1.4,  1.5,  1.4,  1.5,  1.5,
        1.6,  1.4,  1.1,  1.2,  1.5,  1.3,  1.4,  1.7,  1.5,  1.7,  1.5,
        1. ,  1.7,  1.9,  1.6,  1.6,  1.5,  1.4,  1.6,  1.6,  1.5,  1.5,
        1.4,  1.5,  1.2,  1.3,  1.5,  1.3,  1.5,  1.3,  1.3,  1.3,  1.6,
        1.9,  1.4,  1.6,  1.4,  1.5,  1.4])

virginica_petal_length = np.array([ 6. ,  5.1,  5.9,  5.6,  5.8,  6.6,  4.5,  6.3,  5.8,  6.1,  5.1,
        5.3,  5.5,  5. ,  5.1,  5.3,  5.5,  6.7,  6.9,  5. ,  5.7,  4.9,
        6.7,  4.9,  5.7,  6. ,  4.8,  4.9,  5.6,  5.8,  6.1,  6.4,  5.6,
        5.1,  5.6,  6.1,  5.6,  5.5,  4.8,  5.4,  5.6,  5.1,  5.1,  5.9,
        5.7,  5.2,  5. ,  5.2,  5.4,  5.1])




# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns
# Make a scatter plot
# Compute the covariance matrix: covariance_matrix
from datacamp.lib import *

# Compute Pearson correlation coefficient for I. versicolor: r

r = pearson_r(versicolor_petal_length,versicolor_petal_width)
# Print the result
print(r)
