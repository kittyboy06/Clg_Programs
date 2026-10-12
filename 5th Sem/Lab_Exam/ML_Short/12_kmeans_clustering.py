import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv('datasets/mall_customers.csv')
X = df[['Annual_Income_k$', 'Spending_Score']]

kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

print("Cluster Centers:\n", kmeans.cluster_centers_)
print("\nCluster Distribution:\n", df['Cluster'].value_counts().sort_index())

# Visualize clusters and centroids
plt.scatter(X['Annual_Income_k$'], X['Spending_Score'], c=df['Cluster'], cmap='rainbow', s=50)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='black', marker='X', label='Centroids')
plt.title('K-Means Clustering (k=5)')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()
