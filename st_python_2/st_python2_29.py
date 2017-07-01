from datacamp.lib import *
from data.control_treated import *
# Compute the difference in mean sperm count: diff_means
#CNT_TEST = 10000
CNT_TEST = 10000
diff_means = diff_of_means(control,treated)

# Compute mean of pooled data: mean_count
mean_count = np.mean(np.concatenate((control,treated)))

# Generate shifted data sets
control_shifted = control - np.mean(control) + mean_count
treated_shifted = treated - np.mean(treated) + mean_count

# Generate bootstrap replicates
bs_reps_control = draw_bs_reps(control_shifted,
                       np.mean, size=CNT_TEST )
bs_reps_treated = draw_bs_reps(treated_shifted,
                       np.mean, size=CNT_TEST )

# Get replicates of difference of means: bs_replicates
bs_replicates = bs_reps_control-bs_reps_treated

positive_replicates = bs_replicates - np.mean(control) + np.mean(treated)
# Compute and print p-value: p
p = np.sum(positive_replicates > 0) \
            / len(bs_replicates)
print('p-value =', p)
