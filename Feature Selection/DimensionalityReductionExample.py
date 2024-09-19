import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# Load the iris dataset
data = load_iris()
X = data.data
y = data.target

# Apply PCA
pca = PCA(n_components=2) ; X_reduced = pca.fit_transform(X)

# Create a DataFrame for the reduced data
df_reduced = pd.DataFrame(data=X_reduced, columns=['PC 1', 'PC 2'])
df_reduced['Target'] = y

# Plot the reduced dimensions
plt.figure(figsize=(8, 6))
scatter = plt.scatter(df_reduced['PC 1'], df_reduced['PC 2'],
                      c=df_reduced['Target'], cmap='viridis', edgecolor='k', s=100)

# Add labels and legend
plt.title('PCA of Iris Dataset')
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.colorbar(scatter, label='Target Classes')
plt.grid()
plt.show()
