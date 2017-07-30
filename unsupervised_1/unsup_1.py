import matplotlib.pyplot as plt

from unsupervised_1.unsup_c import points

xs = points[:, 0]
ys = points[:, 1]
plt.scatter(xs,ys)
plt.show()