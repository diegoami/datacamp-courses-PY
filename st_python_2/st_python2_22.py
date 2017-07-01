import pandas as pd
from datacamp.lib import *

df = pd.read_csv('../data/horned_frogs.csv')

force_a = df[df['ID']=='A']['impact_force'].as_matrix()
force_b = df[df['ID']=='B']['impact_force'].as_matrix()

# Make an array of translated impact forces: translated_force_b
translated_force_b = force_b - np.mean(force_b)+ 0.55

# Take bootstrap replicates of Frog B's translated impact forces: bs_replicates
bs_replicates = draw_bs_reps(translated_force_b, np.mean, 10000)

# Compute fraction of replicates that are less than the observed Frog B force: p
p = np.sum(bs_replicates <= np.mean(force_b)) / 10000

# Print the p-value
print('p = ', p)
