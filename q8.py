import numpy as np

def gradient_descent(X, y, learning_rate, iterations):
    weights = np.zeros(X.shape[1])
    m = len(y)
    
    for _ in range(iterations):
        predictions = np.dot(X, weights)

        error = predictions - y
        
        gradient = np.dot(X.T, error) / m
        weights -= learning_rate * gradient
    
    return weights

np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

X_b = np.c_[np.ones((100, 1)), X]

learning_rate = 0.01
iterations = 1000

weights = gradient_descent(X_b, y.ravel(), learning_rate, iterations)
print("Weights:", weights)
