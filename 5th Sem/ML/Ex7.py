import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

df = pd.read_csv("train_data_7.csv")

df = df.select_dtypes(include="number")
df = df.fillna(df.mean())

scaler = StandardScaler()
X = scaler.fit_transform(df)

k = 3

model = KMeans(n_clusters=k, random_state=42, n_init=10)
labels = model.fit_predict(X)

df["Cluster"] = labels

print("Clustered Data:")
print(df)

print("\nSilhouette Score:", round(silhouette_score(X, labels), 4))

print("\nCluster Centers:")
print(model.cluster_centers_)

plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(
    model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    marker="X",
    s=200
)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("K-Means Clustering")
plt.show()