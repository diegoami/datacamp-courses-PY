
from data.baseball import *
# Import numpy as np
import numpy as np

# For loop over np_height
for height in np_height:
    print("{0} inches".format(height) )

# For loop over np_baseball
for b in np.nditer(np_baseball):
    print(b )
