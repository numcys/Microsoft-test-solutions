import numpy as np

def kmeans(X, k):
  centroids = X[np.random.choice(X.shape[0], k)]

  while True:
    prev_centroids = centroids.copy()  

    clusters = {i: [] for i in range(k)} 
    for i in range(X.shape[0]):
      distances = np.linalg.norm(X[i] - centroids, axis=1)  
      cluster = np.argmin(distances)  
      clusters[cluster].append(i)

    centroids = np.array([np.mean(X[clusters[i]], axis=0) for i in clusters])

    if np.all(np.linalg.norm(prev_centroids - centroids, axis=1) < 1e-6):  
      break

  return clusters, centroids

X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
k = 2

clusters, centroids = kmeans(X, k)

print("Cluster assignments:")
for i, cluster in clusters.items():
  print(f"Cluster {i}: {cluster}")
print(f"\nCentroids:\n{centroids}")
