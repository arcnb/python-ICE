
import numpy as np
from sklearn.cluster import MeanShift
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as pllt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import style

style.use("classic")

centor = [[0, 0, 0], [5, 5, 5], [3, 10, 10]]

Y,_ = make_blobs(n_samples=500, centers=centor, cluster_std=1.5)

mesh = MeanShift()
mesh.fit(Y)
labeels = mesh.labels_
cc = mesh.cluster_centers_

print(cc)

cn = len(np.unique(labeels))

print("No of expected clustors:", cn)

colour = 10 * ['g', 'b', 'k', 'm', 'r', 'y', 'c']

print(colour)
print(labeels)

fig = pllt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(Y)):
    ax.scatter(Y[i][0], Y[i][1], Y[i][2], c=colour[labeels[i]], marker='o')

ax.scatter(cc[:, 0], cc[:, 1], cc[:, 2],
           marker="x", color='k', s=150, linewidths=5, zorder=10)

pllt.show()