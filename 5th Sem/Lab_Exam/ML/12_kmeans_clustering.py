# Program 12: K-Means Clustering on Mall Customers Dataset
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. Load dataset
df = pd.read_csv('datasets/mall_customers.csv')
X = df[['Annual_Income_k$', 'Spending_Score']]

# 2. Apply K-Means algorithm with k=5 clusters
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)
centroids = kmeans.cluster_centers_

# 3. Display Clusters and Centroids
print("=== Cluster Centers (Annual Income, Spending Score) ===")
for i, center in enumerate(centroids):
    print(f"Cluster {i}: Income = {center[0]:.2f}k$, Spending Score = {center[1]:.2f}")

print("\nCluster Distribution (Customer Count per Cluster):")
print(df['Cluster'].value_counts().sort_index())

print("\nSample Data with Assigned Clusters:")
print(df[['CustomerID', 'Annual_Income_k$', 'Spending_Score', 'Cluster']].head())

# 4. Visualize the Clusters
plt.figure(figsize=(8, 5))
colors = ['red', 'blue', 'green', 'cyan', 'magenta']

for i in range(5):
    cluster_points = X[df['Cluster'] == i]
    plt.scatter(cluster_points['Annual_Income_k$'], cluster_points['Spending_Score'],
                s=50, c=colors[i], label=f'Cluster {i}')

# Plot cluster centroids
plt.scatter(centroids[:, 0], centroids[:, 1], s=200, c='yellow', marker='X', edgecolors='black', label='Centroids')

plt.title('Customer Segmentation using K-Means Clustering')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/12_kmeans_clustering.png')
print("\nPlot saved as outputs/12_kmeans_clustering.png")
plt.show()
