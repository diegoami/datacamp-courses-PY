import pandas as pd
from datacamp.lib import *

df = pd.read_csv('../data/horned_frogs.csv')

force_a = df[df['ID']=='A']['impact_force'].as_matrix()
force_b = df[df['ID']=='B']['impact_force'].as_matrix()

# Compute difference of mean impact force from experiment: empirical_diff_means
empirical_diff_means = diff_of_means(force_a, force_b)

# Draw 10,000 permutation replicates: perm_replicates
perm_replicates = draw_perm_reps(force_a, force_b, diff_of_means, size=10000)

# Compute p-value: p
p = np.sum(perm_replicates >= empirical_diff_means) / len(perm_replicates)

# Print the result
print('p-value =', p)
