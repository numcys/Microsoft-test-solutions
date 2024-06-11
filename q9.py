import numpy as np

def pca(X, num_components=None):
  X_centered = X - np.mean(X, axis=0)

  cov = np.cov(X_centered.T)

  eigenvalues, eigenvectors = np.linalg.eig(cov)

  sort_indices = np.argsort(eigenvalues)[::-1]
  eigenvalues = eigenvalues[sort_indices]
  eigenvectors = eigenvectors[:, sort_indices]

  if num_components is None:
    num_components = len(eigenvalues)
  explained_variance = eigenvalues[:num_components] / np.sum(eigenvalues)  
  principal_components = eigenvectors[:, :num_components]

  X_pca = X_centered @ principal_components

  return X_pca, explained_variance

X = np.array([[1, 2, 1],
              [3, 4, 3],
              [5, 6, 5]])

X_pca, explained_variance = pca(X)

print("Projected data (X_pca):")
print(X_pca)

print("\nExplained variance ratio:")
print(explained_variance)
