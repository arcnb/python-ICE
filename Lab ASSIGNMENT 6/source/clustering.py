import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

X = np.array([[2,2],[2.2,2.2],[3,3],[4,4],[3,3.5], [3.5,4]])
plt.scatter(X[:,0], X[:,1], s=60)

linkage_matrix = linkage(X, "single")
dendogram = dendrogram(linkage_matrix, truncate_mode='none')
plt.title("clustering")
plt.show()