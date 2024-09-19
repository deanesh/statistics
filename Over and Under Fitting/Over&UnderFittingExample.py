import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generate synthetic data
np.random.seed(0)
X = np.random.rand(100, 1) * 10  # 100 data points between 0 and 10
y = np.sin(X).ravel() + np.random.normal(0, 0.5, X.shape[0])  # Add noise

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit a polynomial regression model with degree 1 (Underfitting)
poly1 = PolynomialFeatures(degree=1)
X_poly1_train = poly1.fit_transform(X_train)
X_poly1_test = poly1.transform(X_test)

model1 = LinearRegression()
model1.fit(X_poly1_train, y_train)
y_pred1 = model1.predict(X_poly1_test)

# Fit a polynomial regression model with degree 10 (Overfitting)
poly10 = PolynomialFeatures(degree=10)
X_poly10_train = poly10.fit_transform(X_train)
X_poly10_test = poly10.transform(X_test)

model10 = LinearRegression()
model10.fit(X_poly10_train, y_train)
y_pred10 = model10.predict(X_poly10_test)

# Plot the results
plt.figure(figsize=(12, 6))

# Plot Underfitting
plt.subplot(1, 2, 1)
plt.scatter(X, y, color='blue', label='Data Points')
plt.scatter(X_test, y_pred1, color='red', label='Predictions (Degree 1)')
plt.title('Underfitting (Degree 1)')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()

# Plot Overfitting
plt.subplot(1, 2, 2)
plt.scatter(X, y, color='blue', label='Data Points')
plt.scatter(X_test, y_pred10, color='red', label='Predictions (Degree 10)')
plt.title('Overfitting (Degree 10)')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()

plt.tight_layout()
plt.show()

# Print MSE for both models
print("Mean Squared Error (Degree 1):", mean_squared_error(y_test, y_pred1))
print("Mean Squared Error (Degree 10):", mean_squared_error(y_test, y_pred10))
