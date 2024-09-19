import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso, Ridge
from sklearn.metrics import mean_squared_error

# Generate synthetic data
np.random.seed(42)
X, y = make_regression(n_samples=100, n_features=10, noise=0.1)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Fit a Ridge regression model
ridge_model = Ridge(alpha=1.0)  # Regularization strength
ridge_model.fit(X_train, y_train)
y_pred_ridge = ridge_model.predict(X_test)

# Fit a Lasso regression model
lasso_model = Lasso(alpha=0.4)  # Regularization strength
lasso_model.fit(X_train, y_train)
y_pred_lasso = lasso_model.predict(X_test)

# Calculate Mean Squared Error for both models
mse_ridge = mean_squared_error(y_test, y_pred_ridge)
mse_lasso = mean_squared_error(y_test, y_pred_lasso)

# Print the results
print("Ridge Regression Mean Squared Error:", mse_ridge)
print("Lasso Regression Mean Squared Error:", mse_lasso)

# Plot coefficients
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(range(len(ridge_model.coef_)), ridge_model.coef_, color='blue')
plt.title('Ridge Regression Coefficients')
plt.xlabel('Feature Index')
plt.ylabel('Coefficient Value')

plt.subplot(1, 2, 2)
plt.bar(range(len(lasso_model.coef_)), lasso_model.coef_, color='orange')
plt.title('Lasso Regression Coefficients')
plt.xlabel('Feature Index')
plt.ylabel('Coefficient Value')

plt.tight_layout()
plt.show()
