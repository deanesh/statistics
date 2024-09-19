import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

# Load the iris dataset
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Combine features and target into a single DataFrame
df = pd.concat([X, y.rename("target")], axis=1)

# Calculate the correlation matrix
correlation_matrix = df.corr()

# Display the correlation of features with the target
target_correlation = correlation_matrix["target"].drop("target")

print("Correlation with target:\n", target_correlation)

# Select features with absolute correlation greater than a threshold (e.g., 0.3)
threshold = 0.3
selected_features = target_correlation[abs(target_correlation) > threshold].index.tolist()

print("\nSelected Features based on correlation threshold:", selected_features)
