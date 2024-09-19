import pandas as pd
'''
Covariance measures the degree to which two variables change together. 
Unlike correlation, which is normalized and thus dimensionless, 
covariance is not standardized and depends on the units of the variables. 
Correlation is essentially a normalized version of covariance.
'''

# Sample data
data = {'x': [1, 2, 3, 4, 5], 'y': [2, 4, 5, 4, 5]}

df = pd.DataFrame(data)

# Calculate covariance
covariance = df['x'].cov(df['y'])

print("Covariance (pandas):", covariance)
