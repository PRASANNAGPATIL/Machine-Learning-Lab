import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris = load_iris()
import pandas as pd
X = pd.DataFrame(iris.data)
#print(X)
y = pd.DataFrame(iris.target)

import numpy as np
np.random.seed(2)
colormap = np.array(['red', 'lime', 'black'])
plt.figure(figsize=(14,7))

from sklearn.cluster import KMeans
model = KMeans(n_clusters=3)
model.fit(X)
y_cluster_kmeans=model.predict(X)
plt.subplot(1, 2, 2)
plt.scatter(X[2],X[3], c=colormap[y_cluster_kmeans])
plt.title('K Mean Classification')

import sklearn.metrics as sm
print("KMeans algorithm Accuracy:",sm.accuracy_score(y, y_cluster_kmeans))

from sklearn.mixture import GaussianMixture
gmm = GaussianMixture(n_components=3)
gmm.fit(X)
y_cluster_gmm=gmm.predict(X)
plt.subplot(1, 2, 1)
plt.scatter(X[2],X[3], c=colormap[y_cluster_gmm])
plt.title('GMM Classification')

print("EM algorithm Accuracy:",sm.accuracy_score(y, y_cluster_gmm))
print(sm.confusion_matrix(y, y_cluster_gmm))
