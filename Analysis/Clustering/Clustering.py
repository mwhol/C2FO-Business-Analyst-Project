from sklearn.cluster import KMeans
from sklearn import preprocessing

import pandas as pd
from pandas.api.types import CategoricalDtype
pd.set_option('mode.chained_assignment', None)

from matplotlib import pyplot as plt

#loading in data and setting to just a relevant subset
xls = pd.ExcelFile("Superstore.xls")
orders = pd.read_excel(xls, 'Orders')
ordersClean = orders[["Ship Mode", "Segment", "Region", "Category", "Profit"]]

# We have text columns that we need to clean and we need to clean them differently
# Shipping mode has an order to it that we need to preserve (ordinal)
# Segment, Region and Category have no real order (nominal)
# We will fix these problems in different ways
le = preprocessing.LabelEncoder()

# First we take our Shipping Mode column and peek at the possible values in it
print("Ship Mode Values: ", set(list(ordersClean["Ship Mode"].values)))

# We construct our category ordering and apply it to the shipping data
ship_data_type = CategoricalDtype(categories=['Standard Class', 'Second Class', 'First Class', 'Same Day'], ordered=True)
ordersClean.loc[:,"Ship Mode"] = ordersClean["Ship Mode"].astype(ship_data_type)
ordersClean.loc[:,"Ship Mode"] = le.fit_transform(ordersClean.loc[:,"Ship Mode"].values)

# For Segment, Region and Category we could use the sklearn encoders but a quicker
# way is to just use the pandas get_dummies function
ordersFinal = pd.get_dummies(ordersClean, drop_first=True)

# Now that our data has been encoded in a readable format for the kmeans module
# we can begin to use that.

# First we'll run an elbow test (ty stack overflow for code)
distorsions = []
for k in range(2, 20):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(ordersFinal)
    distorsions.append(kmeans.inertia_)

fig = plt.figure(figsize=(10, 10))
plt.plot(range(2, 20), distorsions)
plt.grid(True)
plt.title('Elbow curve')
fig.savefig("Elbow.png")

# Our graph seems pretty smooth, maybe the data isn't that fit for a cluster
# analysis. However there is a kink at 6 so we'll run with 6 clusters

model=KMeans(n_clusters=6)
model.fit(ordersFinal)

# Okay, now we have our model but we also have 9 dimensions so it's not exactly
# the easiest thing to visualize them, let's take a look at the data:
clusters = model.predict(ordersFinal)
clusterList = list(clusters)

# Hmm, seems like most elements are in one cluster, let's do a count

for x in range(6):
	print(f"Cluster {x}: ", clusterList.count(x))

# This is because KMeans works best on continuous data, it's actually a bit of
# an inappropriate test for data like this, but we're using it as an example
# to show both an unsupervised model and the required cleaning to run it so
# we'll generate a graph and leave it there for the morning. If I were to continue
# I'd probably try a PCA to reduce d

plt.clf()
abc = plt.scatter(ordersFinal["Ship Mode"], ordersFinal["Profit"], c=clusters, s=10)
abc.figure.savefig("shipMode_Profit_Clusters.png")