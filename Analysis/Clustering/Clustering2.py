from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn import datasets

import pandas as pd

from matplotlib import pyplot as plt

#Get Data (comments shorter this time around)
iris = datasets.load_iris()
X = iris.data
y = iris.target

#Learn about the data
print(iris.__dir__())
print(iris.feature_names)


#Run the Elbow Diagram
distorsions = []
for k in range(2, 20):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    distorsions.append(kmeans.inertia_)

fig = plt.figure(figsize=(10, 10))
plt.plot(range(2, 20), distorsions)
plt.grid(True)
plt.title('Elbow curve')
fig.savefig("Elbow2.png")

#
model=KMeans(n_clusters=3)
model.fit(X)

clusters = model.predict(X)
clusterList = list(clusters)

# Hmm, seems like most elements are in one cluster, let's do a count

for x in range(3):
	print(f"Cluster {x}: ", clusterList.count(x))

# This is because KMeans works best on continuous data, it's actually a bit of
# an inappropriate test for data like this, but we're using it as an example
# to show both an unsupervised model and the required cleaning to run it so
# we'll generate a graph and leave it there for the morning. If I were to continue
# I'd probably try a PCA to reduce d

plt.clf()
abc = plt.scatter(X[:,0], X[:,2], c=clusters, s=10)
abc.figure.savefig("iris_clusters.png")
