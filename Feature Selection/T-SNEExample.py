import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.manifold import TSNE

# Load the iris dataset
data = load_iris()
X = data.data
y = data.target

# Apply t-SNE
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X)

# Create a DataFrame for the reduced data
df_tsne = pd.DataFrame(data=X_tsne, columns=['Component 1', 'Component 2'])
df_tsne['Target'] = y

# Plot the t-SNE results
plt.figure(figsize=(8, 6))
scatter = plt.scatter(df_tsne['Component 1'], df_tsne['Component 2'],
                      c=df_tsne['Target'], cmap='viridis', edgecolor='k', s=100)

# Add labels and legend
plt.title('t-SNE of Iris Dataset')
plt.xlabel('Component 1')
plt.ylabel('Component 2')
plt.colorbar(scatter, label='Target Classes')
plt.grid()
plt.show()
