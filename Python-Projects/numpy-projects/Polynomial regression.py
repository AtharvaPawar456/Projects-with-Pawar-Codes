# Polynomial regression: Implement a polynomial regression model using NumPy.

import numpy as np
import matplotlib.pyplot as plt

def polynomial_regression(x, y, degree):
    X = np.vander(x, degree + 1, increasing=True)
    coefficients = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
    return coefficients

def predict(coefficients, x):
    degree = len(coefficients) - 1
    X = np.vander(x, degree + 1, increasing=True)
    y_pred = np.dot(X, coefficients)
    return y_pred

def plot_polynomial_regression(x, y, y_pred):
    plt.scatter(x, y, color='red', label='Actual')
    plt.plot(x, y_pred, color='blue', label='Predicted')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Polynomial Regression')
    plt.legend()
    plt.show()

# Test case
x = np.array([1, 2, 3, 4, 5])
y = np.array([4, 2, 1, 3, 6])
degree = 3

coefficients = polynomial_regression(x, y, degree)
y_pred = predict(coefficients, x)

plot_polynomial_regression(x, y, y_pred)
