import numpy as np

def linear_regression(X, y):
  X = np.hstack((np.ones((X.shape[0], 1)), X))  # Add bias term
  w = np.linalg.pinv(X.T @ X) @ X.T @ y
  return w

def predict(X, w):
  X = np.hstack((np.ones((X.shape[0], 1)), X))
  return X @ w

# Sample data
X = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([2, 7, 13])

# Train the model
w = linear_regression(X, y)

# New data point for prediction
new_data = np.array([[10, 11]])

# Predict target value
predicted_value = predict(new_data, w)

print(f"Predicted value for new data point: {predicted_value}")
