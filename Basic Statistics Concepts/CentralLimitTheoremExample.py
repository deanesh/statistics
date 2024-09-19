import sys
'''
The central limit theorem states that distribution of sample mean approaches a 
normal distribution as sample size becomes large, regardless of the original distribution 
of data. This theorem is important because it justifies the use of
normal distribution-based techniques in inferential statistics and model evaluation.
'''
import numpy as np
import matplotlib.pyplot as plt

# Parameters
population_size = 10000  # Size of the population
sample_size = 30         # Size of each sample
num_samples = 1000       # Number of samples

# Generate a population from a uniform distribution
population = np.random.uniform(low=0, high=100, size=population_size)

# Collect sample means
sample_means = []
for _ in range(num_samples):
    sample = np.random.choice(population, size=sample_size)
    sample_means.append(np.mean(sample))
# Plotting
plt.figure(figsize=(12, 6))

# Plot the population distribution
plt.subplot(1, 2, 1)
plt.hist(population, bins=30, color='lightblue', alpha=0.7)
plt.title('Population Distribution (Uniform)')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Plot the sample means distribution
plt.subplot(1, 2, 2)
plt.hist(sample_means, bins=30, color='salmon', alpha=0.7)
plt.title('Distribution of Sample Means')
plt.xlabel('Sample Mean')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
