import pandas as pd
from sklearn.cluster import KMeans

datafile = "adult.csv"

# read list of words from file column_names.txt
column_names = open("column_names.txt", "r").read().splitlines()

# read data from file adult.csv
data = pd.read_csv(datafile, names=column_names, header=False)

X = data[['age', 'workclass', 'capital-loss']].copy()

# apply KMeans clustering to data
kmeans = KMeans(n_clusters=3).fit(X)

print("Cluster Centers :", kmeans.cluster_centers_)
print("Sum Squared Error :", kmeans.inertia_)
