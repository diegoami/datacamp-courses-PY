import numpy as np

from data.petals import *

# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns


# Set default Seaborn style
sns.set()



# Plot histogram of versicolor petal lengths
_ = plt.hist(versicolor_petal_length)

# Label axes

_ = plt.ylabel('count')
_ = plt.xlabel('petal length (cm)')


# Show histogram
plt.show()