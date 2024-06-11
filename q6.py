import numpy as np

def sigmoid(z):
  return 1 / (1 + np.exp(-z))

def cost_function(X, y, w):
  m = len(y)
  h = sigmoid(X @ w)  
  return -1/m * np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))


X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([0, 1, 1])


w = np.zeros(X.shape[1]) 

cost = cost_function(X, y, w)
print(f"Cost (average binary cross-entropy): {cost}")
